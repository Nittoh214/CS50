#change :) and :( to 🙂 and 🙁
def main():
    a = input("use :) or :( in your sentence: ")
    b = a.replace(":)", "🙂").replace(":(", "🙁")
    print(b)

main()