import pandas as pd

from Ordinal_encoder import ordinal_encoder
data = pd.read_csv('trial.csv')
encoder = ordinal_encoder()
encoder.fit_transform(data)
print(data)

from One_hot_encoder import one_hot_encoder
data = pd.read_csv('trial.csv')
encoder = one_hot_encoder()
encoder.fit_transform(data)
print(data)