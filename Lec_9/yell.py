def main():
    yell("Hello", "World", "!!!")


def yell(*words):
    #  print(*words)  # prints the words separated by space
    #  uppercased = list()
    #  for word in words :
    #      uppercased.append(word.upper())
    # uppercased = map(str.upper,words)
    uppercased=[word.upper() for word in words]
    print(*uppercased)    




if __name__ == "__main__":
    main()