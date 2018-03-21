#!/bin/ruby

def detect_html_links(line)
	line.scan(/<a\s.*?href=\"([^\"\s]*)?\".*?>(?:<.*?>)?\s?([^<]+)?/).each do |match|
		puts "#{match[0]},#{match[1]}"
	end
end

n = gets.strip.to_i
n.times { |line| detect_html_links gets.strip }
