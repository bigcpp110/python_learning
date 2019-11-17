import numpy as np
import pandas as pd

class Momentum():
    def mtm(self,data,n):
        mtm=np.diff(data,n,axis=-1)
        return mtm

    def avg(self,data,n):
        return data.rolling(n).mean()

    def mtmma(self,data,n,m):
        mtm=self.mtm(data,n)
        mtmma=mtm.rolling(m).mean()
        return mtmma
