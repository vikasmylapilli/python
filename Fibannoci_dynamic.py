import time
def fibannoci(n):
    
    if memo[n] != 0:
        return memo[n]
    if n<= 1:
        return 1

    memo[n] =  fibannoci(n-1)+fibannoci(n-2)
    return memo[n]


if __name__== "__main__":
    n = 1000
    memo = {}
    for i in range(n+1):
        memo[i] = 0
    

    start = time.time()
    
    for i in range (n):
        print(fibannoci(i),end=",")
    print()

    stop = time.time()
    print(stop-start)

    




    
