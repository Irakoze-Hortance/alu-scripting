#!/usr/bin/env ruby
Format = ARGV[0].scan(/from:(.+)|to:(.\w+)|flags:([0-9:-]+)/)
List = [Format[0].compact, Format[1].compact, Format[2].compact]
puts List.join(',')
