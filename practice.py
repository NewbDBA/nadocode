
# 연산자

print(1 == 3) # 앞 뒤가 같음
print(1 != 3) # 앞 뒤가 같지 않음
print(not(1 == 3)) # 위에 거랑 비슷

print((3 > 0) and (3 < 5)) # 2개 다 만족해야함
print((3 > 0) & (3 < 5)) # 위에거랑 같음

print((3 < 0) or (3 > 5)) # 둘 중에 하나만 되도 okay
print((3 < 0) | (3 > 5)) # 위에 거랑 같은데, 백스페이스 밑에꺼 shift +x

# 연산자

# 간단수식
number = 2+4*3
number = number + 2 #number라는 변수에 2 더하고 싶댑니다.#
print(number)

# 아래거는 위에꺼랑 똑같음
number += 2 # *= 숫자 // -= 숫자 // /=숫자 다됨
print(number)


asshole = 43+5+3*8
asshole %= 5
print(asshole)
# 간단수식

# 숫자 처리 함수 
print(abs(-5)) # ABS=absolute (절대값)
print(pow(5, 2)) # == 5 ** 2
print(max(5,10,12)) # min 도 있음
print(round(3.2)) # 반올림

from math import * # math 라는 모듈에서 모든 값(*)을 불러온다는 말
print(floor(5.99)) # math 모둘 호출 후에 버림(floor) 가능
print(ceil(1.11)) # 올림
print(sqrt(4)) # 제곱근
