import numpy as np
import pandas as pd
# create a sample dataset
data=pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df=pd.DataFrame(data=data, index=['row1', 'row2', 'row3'])
print(df)