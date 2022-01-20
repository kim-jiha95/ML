import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import utils
from tensorflow.keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D
from tensorflow.keras import Model
import tensorflow as tf

from elice_utils import EliceUtils

from utils import drawRNNLoss, calc_in4p, read_seqdata
elice_utils = EliceUtils()

def main():
    # 초기화 : 아래 seed 값은 수정하지 마세요.
    tf.random.set_seed(90)
    np.random.seed(90)
    
    # TODO : 데이터 읽어들이기
    (x_train, t_train), (x_test, t_test) = read_seqdata()
    
    
    # 전체 학습이 진행되기 전 설정값 확인에 사용합니다.
    data_size = 100
    (x_train, t_train), (x_test, t_test) = (x_train[:data_size], t_train[:data_size]), (x_test[:data_size], t_test[:data_size])
    
    
    # TODO : SimpleRNN 신경망 구현
    srnn_100_model = tf.keras.Sequential([
            tf.keras.layers.SimpleRNN(units=30, return_sequences=True, input_shape=[100,2]),
            tf.keras.layers.SimpleRNN(units=30), 
            tf.keras.layers.Dense(1)
            ])
    
    
    # TODO : optimizer, loss 설정합니다.
    srnn_100_model.compile(optimizer='adam', loss='mse') 
    
    
    # TODO : epoch와 verbose 설정
    srnn_100_history = srnn_100_model.fit(x_train, t_train, epochs=100, validation_split=0.2, verbose=2)
    
    
    # 그래프 확인
    drawRNNLoss(srnn_100_history)
    
    
    # 라벨에 있는 값과 예측한 값의 차이가 0.1 이내면 맞은 것으로 처리
    prediction = srnn_100_model.predict(x_test)
    calc_in4p(prediction, 0.1)
    
    return prediction

if __name__ == "__main__":
    main()
