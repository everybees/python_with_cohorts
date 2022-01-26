import datetime

while(True):
    city = input("Enter the city: ")

    current_time = datetime.datetime.now();
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    if city == 'Boston':
        hour = hour - 4
    elif city == 'Tokyo':
        hour = hour + 9
    elif city == 'Chicago':
        hour = hour - 5
    elif city == 'Seattle':
        hour = hour - 7
    elif city == 'Kolkota':
        hour = hour + 5
        minutes = minute + 30
    elif city == 'Cairo':
        hour = hour + 2

