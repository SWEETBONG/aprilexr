import random as rd

lotto_list = list(range(1,46))
rd.shuffle(lotto_list)
lotto_list = lotto_list[:6]
lotto_list.sort()

print('this week :',lotto_list)

