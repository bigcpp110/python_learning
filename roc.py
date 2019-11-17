import numpy as np
import pandas as pd

pd.set_option("display.max_columns",None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth',100)

class Roc():

    def ax(self,array,n):
        ret=array[-1]-array[-n]
        return ret
    def roc(self,array,n):
        ret=self.ax(array,n)/array[-1]
        return ret

    def func(self,x,y):
        if x*y<0 and x>0:
            return -1
        elif x*y<0 and x<0:
            return 1
        else:
            return 0


    def up_down(self,data):
        data=data[["roc"]]
        shift_data=data.shift(periods=1)
        data=pd.merge(data,shift_data,left_index=True,right_index=True)
        data.columns=["roc","roc_shift"]
        data.dropna(inplace=True)
        data["roc_signal"]=data.apply(lambda x:self.func(x["roc"],x["roc_shift"]),axis=1)
        return data[["roc_signal"]]

    def roc_curve(self,data,n):
        shift_data=data.shift(periods=n)
        diff_data=data.diff(periods=n)
        data=pd.merge(data,diff_data,left_index=True,right_index=True)
        data = pd.merge(data, shift_data, left_index=True, right_index=True)
        data.dropna(inplace=True)
        data.columns=["indicvalue","indicvalue_diff","indicvalue_shift"]
        data["roc"]=data["indicvalue_diff"]/data["indicvalue_shift"]
        data=self.up_down(data)
        return data


if __name__=="__main__":
    df = pd.DataFrame({'a': np.random.randint(1, 100, 100)})
    r=Roc()
    data=r.roc_curve(df,3)
    print(data)