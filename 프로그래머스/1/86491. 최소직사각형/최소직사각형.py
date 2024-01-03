def solution(sizes):
    
    max_width = min_height = 0
    for size in sizes:
        w, h = size
        max_width = max(w, h, max_width)
        min_height = max(min(w, h), min_height)
        
    return max_width* min_height
     