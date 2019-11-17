import numpy as np
import pandas as pd

class Aroon():
    def aroonup(self,n,array):
        max_pos=np.argmax(array,axis=0)
        num=n-max_pos-1
        up=(n-num)/n*100
        if up==100:
            return 1
        else:
            return 0


    def aroondown(self,n,array):
        min_pos=np.argmin(array,axis=0)
        num=n-min_pos-1
        down=(n-num)/n*100
        if down == 100:
            return -1
        else:
            return 0

    def aroon(self,data,n):
        for i in range(n,data.shape[0]):
            ret=data["a"][i-n:i]
            data.loc[i,"aroonup"]=self.aroonup(n,ret)
            data.loc[i,"aroondown"]=self.aroondown(n,ret)
        return data



if __name__ == "__main__":
    df = pd.DataFrame({'a': np.random.randint(1, 100, 10)})
    a=Aroon()
    a.aroon(df,4)


