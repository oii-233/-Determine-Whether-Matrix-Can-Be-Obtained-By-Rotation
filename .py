class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        adi=[]
        result=False
        row=len(mat)
        col=len(mat[0])
        for i in range(col):
                adi.append([0]*row)

        def dge():
            nonlocal result
            match=True
            for i in range(row):
                for j in range(col):
                    adi[j][row-1-i]=mat[i][j]
            for i in range(row):
                for j in range(col):
                    if adi[i][j]!=target[i][j]:
                        match=False
                        break
                if not match:
                    break
            if match:
                result=True

        for h in range(4):
            dge()
            if result==True:
                break
            mat = [row[:] for row in adi]

        return result
        

        
