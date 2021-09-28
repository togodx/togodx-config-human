require 'json'
require 'open-uri'
require 'yaml'

class Property
  def initialize(property)
    @id = property["propertyId"]
    @label = property["label"]
    @desc = property["description"]
    @data = property["data"]
    @data_source = property["dataSource"]
    @data_source_url = property["dataSourceUrl"]
    @data_source_version = property["dataSourceUrlVersion"]
    @update = property["updatedAt"]
    @key = property["primaryKey"]
    @keyLabel = property["keyLabel"]
    @view_method = property["viewMethod"]
    @datamodel = define_datamodel
  end
  attr_accessor :id, :label, :desc, :data, :data_source, :data_source_url, :update, :key, :keyLabel

  def define_datamodel
    if @view_method
      :distribution
    else
      :classification
    end
  end

  def attribute
    attr = {
      id: @id,
      label: @label,
      description: @desc,
      api: @data,
      dataset: @key,
      datamodel: @datamodel,
      source: [
        {
          label: @data_source,
          url: @data_source_url,
          version: @data_source_version,
          updated: @update,
        },
      ],
    }
    attr[:viewMethod] = @viewMethod if @viewMethod
    attr
  end
end

class Subject
  def initialize(subject)
    @id = subject["subjectId"]
    @label = subject["subject"]
    @properties = subject["properties"].map{|prop| Property.new(prop) }
  end
  attr_accessor :id, :label, :properties
end

if __FILE__ == $0
  workdir_path = File.expand_path(File.dirname(__FILE__))

  properties_json_path = "#{workdir_path}/../config/properties.json"
  properties = JSON.load(open(properties_json_path).read)

  # togoid_dataset_config_url = 'https://raw.githubusercontent.com/dbcls/togoid-config/main/config/dataset.yaml'
  # id_config = YAML.load(open(togoid_dataset_config_url).read)
  # id_examples = id_config.each_with_object({}) do |(id, dataset), hash|
  #   examples = dataset["examples"]
  #   hash[id] = examples[0].slice(0,5) if examples
  # end

  id_examples_json_path = "#{workdir_path}/../config/human_examples.json"
  examples = JSON.load(open(id_examples_json_path).read)

  config = properties.each_with_object({}) do |subject, hash|
    hash[:categories] ||= []
    hash[:attributes] ||= {}
    hash[:datasets] ||= {}

    s = Subject.new(subject)

    # identifiers
    ids = s.properties.map{|p| { dataset: p.key, label: p.keyLabel } }.uniq

    ids.each do |id|
      type = id.delete(:dataset)
      id[:template] = "https://raw.githubusercontent.com/togodx/togodx-config-human/develop/templates/#{type}.hbs"

      id[:target] = case type
      when "togovar"
        false
      else
        true
      end

      id[:examples] = examples[type]

      hash[:datasets][type] = id
    end

    s.properties.each do |prop|
      a = prop.attribute
      id = a.delete(:id)
      hash[:attributes][id] = a
    end

    # categories and attributes
    h = {
      id: s.id,
      label: s.label,
      attributes: s.properties.map{|p| p.id }
    }

    hash[:categories] << h
  end

  id_types = config[:datasets].keys
  id_types.each do |id|
    config[:datasets][id][:conversion] = id_types.each_with_object({}) do |oid, hash|
      hash[oid] = "https://api.togoid.dbcls.jp/convert?format=json&route=#{id},#{oid}&ids=" if id != oid
    end
  end

  puts JSON(config)
end
