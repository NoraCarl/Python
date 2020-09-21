import numpy as np 
import pandas as pd

if __name__ == "__main__":
    df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],'value': [1, 2, 3, 5]})
    df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],'value': [5, 6, 7, 8]})

    print(df1)
    print(df2)
    print(df1.merge(df2,left_on='lkey', right_on='rkey'))