#can be printed anywhere
print("I can print anywhere I like")

class FirstLab: #creating a class
    def __init__(self): #method for initializing attributes of a class
                        #def is used to find defined functions (eg. __init__
        print("hi, this is my first python class") #what the class does (eg, method here is print)

fl = FirstLab() #create instance of class BELOW class creation

class SqNum:
    def __init__(self):
        x = 5
        y = 2
        z = x ** y
        print(z)

sn = SqNum()