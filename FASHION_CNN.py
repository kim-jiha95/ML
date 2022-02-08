import response
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

max_features = 6000
max_len =  130
embedding_size = 128

(input_train, label_train), (input_test, label_test) = imdb.load_data(num_words=max_features)
input_train = pad_sequences(input_train, maxlen=max_len)
input_test = pad_sequences(input_test, maxlen=max_len)

def expand_dim(_input):
    # (3,2) -> (3,2,1) 과 같이 뒤쪽에 차원을 늘립니다.
    return tf.expand_dims(_input, -1)

def main():
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(max_features, embedding_size),
        # TODO: GRU층을 추가시켜 봅니다.
        tf.keras.layers.GRU(32),
        tf.keras.layers.Dense(1, activation = tf.nn.sigmoid),
    ])
    
    # TODO: 모델 학습에 필요한 파라미터들을 설정하고, 학습을 진행합니다.(파라미터들을 조정해가며 성능을 최대한 향상시켜 봅니다.)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(input_train, label_train, validation_split=2, batch_size=100, verbose=1)
if __name__ == '__main__':
    response.run()
