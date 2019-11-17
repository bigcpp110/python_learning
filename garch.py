from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARMA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from arch import arch_model
import warnings
warnings.filterwarnings("ignore")


import tushare as ts

import pandas as pd

import numpy as np


class Garch():
    pass


if __name__=="__main__":


    # sh = ts.get_hist_data('sh').sort_index()
    #
    #
    # sh['re'] = np.log(sh['close'] / sh['close'].shift(1))
    #
    # sh = sh.dropna()
    # am = arch_model(sh['re'])
    #
    # model = am.fit(update_freq=0)
    #
    # ret=model.forecast(horizon=1)
    #
    # print(ret.variance)
    #
    # model.hedgehog_plot()
    # plt.show()

    import datetime as dt
    import sys

    import numpy as np
    import pandas as pd
    import pandas_datareader.data as web

    from arch import arch_model

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2017, 1, 1)
    data = web.get_data_famafrench('F-F_Research_Data_Factors_daily', start=start, end=end)
    mkt_returns = data[0]['Mkt-RF'] + data[0]['RF']
    returns = mkt_returns
    print("returns is %s"%returns)
    print("-------returns-----------")
    print(mkt_returns)
    am = arch_model(returns, vol='Garch', p=1, o=0, q=1, dist='Normal')
    res = am.fit(update_freq=5)
    forecasts = res.forecast()
    # print(forecasts.mean.iloc[-3:])
    # print(forecasts.residual_variance.iloc[-3:])
    # print(forecasts.variance.iloc[-3:])
    forecasts = res.forecast(horizon=5)
    # print(forecasts.residual_variance.iloc[-3:])
    res = am.fit(last_obs='2011-1-1', update_freq=5)
    forecasts = res.forecast(horizon=5)
    # print(forecasts.variance.dropna().head())
    index = returns.index
    start_loc = 0
    end_loc = np.where(index >= '2010-1-1')[0].min()
    forecasts = {}
    for i in range(20):
        sys.stdout.write('.')
        sys.stdout.flush()
        res = am.fit(first_obs=i, last_obs=i + end_loc, disp='off')
        temp = res.forecast(horizon=3).variance
        fcast = temp.iloc[i + end_loc - 1]
        forecasts[fcast.name] = fcast
    # print()
    # print(pd.DataFrame(forecasts).T)
    import pandas as pd
    import numpy as np

    index = returns.index
    start_loc = 0
    end_loc = np.where(index >= '2010-1-1')[0].min()
    forecasts = {}
    for i in range(20):
        sys.stdout.write('.')
        sys.stdout.flush()
        res = am.fit(last_obs=i + end_loc, disp='off')
        temp = res.forecast(horizon=3).variance
        fcast = temp.iloc[i + end_loc - 1]
        forecasts[fcast.name] = fcast
    # print()
    # print(pd.DataFrame(forecasts).T)