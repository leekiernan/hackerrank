#!/bin/ruby

def encryption(s)
    sqr = Math.sqrt s.length
    grid = s.scan(/\w{0,#{sqr.ceil}}/).map { |m| m.split('') }
    out = []
    (0...sqr.ceil).each do |n|
        (0...sqr.round).each { |nn| out.push grid[nn][n] if grid[nn][n] && grid[nn][n] != "" }
        out.push ' '
    end
    return out.join.strip
end

s = gets.strip
result = encryption(s.gsub(/\s+/, ""))
puts result
