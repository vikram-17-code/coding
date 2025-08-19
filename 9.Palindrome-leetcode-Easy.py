def isPalindrome(self, x: int) -> bool:
  dummy=str(x)
    if dummy==dummy[::-1]:
      return True
    else:
      return False
