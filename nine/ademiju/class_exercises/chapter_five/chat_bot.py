import datetime
import random
import time


def chatbot():
    response = "yes"
    while response == "yes":

        users_question = input("What Questions would you like to ask me ?\n").split()
    

        dictionary = {
            "time": ["The time is " + str(datetime.datetime.now().time()), 
             "The time is " + str(datetime.datetime.now().time())+"\nYou can get a watch at your nearest Watch Store"],
            "name": ["My name is Siri", "My name is Sam", "My name is Alexa", "My name is Cortana","My name is Judith"],
            "love": ["Ja, ich liebe dich!", "Nein, ich liebe dich nicht", "Scheiße", "Love is wicked"],
            "eat": ["Yeah, baby!", "Nah 😢"],
            "single": ["I'm single as feck", "It's like I'm in one relationship like that joor"],
            "programs": ["I write python sometimes", "I'm learning java", "I can write golang partially",
                         "C# is unnecessarily hard but i can still get a hang of it"],
            "country": ["I've been to Canada", "Maybe the UK", "Lovely Kenya", "Extremely beautiful Latvia"],
            "age": ["I am "+str(num for num in range(1, 100))+" old","My age is technology-dependent","My age is beyound my comprehension"],
            "play": ["It depends tho", "Biko leave me alone joor", "Make I daze you?!"],
            "sleep": ["I rarely sleep", "I can't shutdown, I can only have a 10sec power nap daily"]
                
        }

        reply = []

        users_question = [x.lower() for x in users_question]

        if  users_question == ["exit"]:
            print("Exiting...")
            break

        for key in users_question:
            if key in dictionary.keys():
                reply.append(random.choice(dictionary[key]))
                if reply:
                    print(random.choice(reply))
                else:
                    print("I don't have an answer for you, Ask another question")

        time.sleep(1)
        print()

        response = input("Do you want to chat more? (yes or no)\n").lower()
        if response == 'no':
          print("Bye!")

chatbot()
