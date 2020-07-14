print("Welcome to ramba game ")
number = 7
essaies = 4
a = 0
while(a<=essaies):
        value = (input("insert a number: "))
        while not(value.isdigit()):
            value = (input("insert a right number: "))
        if value == str(number):
            print("You have won")
            exit()
        a += 1
print("You have lost and the mytery number was 7")