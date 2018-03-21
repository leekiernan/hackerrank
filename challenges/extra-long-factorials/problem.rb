#!/bin/ruby

def extraLongFactorials(n, count)
    return puts count if n == 1
    extraLongFactorials n - 1, count * n
end

n = gets.strip.to_i
extraLongFactorials(n, 1)

