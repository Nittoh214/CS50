# + - * / (%=modular arithmitic, calculate remainder)
#Pythonic - the way you do things in Python

def main():
    x = int(input("What's x? "))
    if is_even(x): #returns True or False 
        print("Even")
    else:
        print("Odd")

#defining function for is_even
def is_even(n):
    return n % 2 == 0 #n % 2 == 0 Boolean expression | add () for order of operations


main()
#-------------        
#def main():
#    x = int(input("What's x? "))
#    if is_even(x): #returns True or False 
#        print("Even")
#    else:
#        print("Odd")python p
#defining function for is_even
#def is_even(n):
#    if n % 2 == 0: #returning boolean values, can only be True or False. 
#        return True
#    else:
#        return False


#main()

#-----------
#x = int(input("What's x? "))

#if x % 2 == 0:
#   print("Even")
#else:
#    print("Odd")