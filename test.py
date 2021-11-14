# class Flight:
#
#     rise_amount = 1.05
#     def __init__(self, first, last, price):
#         self.firstname = first
#         self.lastname = last
#         self.price = price
#
#     def ticket(self):
#         return '{} {} - €{}'.format(self.firstname, self.lastname, self.price)
#
#     def price_rise(self):
#         self.price = int(self.price * Flight.rise_amount)
#         #self.price = int(self.price * self.rise_amount)   // can also be used through the self instance
#
# passenger1 = Flight('Ben', 'Johnson', 200)
#
# print(Flight.ticket(passenger1), "\n")
#
# print(passenger1.price)
# passenger1.price_rise()
# print(passenger1.price)

#///////////////////////////////////////////////////////////////

#code for highest num
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(3,1,2))

#///////////////////////////////////////////////////////////////

#code for min num
# def min_num(num1, num2, num3):
#      if num1 <= num2 and num1 <= num3:
#          return num1
#      elif num2 <= num1 and num2 <= num3:
#          return num2
#      else:
#          return num3
#
# print(min_num(1,2,3))

#///////////////////////////////////////////////////////////////

#basic calculations
# num1 = float(input("Enter num1: "))
# op = input("Select operator (+, -, /, *): ")
# num2 = float(input("Enter num2: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator!")

#///////////////////////////////////////////////////////////////

#guessing game
# secret_word = "banana"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses, you lose!!")
# else:
#     print("You win!!")

#///////////////////////////////////////////////////////////////