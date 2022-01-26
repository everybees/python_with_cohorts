tp = int(input('Enter a fived-digit number:'))
for i in range(5):
    tp1 = tp // 10000
    tp2 = (tp % 10000) // 1000
    tp3 = ((tp % 10000) % 1000) // 100
    tp4 = (((tp % 10000) % 1000) % 100) // 10
    tp5 = (((tp % 10000) % 1000) % 100) % 10
print(tp1,end=' ')
print(tp2,end=' ')
print(tp3,end=' ')
print(tp4,end=' ')
print(tp5,end=' ')