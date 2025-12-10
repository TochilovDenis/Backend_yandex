def max_beauty(k, s):
    n = len(s)
    if n == 0:
        return 0
    
    max_len = 1
    
    for target in range(26):
        target_char = chr(ord('a') + target)
        left = 0
        diff_count = 0
        
        for right in range(n):
            if s[right] != target_char:
                diff_count += 1
            
            while diff_count > k:
                if s[left] != target_char:
                    diff_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
    
    return max_len

if __name__ == "__main__":
    k = int(input())
    s = input().strip()
    print(max_beauty(k, s))