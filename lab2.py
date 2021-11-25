class StringTesting:
    def __init__(self):
        sentence = "hello BEN! How are you?"
        #some python functions
        print(sentence.find("e"))
        print(sentence.count("o"))
        print(sentence.lower())
        print(sentence.capitalize())

st = StringTesting()


class MathsTesting:
    def __init__(self):
        x = 42
        ans = ((((x+2)*3)-6)/3) #accurate brackets
        print(ans)

mt = MathsTesting()


class MathsTestingVariables:
    def __init__(self):
        #declaring variables
        my_var1 = 7.0
        my_var2 = 5
        print(my_var1 % my_var2) #remainder

mtv = MathsTestingVariables()


