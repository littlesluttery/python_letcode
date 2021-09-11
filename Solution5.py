def f(n):
    hash_number = [1,2,3]
    or_n = n
    new_n = []
    while n > 0:
        middle_r = n % 10
        #print(middle_r)
        if middle_r in hash_number:
            new_n.append(middle_r)
        else:
            #n = int(str(n/10) + '3')
            new_n.append(3)

        n = n // 10
    new_n = new_n[::-1]
    new_n = int(''.join(list(map(str,new_n))))
    if new_n > or_n:
        new_n = new_n % (10 ** (len(str(new_n))-1))
    return new_n


new_n = f(100)
print(new_n)

# 创建一个hash表，存储123
# 依次拿到n中每一个数，查找是不是在表中，如果全都在则满足，
# 如果不在，则先将不满足部位取为3，依次在找


