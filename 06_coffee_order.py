print()
print("*** Coffee Order Demo ***")

keep_going = ""
while keep_going == "":

    want_coffee = input("Do you want Coffee? ")
    if want_coffee != "yes":
        print("Wrong answer, you always want coffee")
        continue

    else:
        print("Good choice")
        break

print()
print("End of program")
print()    