#Print 1 To N Without Loop
#geeksforgeeks
def printNos(self,N):
    if N==0:
        return
    self.printNos(N-1)
    print(N,end=" ")

