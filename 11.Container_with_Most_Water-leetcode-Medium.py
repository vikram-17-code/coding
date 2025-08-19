def maxArea(self, height: List[int]) -> int:
        
  left, right = 0, len(height) - 1
  maximum = 0

  while left < right:
    lower = min(height[left], height[right])
    cap = lower * (right - left)
    maximum = max(maximum, cap)

    
    if height[left] < height[right]:
      left += 1
    else:
      right -= 1

  return maximum
