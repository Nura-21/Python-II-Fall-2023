import numpy as np
import pandas as pd
import csv


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


df = pd.read_csv('input_6.csv', header=None, names=[
                 'x', 'thetaZero', 'thetaOne'])
m = df.iloc[0, 0]
df['prediction'] = sigmoid(df['x'] * df['thetaOne'] + df['thetaZero'])

df[['prediction']].round(2).to_csv(
    'output_6.csv', index=False, header=False, quoting='')
