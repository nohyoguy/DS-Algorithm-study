# 배열 원소의 최댓값을 구해서 출력하기(원솟갑을 난수로 생성)

import random
from typing import Any, Sequence


def max_of(a: Sequence) -> Any:
    '''시퀀스형 a 원소의 최댓값을 반환'''
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


print('난수의 최댓값을 구합니다.')
num = int(input('난수의 개수를 입력하세요.: '))
lo = int(input('난수의 최솟값을 입력하세요.: '))
hi = int(input('난수의 쵀댓값을 입력하세요.: '))
x = [None]*num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')
