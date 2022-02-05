# 실습에 사용할 변수를 선언합니다.
args = [1, 2, 3, 4, 5]

# 1. x를 인자로 받아 x의 제곱 x*x를 리턴하는 lambda 함수를 f에 저장하세요.
f = lambda x: x*x

# 2. args의 모든 요소를 f에 대입하여 결과를 얻은 후 ret1에 저장하세요.
ret1 = map(f, args)

# 3. ret1에 저장된 객체를 리스트 형태로 변환하세요.
ret2 = list(ret1)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret2)
