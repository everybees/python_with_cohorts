tp = int(input('Enter a fived-digit number:'))
for i in range(5):
    tp1 = tp // 10000
    tp2 = (tp % 10000) // 1000
    tp3 = ((tp % 10000) % 1000) // 100
    tp4 = (((tp % 10000) % 1000) % 100) // 10
    tp5 = (((tp % 10000) % 1000) % 100) % 10
if tp1 == tp5 and tp2 == tp4:
    print(tp, 'is a palindrome')
else:
    print(tp,'is not a palindrome')