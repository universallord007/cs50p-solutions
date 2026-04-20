def main():
    n = int(input("Whats n ?"))
    for i in sheep(n):
        print(i)


def sheep(s):
    # flock = []
    # for i in range(s):
    #     flock.append("🐑"*i)
    # return flock
    for i in range(s):
        yield "🐑" * i


if __name__ == "__main__":
    main()