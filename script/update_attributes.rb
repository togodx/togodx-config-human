require 'json'

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
      data: [
        {
          label: @data_source,
          url: @data_source_url,
          version: @data_source_version,
          updateDate: @update,
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
  properties_json_path = ARGV[0]
  properties = JSON.load(open(properties_json_path).read)
  config = properties.each_with_object({}) do |subject, hash|
    hash[:tracks] ||= []
    hash[:attributes] ||= {}
    hash[:datasets] ||= {}

    s = Subject.new(subject)

    # identifiers
    ids = s.properties.map{|p| { dataset: p.key, label: p.keyLabel } }.uniq

    ids.each do |id|
      type = id.delete(:dataset)
      id[:template] = "https://raw.githubusercontent.com/togodx/togodx-config-human/develop/templates/#{type}.hbs"
      id[:target] = true

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

    hash[:tracks] << h
  end

  id_types = config[:datasets].keys
  id_types.each do |id|
    config[:datasets][id][:conversion] = id_types.each_with_object({}) do |oid, hash|
      hash[oid] = "https://api.togoid.jp/convert?format=json&route=#{id},#{oid}" if id != oid
    end
  end

  puts JSON(config)
end
