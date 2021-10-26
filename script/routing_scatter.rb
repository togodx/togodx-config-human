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
    next if source == "ensembl_transcript"
    routes = dataset_category.each_with_object({}) do |(target, t_cat), obj|
      next if target == "ensembl_transcript"
      if source != target
        route_s_t = routing["route"][s_cat][t_cat]
        route_t_s = routing["route"][t_cat][s_cat]

        direction = route_s_t ? :fwd : :rev

        route = case direction
        when :fwd
          route_s_t[0]
        when :rev
          route_t_s[0]
        end

        # exceptions
        # mondo-medgen-hp
        if (source == "mondo" && target == "hp")
          route = route.push("medgen")
        elsif (source == "hp" && target == "mondo")
          route = route.unshift("medgen")
        end

        # compound to mesh
        if (s_cat == "compound" && target == "mesh") or (t_cat == "compound" && source == "mesh")
          route.pop
        end

        route_complete = case direction
        when :fwd
          [source, route, target].flatten.uniq
        when :rev
          [target, route, source].flatten.reverse.uniq
        end

        obj[target] = route_complete.join(",")
      end
    end
    obj[source] = routes.sort_by{|key, value| key }.each_with_object({}){|arr, obj| obj[arr[0]] = arr[1]}
  end
  puts JSON(sections.sort_by{|key, value| key }.each_with_object({}){|arr, obj| obj[arr[0]] = arr[1]})
end
