def main():
    data = input().strip().split()
    numbers = list(map(int, data))
    
    tree = []    
    key_to_index = {}    
    root_index = -1
    height_result = 0
    
    for num in numbers:
        if num == 0:
            break
            
        if num in key_to_index:
            continue
      
        new_index = len(tree)
        tree.append([num, -1, -1])  # [key, left, right]
        key_to_index[num] = new_index
        
        if root_index == -1:
            root_index = new_index
            height_result = 1
        else:
            current = root_index
            depth = 1
            
            while True:
                depth += 1
                if num < tree[current][0]:
                    if tree[current][1] == -1:
                        tree[current][1] = new_index
                        break
                    else:
                        current = tree[current][1]
                else:
                    if tree[current][2] == -1:
                        tree[current][2] = new_index
                        break
                    else:
                        current = tree[current][2]
            
            height_result = max(height_result, depth)
    
    print(height_result)


if __name__ == "__main__":
    main()