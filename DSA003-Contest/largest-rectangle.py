def largestRectangle(h):
    stack = []
    max_area = 0
    index = 0
    
    h.append(0)
    
    while index < len(h):
        if not stack or h[stack[-1]] <= h[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            
            if not stack:
                width = index 
            else:
                width = index - stack[-1] - 1
            area = h[top]* width 
            max_area = max(max_area, area)
    return max_area
    
