def max_product_pair():
    arr = list(map(int, input().split()))
    
    max1 = max2 = -float('inf')
    min1 = min2 = float('inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    product_with_max = max1 * max2
    product_with_min = min1 * min2
    
    if product_with_max > product_with_min:
        return sorted([max1, max2])
    else:
        return sorted([min1, min2])


def main():
    result = max_product_pair()
    print(result[0], result[1])


if __name__ == "__main__":
    main()
