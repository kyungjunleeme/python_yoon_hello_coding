

'''
출처: 예제로 배우는 프로그래밍
http://pythonstudy.xyz/python/article/509-%EB%82%9C%EC%88%98-random

난수 (random)
파이썬에서 난수(random number)를 사용하기 위해서는 기본적으로 제공되는 random 모듈을 사용한다. random 모듈에서 자주 사용되는 함수는 다음과 같다.

randint(최소, 최대) : 입력 파라미터인 최소부터 최대까지 중 임의의 정수를 리턴한다
random() : 0 부터 1 사이의 부동소수점(float) 숫자를 리턴한다
uniform(최소, 최대) : 입력 파라미터인 최소부터 최대까지 중 임의의 부동소수점(float) 숫자를 리턴한다
randrange(시작,끝[,간격]) : 입력 파라미터인 시작부터 끝값까지 (지정된 간격으로 나열된) 숫자 중 임의의 정수를 리턴한다


from random import *
 
i = randint(1, 100)  # 1부터 100 사이의 임의의 정수
print(i)
 
f = random()   # 0부터 1 사이의 임의의 float
print(f)
 
f = uniform(1.0, 36.5)   # 1부터 36.5 사이의 임의의 float
print(f)
 
i = randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
print(i)
 
i = randrange(10)  # 0부터 9 사이의 임의의 정수
print(i)

아래는 난수를 사용한 간단한 예제로서 난수를 생성한 후 어떤 숫자인지 맞추는 프로그램이다. 
즉, 사용자가 입력한 숫자가 난수보다 큰지 작은지를 알려주고 계속 추측해서 난수값을 맞추게하는 예제이다.
'''

from random import randint

n = randint(1, 10)

while True:
    ans = input("Guess my number (Q to exit): ")
    if ans.upper() == "Q":
        break
    ians = int(ans)
    if (n == ians):
        print("Correct!")
        break
    elif (n > ians):
        print("Choose higher number")
    else:
        print("Choose lower number")
    '''
샘플링 (sample)
random 모듈에서 또 한가지 유용한 기능은 리스트, set, 튜플 등과 같은 컬렉션으로부터 일부를 샘플링해서 뽑아내는 기능이다. 
random 모듈에서 sample(컬렉션, 샘플수) 함수는 지정된 컬렉션으로부터 샘플수만큼 랜덤 추출을 하는 함수이고, 
이보다 좀 더 복잡한 choices() 함수는 샘플링에 가중치를 주어 추출하는 기능을 가지고 있다. 
아래 예제는 (1) 숫자 리스트로부터 3개를 랜덤하게 샘플링하고 (2) 튜플에서 2개의 문자열을 샘플링하는 예이다.

import random
 
# (1) 숫자리스트 샘플링
numlist = [1,2,3,4,5,6,7,8,9]
s = random.sample(numlist, 3)
print(s)  # [1, 2, 8]
 
# (2) 튜플 샘플링
frutes = ('사과', '귤', '포도', '배')
s = random.sample(frutes, 2)
print(s)  # ['배', '사과']
'''