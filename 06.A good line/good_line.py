def main():
    n = int(input())
    counts = [int(input()) for _ in range(n)]
    
    good = 0
    for i in range(n - 1):
        good += min(counts[i], counts[i + 1])
    
    print(good)

if __name__ == "__main__":
    main()