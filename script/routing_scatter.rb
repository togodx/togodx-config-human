require 'json'

if __FILE__ == $0
  workdir_path = File.expand_path(File.dirname(__FILE__))

  routing_json_path = "#{workdir_path}/../config/routing_org.json"
  routing = JSON.load(open(routing_json_path).read)

  dataset_category = routing["database"].each_with_object({}) do |(key, value), obj|
    value.each do |v|
      obj[v] = key
    end
  end

  sections = dataset_category.each_with_object({}) do |(source, s_cat), obj|
    obj[source] = dataset_category.each_with_object({}) do |(target, t_cat), obj|
      if source != target
        route_s_t = routing["route"][s_cat][t_cat]
        route_t_s = routing["route"][t_cat][s_cat]
        route = route_s_t ? [source, route_s_t[0], target].flatten : [target, route_t_s[0], source].flatten.reverse
        obj[target] = route.uniq.join(",")
      end
    end
  end

  puts JSON(sections)
end
