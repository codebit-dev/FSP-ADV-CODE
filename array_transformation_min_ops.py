def min_operations(n, arr, k):
    base = arr[0] % k
    for x in arr:
        if x % k != base:
            return -1

    arr = [x // k for x in arr]
    arr.sort()
    median = arr[n // 2]

    return sum(abs(x - median) for x in arr)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    print(min_operations(n, arr, k))


if __name__ == "__main__":
    main()
