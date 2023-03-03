import pandas as pd
import numpy as np 

df = pd.read_csv('data.csv')
show = df['Year']

def linear(arr, val, size):
    for i in range(0, size-1):
        if arr[i] == val:
            return i

    return 'nope'

arr = np.asarray(show)
val = 2022
size = len(arr)
result = linear(arr, val, size)
print(result)

#tera asmaan, ye jaadu ki nagree baba song