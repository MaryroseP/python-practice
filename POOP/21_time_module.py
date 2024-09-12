# ***********************************************
import time
# ***********************************************
print(time.ctime())    # convert a time expressed in seconds since epoch to a readable string
#                         epoch = when the computer thinks time began

print(time.time())     # return current seconds since epoch

print(time.ctime(time.time())) # Tells the time since epoch in a readable format

time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
                            # syntax time.strftimr(format,time_object)
                            # check documentation for the format samples)
print(local_time)

# Time tuple >>> string
utc_time_object = time.gmtime()
utc_time = time.strftime("%B %d %Y %H:%M:%S",utc_time_object)
# Convert a time tuple to a string according to a format specification.
print(utc_time)

# string >>> time tuple (according to specified format)
time_string = "12 September, 2024"
newtime = time.strptime(time_string,"%d %B, %Y")
# Parse a string to a time tuple according to a format specification.
print(newtime)


# (year,month,day,hours,minutes,secs, #day of the week, #day of the year, dst)
time_tuple = (2024,9,12,4,20,0,0,0,0)
time_new = time.asctime = time.asctime(time_tuple)
print(time_new)

