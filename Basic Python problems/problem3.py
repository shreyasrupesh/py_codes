#printing alternative numbers in a array
def printAl (arr,n):
    for i in range(0,n,2):
        print(arr[i],end=" ")

printAl(arr=[1,2,3,4],n=4)