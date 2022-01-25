# Initialize total to zero
# Initialize grade counter to zero
# Input the first grade (possibly the sentinel)
# While the user has not entered the sentinel
# Add this grade into the running total
# Add one to the grade counter
# Input the next grade (possibly the sentinel)
# If the counter is not equal to zero
# Set the average to the total divided by the counter
# Display the average
# Else
# Display “No grades were entered”

total = 0
grade_counter = 0

user_input = int(input('Enter a grade or -1 to exit'))

while user_input != -1:
    total += user_input
    grade_counter+= 1

    user_input = int(input('Enter a grade or -1 to exit'))

if(grade_counter != 0):
        average = total/grade_counter
        print(average)
else:
        print('No grades were entered')