def main():
        convert()


def convert():
        userInput = input("")
        if ":)" in userInput and ":(" in userInput:
                print(userInput.replace(":)", "🙂").replace(":(", "🙁"))
        elif ":)" in userInput:
                print(userInput.replace(":)", "🙂"))
        elif ":(" in userInput:
                print(userInput.replace(":(", "🙁"))
        else:
                print(userInput)


main()
