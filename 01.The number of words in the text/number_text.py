import sys


def main():
    words = set()
    for line in sys.stdin:
        if line.strip() == "":
            break
        for word in line.split():
            words.add(word)
    print(len(words))


if __name__ == "__main__":
    main()
