def main():
    n, m = map(int, input().split())
    events = []
    
    for _ in range(n):
        a, b = map(int, input().split())
      
        left = min(a, b)
        right = max(a, b)
        
        events.append((left, 0, 1))
        events.append((right, 2, -1))
    
    points = list(map(int, input().split()))
    
    for i, x in enumerate(points):
        events.append((x, 1, i))
  
    events.sort(key=lambda event: (event[0], event[1]))
    
    result = [0] * m
    current_segments = 0
    
    for event in events:
        coord, event_type, value = event
        
        if event_type == 0:
            current_segments += 1
        elif event_type == 1:
            point_idx = value
            result[point_idx] = current_segments
        else:
            current_segments += value

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()