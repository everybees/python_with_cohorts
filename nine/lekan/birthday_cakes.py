import sys
def birhtdayCakeCandles(candles):
    count = 0
    temp = candles[0]
    for i in range(1, len(candles)):
        if candles[i] > temp:
            temp = candles[i]

    for i in range(0, len(candles)):
        if candles[i] == temp:
            count += 1
    return c

