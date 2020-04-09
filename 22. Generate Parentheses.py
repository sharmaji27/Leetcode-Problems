class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
         
        return self.rec(n,'',0,0,[])

    def rec(self,n,s,opened,closed,result):
        
        if opened==n and closed!=n:
            result.append((s + ')'*(n-closed)))

        elif opened==closed and opened<=n:
            self.rec(n,s+'(',opened+1,closed,result)

        elif opened > closed and opened<=n:
            self.rec(n,s+')',opened,closed+1,result)
            if opened<n:
                self.rec(n,s+'(',opened+1,closed,result)

        return result