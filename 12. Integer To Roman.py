class Solution:
    def intToRoman(self, num: int) -> str:
        out=''
        I = ['','I','II','III','IV','V','VI','VII','VIII','IX','X']
        X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','C']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','M']
        M = ['','M','MM','MMM']
        out = M[num//1000]+C[(num%1000)//100]+X[(num%100)//10]+I[num%10]       
        return out.strip()