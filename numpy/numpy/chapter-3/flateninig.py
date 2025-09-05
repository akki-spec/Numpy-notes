"""flatening: multi dimenional araay into 1d array convertion,there are two types
1).raval() [in this it shows view means modification is done in original array]
2).flatten() [in this it returns copy so it mean original array not going to change]"""
import numpy as np
arr = np.array([[10,20,30],[40,50,60]])
print(arr.ravel())
print(arr.flatten())
