#!/bin/ruby

def timeInWords(h, m)
    # Complete this function
    # 15/45 quarter
    # 30 half
    # o' clock
    words_hash = {
    	1=>"one", 2=>"two", 3=>"three", 4=>"four", 5=>"five", 6=>"six", 7=>"seven", 8=>"eight", 9=>"nine",
    	10=>"ten", 11=>"eleven", 12=>"twelve", 13=>"thirteen", 14=>"fourteen", 15=>"fifteen", 16=>"sixteen",
    	17=>"seventeen", 18=>"eighteen", 19=>"nineteen", 20=>"twenty",
    	21=>"twenty one", 22=>"twenty two", 23=>"twenty three", 24=>"twenty four", 25=>"twenty five", 26=>"twenty six", 27=>"twenty seven", 28=>"twenty eight", 29=>"twenty nine",
    }

    if m == 0
    	return "#{words_hash[h]} o' clock"
    end

    to_from = m > 30 ? 'to' : 'past'
    m = 60-m if m > 30
    # if m - 20 > 0

    if m == 30
    	mm = "half"
    elsif m % 15 == 0
    	mm = "quarter"
    else
    	minutes = (m == 1 ? 'minute' : 'minutes')
    	mm = "#{words_hash[m]} #{minutes}"
    end

    return "#{mm} #{to_from} #{to_from == 'to' ? words_hash[h+1] : words_hash[h]}"
end

h = gets.strip.to_i
m = gets.strip.to_i
result = timeInWords(h, m)
puts result
