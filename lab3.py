class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        # 1. print only first and last of the sentence:
        print("First:", message[0], "Last:", message[-1])

        # 2. use slice notation:
        print(message[2:4])

        # 3. escaping a character, such as an apostrophe or & sign:
        print(message,"\'s dog")

        # 4. find all a's in the input word and count how many there are:
        message.find("a")
        print(message.count("a"))

        # 5. replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        print(message.replace("a", "-"))

    # to run the tasks associated with this file, you must first
    # uncomment line number 75 and comment line 74
    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # 6. hand the input string to a list and print it out:
        message_list = message.split()
        print(message_list)

        # 7. append a new element to the list and print:
        message_list.append("banana")
        print(message_list)

        # 8. remove from the list in 3 ways:
        message_list.pop(1)
        print(message_list)
        message_list.remove("carl")
        print(message_list)
        #message_list.clear()
        #print(message_list)

        # 9. check if the word cake is in your input list:
        if "cake" in message_list:
            print("Cake is in this list.")
        else:
            print("Cake is not in this list!")

        # 10. reverse the items in the list and print using a function:
        message_list.reverse()
        print(message_list)

        # 11. reverse the list with the slicing trick:
        print(message_list[::-1])

        # 12. print the list 3 times by using multiplication:
        print(message_list*3)


tas = Types_and_Strings() # creates an instance of the object
#tas.play_with_strings() # calls the method play_with_strings()
tas.play_with_lists()
