f = open("scores.txt", "w")

while True:
    participant = raw_input("Participant Name > ")

    if participant == "quit":
        print("Quitting...")
        break    

    score = raw_input("Score for " + participant + "> ")
    f.write(participant + "," + score + "\n")

f.close
