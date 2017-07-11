def introduce():
    print("Hello, I'm Gittie!")


def add(a, b):
    pass


def joke():
    print("How do trees access the internet?")
    answer = "They log on."
    for i in range(5):
        if input("Answer({} tries left): ".format()) == answer:
            print("You have the correct answer.")
            return
    print("You ran out from tries. The answer was: {}".format(answer))
        

def shout():
    pass
