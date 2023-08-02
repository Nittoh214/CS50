while True:  #while creates a loop to reprompt
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}") 

#NameError 
#---
#File "C:\Users\Lenny\OneDrive\Desktop\CS50\CS50P\number.py", line 6, in <module>
#    print(f"x is {x}")
                  
#NameError: name 'x' is not defined
# order of operations problem: input function is working fine. Value Error happened first 
# Use else

#---

#try:
#    x = int(input("What's x? "))
#    print(f"x is {x}") will not raise a value error
#except ValueError: 
#    print("x is not an integer")

#Using non int like 'cat': ValueError: invalid literal for int() with base 10: ' cat' base10 refers to decimal system, literal is something thats been typed in for int
#need f string in line 3 to subsitute what x is in the curly braces
#program defensively to handle as many errors as possible
#Line 4 + 5 to handle Value Error
#Don't catch all errors, handle them all explicitly