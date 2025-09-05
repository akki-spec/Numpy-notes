#np.isnan() it only shows that value is missing there,uded to detect unaware values or missing values
import numpy as np

arr = np.array([1,2,np.nan ,3,4, np.nan])
print(np.isnan(arr))
"""
we cannot directly compare this isnan value like
if(np.nan = np.nan)
"""
