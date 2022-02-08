def seconds_since_midnight(hour, minutes, second):
    hour_in_seconds = 3600
    minute_in_seconds = 60
    return (hour * hour_in_seconds) + (minute_in_seconds * minutes) + second


result = seconds_since_midnight(13, 30, 45)
print(result)
