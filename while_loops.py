#2 examples of loops in here

#Using for to print everything in the list
#names = ["Inge", "Alan", "Erica"]
#for name in names:
#    print("Hello " + name)


#loop for a fixed number of times using while
#counter = 0
#while counter < 5:
#    print("Hello " + str(counter))
#    counter = counter + 1

#loop for a fixed number of times using for
#for i in [0, 1, 2, 3, 4]:
#    print("Hello " + str(i))


#counter = 0
#while True:
#    print("Hello " + str(counter))
#    counter = counter + 1
#
#    if counter >= 5:
#        break

print("Hello human!")

while True:
    user_input = raw_input("> ")
    if user_input == "quit":
        print("Goodbye human!")
        break
    else:
        print(user_input)

