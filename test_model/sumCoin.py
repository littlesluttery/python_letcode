import math
def sum_Coin(N):
    sum_coin = 0
    if N<2:
        return 0,N
    if N==2:
        return 1,0


    for i in range(1,math.ceil(math.sqrt(N))+1):
        print(math.ceil(int(math.sqrt(N)))+1)
        sum_coin += i*i+1
        print(sum_coin)
        if sum_coin>N:
            break
    print(i-1,N-(sum_coin-(i*i+1)))
'''
while True:
    try:
        n = int(input())
        num,numof = sum_Coin(n)
        print(num,numof)
    except:
        break
'''

sum_Coin(3)