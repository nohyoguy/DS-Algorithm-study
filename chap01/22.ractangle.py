# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나영하기

area = int(input('직사각형의 넓이를 입력하세요. '))

for i in range(1, int(area ** (0.5)) + 1):
    if not area % i:
        print(f'{i} x {int(area/i)}')
