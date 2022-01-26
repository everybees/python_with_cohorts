# 4.6 (Modified average Function) The average function we defined in Section 4.11 can receive any number of arguments.
# If you call it with no arguments, however, the function causes a ZeroDivisionError.
# Reimplement average to receive one required argument and the arbitrary argument list argument *args,
# and update its calculation accordingly. Test your function. The function will always require at least one argument,
# so you’ll no longer be able to get a ZeroDivisionError. When you call average with no
# arguments, Python should issue a TypeError indicating "average() missing 1 required
# positional argument."


def average(game, *args):
    if not args:
        return game / len(str(game))
    elif args:
        return (game + sum(args)) / (len(args) + len(str(game)))


print(average(1, 2, 3, 4, 5))



