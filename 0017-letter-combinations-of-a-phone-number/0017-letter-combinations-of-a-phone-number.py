class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.number = {'2' :['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        self.result =[]
        self.po=[]
        self.n = len(digits)
        def solver(level):
            if level == self.n:
                self.result.append("".join(self.po))
                return
            for i in self.number[digits[level]]:
                self.po.append(i)
                solver(level+1)
                self.po.pop() 
        solver(0)
        return self.result
