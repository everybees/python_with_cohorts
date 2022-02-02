import datetime
import random
import time


def chatbot():
    response = "yes"
    while response == "yes":

        question = input("Ask me any Question?\n").split()

        dictionary = {
            "time": ["The time is " + str(datetime.datetime.now().time())],
            "name": ["My name is Siri", "my name is Sam", "my name is Alexa", "my name is Sholz"],
            "love": ["Ja, ich liebe dich!", "Nein, ich liebe dich nicht", "Scheiße", "Love is wicked"],
            "eat": ["Yeah, baby!", "Nah 😢"],
            "relationship": ["I'm currently single ", "I'm in a lovely relationship" " I only do mutual relationships"],
            "programs": ["I write python sometimes", "I'm learning java", "I write Javascript",
                         "I'm learning C#"],
            "country": ["I've been to Canada", "I'm from the UK", "Lovely Kenya", "Extremely beautiful Latvia"],
            "old": ["I am " + str(random.randrange(1, 100)) + " years old"],
            "play": ["I like playing Chess", "I play computer games", "I prefer reading"],
            "sleep": ["I rarely sleep", "I can't shutdown, I can only have a 10sec power nap daily"]
        }

        reply = []

        question = [x.lower() for x in question]

        if ["exit"] == question:
            print("Exiting...")
            break

        for key in question:
            if key in dictionary.keys():
                reply.append(random.choice(dictionary[key]))

                if reply:
                    print(random.choice(reply))
                else:
                    print("Can't say for now.... you can check later!")

        time.sleep(1)
        print()

        response = input("Do you want to chat more? (yes or no)\n").lower()
        if response == 'no':
            print("Bye!")

chatbot()

