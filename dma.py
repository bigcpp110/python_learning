import pandas as pd
import numpy as np

pd.set_option("display.max_columns",None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth',100)

class Dma():
    def roll(self,data,n):
        return data.rolling(n).mean()

    def func(self,x,y):
        if x*y<0 and y>0:
            return -1
        elif x*y<0 and y<0:
            return 1
        else:
            return 0

    def up_down(self,data):
        data=data[["DMA-AMA"]]
        shift_data = data.shift(periods=1)
        print(shift_data)
        data=pd.merge(data,shift_data,left_index=True,right_index=True)
        data.columns=["DMA-AMA","DMA-AMA_shift_1"]
        data["signal"]=data.apply(lambda x:self.func(x["DMA-AMA"],x["DMA-AMA_shift_1"]),axis=1)
        print(data)



    def dma(self,data):
        roll_10=self.roll(data, 10)
        roll_5=self.roll(data,5)
        data=pd.concat([data,roll_5,roll_10],axis=1)
        data.columns=["indicvalue","roll_5","roll_10"]
        data["DMA"]=data["roll_5"]-data["roll_10"]
        data["AMA"]=self.roll(data[["DMA"]],5)
        data.dropna(inplace=True)
        data["DMA-AMA"]=data["DMA"]-data["AMA"]#差值由正转负为-1
        self.up_down(data)

if __name__=="__main__":
    df = pd.DataFrame({'a': np.random.randint(1,100, 100)})
    r=Dma()
    r.dma(df)