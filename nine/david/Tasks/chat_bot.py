import datetime
import random
import time
import json


def chatbot():
    response = "yes"
    while response == "yes":

        question = input("What's that your question sef?\n").split()

        dictionary = open("C:/Users/US CHIPS/python_with_cohorts/nine/david/Tasks/david.json")
        
        dictionary = json.load(dictionary)

        reply = []

        # question = [x.lower() for x in question]

        question = question
           

        if ["exit"] == question:
            print("Existing...")
            break

        for key in question:
            if key in dictionary.keys():
                reply.append(random.choice(dictionary[key]))

            if reply:
                print(random.choice(reply))
            else:
                print("Ogbeni, don't stress me.... Ask better question biko!")

        time.sleep(1)
        print()

        response = input("Do you want to chat more? (yes or no)\n").lower()
        if response == 'no':
            print("Bye!")

chatbot()
