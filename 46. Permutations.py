class Solution:
    def permute(self,digits):
        result = []
        for p in self.rec(digits):
            result.append(p)
        return result
        
    def rec(self,lst):
        if len(lst)==0:
            return []
        elif len(lst)==1:
            return [lst]
        else:
            l = []
            for i in range(len(lst)):
                x = lst[i]
                xs = lst[:i] + lst[i+1:]
                for p in self.rec(xs):
                    l.append([x]+p)  
            return l