import sys


def main():
    n = int(input())
    synonyms = {}

    for _ in range(n):
        word1, word2 = input().split()
        synonyms[word1] = word2
        synonyms[word2] = word1

    word = input()
    print(synonyms[word])


if __name__ == '__main__':
    main()
