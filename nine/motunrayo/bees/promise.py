import random


counter = 0
while counter < 5000:
    sentence = ("I", "will", "not", "disturb", "Semicolon", "again")
    shuffled_sentence = " ".join(random.sample(sentence,len(sentence)))
    print("{}".format(shuffled_sentence), sep=" ")
    counter += 1
