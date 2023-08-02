#allows you to express ideas more compactly
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Lariane":
        print("Ravenclaw")
    case _: #_ for any case not yet defined
        print("Who?")

#------  
#name = input("What's your name? ")

#match name:
#    case "Harry":
#        print("Gryffindor")
#    case "Hermione":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")
#    case "Draco":
#        print("Slytherin")
#    case _: #_ for any case not yet defined
#        print("Who?")

#--------
#name = input("What's your name? ")
    
#if name == "Harry" or name == "Hermione" or name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else: 
#    print("Who?")


#--------  
#name = input("What's your name? ")

#if name == "Harry":
#    print("Gryffindor")
#elif name == "Hermione":
#    print("Gryffindor")
#elif name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else: 
#    print("Who?")
