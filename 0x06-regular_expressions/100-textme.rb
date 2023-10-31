#!/usr/bin/env ruby
# This script outputs script should output: [SENDER],[RECEIVER],[FLAGS]

input = ARGV[0]
matches = input.scan(/\[from:(\+?\w*)\]\s\[to:(\+?\w*)\]\s\[flags:(\S*)\]/)

formatted_matches = matches.map do |match|
  match.join(',')
end

puts formatted_matches.join(',')

