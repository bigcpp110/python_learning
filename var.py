import tushare as ts
import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

class Var():
    def quantile(self,timeseries,n):
        ptiles_vers = timeseries.quantile(n)
        return ptiles_vers


    def signal(self,timeseries):
        tmp=timeseries[:-1]
        per_5=self.quantile(tmp,0.05)
        per_95=self.quantile(tmp,0.95)
        var=timeseries[-1]
        if var>per_95:
            return -1
        elif var<per_5:
            return 1
        else:
            return 0




if __name__=="__main__":
    pro = ts.pro_api('750c96db6ca4a0d0155228106aa915891040b73e82d6c02a05b58744')
    ticker_data = pro.daily(ts_code='600377.SH')
    print('数据量：', len(ticker_data))
    ticker_data['trade_date'] = pd.to_datetime(ticker_data['trade_date'], format='%Y%m%d')
    ticker_data.set_index('trade_date', inplace=True)
    returns = ticker_data["close"].pct_change().dropna()

    plt.figure(figsize=(15, 5))
    plt.title("股票代码:600377 - 宁沪高速", weight='bold')
    ticker_data['close'].plot()
    plt.show()
    plt.figure(figsize=(15, 5))
    ticker_data["close"].pct_change().plot()
    plt.title("股票代码:600377 - 宁沪高速", weight='bold')
    plt.show()
    VaR_90 = returns.quantile(0.1)
    VaR_95 = returns.quantile(0.05)
    VaR_99 = returns.quantile(0.01)
    VaR_9999 = returns.quantile(0.001)

    h_VaR = {'90%': VaR_90, '95%': VaR_95, '99%': VaR_99, '99.99%': VaR_9999}
    print(pd.DataFrame.from_dict(h_VaR, orient='index', columns=['在险损失（VaR）']))
