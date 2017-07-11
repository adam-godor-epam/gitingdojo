def introduce():
    print("Hello, my name is Gittie! Nice to meet you!")
    print("I have a good joke for you!")


def add(a, b):
    return a+b


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
