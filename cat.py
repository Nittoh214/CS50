#looping
#while loop- one way to express a loop
#start counting from 0
#for loop | list

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n



def meow(n):
    for _ in range(n):
        print("meow")


main()





#while True:
#    n = int(input("What's n?"))
#    if n > 0:
#        break #break out of the most recent loop

#for _ in range(n):
#    print("meow")





#print("meow\n" * 3, end="") #\n starts new line, end removes blank line



#for _ in range(3):            #[1, 2, 3] use [] for lists
#    print("meow")

    


#i = 0
#while i < 3:
#    print("meow")
#    i += 1

#--- infinite loop
#i = 3
#while i != 0:
#    print("meow")

#--- use loop instead of repetition
#print("meow")
#print("meow")
#print("meow")