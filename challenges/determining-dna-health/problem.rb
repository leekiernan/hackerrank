#!/bin/ruby

number_of_genes = gets.strip.to_i
genes = gets.strip.split(' ')
health = gets.strip.split(' ').map(&:to_i)
gene_map = Hash[genes.zip(health)]
s = gets.strip.to_i

min = nil
max = nil
s.times do |a|
    first, last, d = gets.strip.split(' ')
    first = first.to_i
    last = last.to_i

    genes_against = genes[first..last]
    health_against = health[first..last]
    track = 0
    genes_against.each_with_index do |g,ix|
    	step = g.length
    	c = 0
    	while (c+step) <= d.length
    		if g == d[c,step]
	    		track += health_against[ix]
	    	end
    		c += 1
    	end
    end

    max = track if !max || track > max
    min = track if !min || track < min
end

puts "#{min} #{max}"
