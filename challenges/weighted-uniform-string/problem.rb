#!/bin/ruby

s = gets.strip
n = gets.strip.to_i
# ALPHABET = "abcdefhijklmnopqrstuvwxyz".split('')

# def weight?(s)
# 	ALPHABET.find_index(s) || -1
# end


ar = []
pr = ''
w = 0
for i in (0...s.length)
    w = 0 if s[i] != pr
    w += s[i].ord - 96
    ar.push w
    pr = s[i]
end

for a0 in (0..n-1)
	x = gets.strip.to_i
    puts ar.find_index(x) ? "Yes" : "No"
end

