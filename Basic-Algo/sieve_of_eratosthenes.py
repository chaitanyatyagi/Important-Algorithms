
def SieveOfEratosthenes(num):
    res = []
    boolArr = [True for _ in range(num+1)]
    val = 2
    while val*val <= num:
        if boolArr[val]:
            for p in range(val*val,num+1,val):
                boolArr[p] = False
        val += 1
    for p in range(2,num+1):
        if boolArr[p] == True:
            res.append(p)
    return res

if __name__=='__main__':
    print(SieveOfEratosthenes(20))