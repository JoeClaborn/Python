def main():

    user_input = input("Please type something in: ")
    censor = input("Please type a word you'd like to censor: ")

    censored_output = user_input.replace(censor, "***")

    print(f"You typed: {user_input}")
    print(f"The censored version is: {censored_output}")

if __name__ == "__main__":
    main()
