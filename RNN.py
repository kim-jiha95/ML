import response
import numpy as np


def rnn(inputs, output_size, bias = [], [], []):
    input_size = len(inputs[0])
    # TODO: 0의 값을 갖는 (output_size,) 모양의 state 벡터를 만들어 봅니다.
    state = np.zeros((output_size,))
    # TODO: 1의 값을 갖는 (output_size, input_size) 모양의 w 벡터를 만들어 봅니다.
    w = np.ones((output_size, input_size))
    # TODO: 1의 값을 갖는 (output_size, output_size) 모양의 u벡터를 만들어 봅니다.
    u = np.ones((output_sizem output_size))
    # TODO: 임의의 값을 갖는 (output_size,) 모양의 b벡터를 만들어 봅니다.
    b = np.random.random((output_size,))
    
    # TODO: bias 가 False 이면 b를 (output_size,) 모양의 영벡터를 만들어 줍니다.
    if not bias:
        b = np.zeros((output_size,))
        
    outputs = []
    
    for _input in inputs:
        # TODO: (Numpy 사용) w와 _input을 내적하고, u 와 state를 내적한 후 b를 더한 다음 하이퍼볼릭 탄젠트 함수를 적용합니다.
        _output = np.tahn(np.dot(u, state) + np.dot(w, _input) + b)
        outputs.append(_output)
        state=_output
        
    return np.stack(outputs, axis=0) 


## TODO: 입력과 출력을 바꾸어 가며 RNN의 원리를 파악해 봅니다.

def main():
    print("-----------------CASE 1-----------------")
    _input = [[0], [0], [0], [0], [0]]
    # 입력이 모두 0이고 출력 벡터의 크기가 1일 때 값의 추세가 어떠한 지 확인해 봅니다.
    print(rnn(_input, output_size=1))
    # Bias 가 있으면 값이 어떻게 변화하는지 알아봅시다.
    print(rnn(_input, output_size=1, bias = True))
    
    
    print("-----------------CASE 2-----------------")
    _input = [[1], [1], [1], [1], [1]]
    # 입력이 모두 1이고 출력 벡터의 크기가 1일 때 값의 추세가 어떠한 지 확인해 봅니다.
    print(rnn(_input, output_size=1))
    # Bias 가 있으면 값이 어떻게 변화하는지 알아봅시다.
    print(rnn(_input, output_size=1, bias = True))
    
    
    print("-----------------CASE 3-----------------")
    _input = [[1], [2], [3], [4], [5]]
    
    # 입력값이 증가하고 출력 벡터의 크기가 2일 때 값의 추세가 어떠한 지 확인해 봅니다.
    print(rnn(_input, output_size=2))
    # Bias 가 있으면 값이 어떻게 변화하는 지 알아봅시다.
    print(rnn(_input, output_size=2, bias = True))

    print("-----------------CASE 4-----------------")
    _input = [[1], [1], [3], [4], [4]]
    # 입력값이 위와 같을 때 값의 추세가 어떠한 지 확인해 봅니다.
    print(rnn(_input, output_size=2))
    # Bias 가 있으면 값이 어떻게 변화하는 지 알아봅시다.
    print(rnn(_input, output_size=2, bias = True))


if __name__ == '__main__':
    response.run()
