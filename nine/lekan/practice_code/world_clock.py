import datetime


def print_time(hours, minutes, seconds):
    return hours, ':', minutes, ":", seconds


while True:
    city = input("Enter the city: ")

    current_time = datetime.datetime.now();
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    if city == 'Boston':
        hour = hour - 4
        print_time(hour, minute, second)
    elif city == 'Tokyo':
        hour = hour + 9
        print_time(hour, minute, second)
    elif city == 'Chicago':
        hour = hour - 5
        print_time(hour, minute, second)
    elif city == 'Seattle':
        hour = hour - 7
        print_time(hour, minute, second)
    elif city == 'Kolkota':
        hour = hour + 5
        minutes = minute + 30
        print_time(hour, minutes, second)
    elif city == 'Cairo':
        hour = hour + 2
        print_time(hour, minute, second)

