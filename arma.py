from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARMA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox


class Arma():

    @staticmethod
    def adf_test(timeseries):  #adf检验
        adftest=adfuller(timeseries,autolag="AIC")
        return adftest[0]
    @staticmethod
    def stochastic(timeseries):   #随机性检验
        p_value=acorr_ljungbox(timeseries,lags=1)[1]
        return p_value

    @staticmethod
    def model_select(timeseries,max_lag,method="css"):
        init_bic=float("inf")
        init_p=0
        init_q=0
        init_proper_model=None
        for p in np.arange(max_lag):
            for q in np.arrange(max_lag):
                model=ARMA(timeseries,order=(p,q))
                try:
                    result_ARMA=model.fit(disp=-1,method=method)
                except:
                    continue
                bic=result_ARMA.bic
                if bic < init_bic:
                    init_p=p
                    init_q=q
                    init_proper_model=result_ARMA
                    init_bic=bic
        return init_bic,init_p,init_q,init_proper_model

