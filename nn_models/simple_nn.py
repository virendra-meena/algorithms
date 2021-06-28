import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

model = tf.keras.models.Sequential(
    [
        Input(shape=(512,), name='input_layer', dtype='float'),
        Dense(1, activation='linear')
    ]
)


inp = Input(shape=(512, ), name='input_layer', batch_size=64)
x = Dense(32, activation='linear')(inp)
x = Dense(1, activation='linear')(x)

layered_model = tf.keras.Model(inputs=inp, outputs=x)

print(layered_model.summary())
