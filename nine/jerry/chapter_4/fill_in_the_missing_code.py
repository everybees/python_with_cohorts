# 4.5 (Fill in the Missing Code?) Replace the ***s in the seconds_since_midnight function
# so that it returns the number of seconds since midnight. The function should receive
# three integers representing the current time of day. Assume that the hour is a value from
# 0 (midnight) through 23 (11 PM) and that the minute and second are values from 0 to 59.
# Test your function with actual times. For example, if you call the function for 1:30:45 PM
# by passing 13, 30 and 45, the function should return 48645.
# def seconds_since_midnight(***):
#  hour_in_seconds = ***
#  minute_in_seconds = ***
#  return ***


def seconds_since_midnight(hour, minute, seconds):
    hour_in_seconds = hour * 3600
    minute_in_seconds = minute * 60
    return hour_in_seconds + minute_in_seconds + seconds


time = seconds_since_midnight(13, 30, 45)
print(time)
