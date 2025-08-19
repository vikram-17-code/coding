def longestCommonPrefix(self, strs: List[str]) -> str:
  if strs==None:
    return ""
  for i in range(len(strs[0])):
    letter=strs[0][i]
    for j in strs[1:]:
      if i>=len(j) or letter!=j[i]:
        return strs[0][:i]
  return strs[0]
