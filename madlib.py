## string concatenation (like how to put some strings together)
## suppose  we want to create a string that says "Subscribe to ___"
#youtube = "Kylie Ying" # some string variable
#
## a few ways to do this
#print("subscribe to" + youtube)
#print("subscribe to {}".format(youtube))
#print(f"subscribe to {youtube}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)