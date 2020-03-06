#/usr/bin/env ruby
# Get days since born

require 'pp'
require 'date'

birthday = "1984/07/28"

birthDate = Date.parse(birthday)
now = DateTime.now

diff = now.mjd - birthDate.mjd
birthdiff = diff.to_s
finalnum = birthdiff[0..1] + "," + birthdiff[2..-1]
print "\nContragulations! You have been alive #{finalnum} days on the planet!\n\n"




