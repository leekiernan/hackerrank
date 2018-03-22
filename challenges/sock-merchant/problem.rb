#!/bin/ruby

def sockMerchant(n, ar)
    d = {}
    m = 0
    ar.each do |c|
        if d[c]
            m += 1
            d.delete(c)
        else
            d[c] = true
        end
    end
    return m
end

n = gets.strip.to_i
ar = gets.strip
ar = ar.split(' ').map(&:to_i)
result = sockMerchant(n, ar)
puts result;

