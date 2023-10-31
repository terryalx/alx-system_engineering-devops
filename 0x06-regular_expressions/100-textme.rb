#!/usr/bin/env ruby
input = ARGV[0]
matches = input.scan(/from:(\w+)|to:(\w+)|flags:([0-9:-]+)/)

formatted_matches = matches.map do |match|
  match.compact.join(':')
end

puts formatted_matches.join(',')

