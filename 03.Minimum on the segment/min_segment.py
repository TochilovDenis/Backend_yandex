def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    deq = [0] * n
    head = 0
    tail = 0

    for i in range(n):
        if head < tail and deq[head] <= i - k:
            head += 1

        while head < tail and arr[deq[tail - 1]] >= arr[i]:
            tail -= 1

        deq[tail] = i
        tail += 1

        if i >= k - 1:
            print(arr[deq[head]])

if __name__ == "__main__":
    main()