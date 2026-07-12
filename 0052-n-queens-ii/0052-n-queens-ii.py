class Solution:
    def totalNQueens(self, n: int) -> int:
        self.sol = 0
        pl =[]

        def right():
            last = len(pl) - 1
            for i in range(last):
                
                    if pl[i]==pl[last]:
                        return False
 
                    if abs(i-last)==abs(pl[i] - pl[last]):
                        return False
            
            return True



        def solver(level):
            if(level == n):
                self.sol +=1
                return
            
            for i in range(n):
                pl.append(i)
                if right():
                    solver(level+1)
                pl.pop()
        solver(0)      
        return self.sol