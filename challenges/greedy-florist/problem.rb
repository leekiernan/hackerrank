#!/bin/ruby

def getMinimumCost(n, k, c)
    # Complete this function
end

n, k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
c = gets.strip
c = c.split(' ').map(&:to_i)
minimumCost = getMinimumCost(n, k, c)
puts minimumCost;
