# 此处定义了根据账户价值计算统计信息的函数。
# 统计结果：
    # short：计算投资收益率与最大回撤比值。若最大回撤（分母）为0则返回10。
    # long：分别输出包含逐笔交易的交易过程和基本统计信息，其中统计信息包括
        # 逐笔收益，操作胜率，收益率(年化),标准差(年化),夏普比率(年化),最大回撤水平,最大回撤比率,平均每日开仓次数,胜率
import numpy as np
import pandas as pd
def value2sttc_short(data_score):
    cash_value = data_score[['value']]
    rate_of_return = (cash_value.iloc[-1,0] / cash_value.iloc[0,0] - 1)
    max_drawdown = (cash_value.cummax() - cash_value).max()[0]
    return rate_of_return / max_drawdown if max_drawdown else 100

def value2sttc_long(data_score):
    # 每笔收益: 开多仓的费率是0.23*2/10000; 开空仓的费率是(3.45 + 0.23)/10000
    data_per_trade = data_score[['pos','value']].copy()
    data_per_trade.loc[data_per_trade.index[-1],'pos'] = 233
    data_per_trade.loc[(data_per_trade['pos'] == 0)|(data_per_trade['pos'] == data_per_trade['pos'].shift(1)),'pos'] = np.nan
    value_per_trade = data_per_trade.dropna()
    V1 = value_per_trade['value'].shift(-1)
    V0 = value_per_trade['value']
    _ = (V1 - V0 * 0.23/10000 - V1 * ((value_per_trade['pos'] == 1) * 0.23 + (value_per_trade['pos'] == -1) * 3.45)/10000) / V0 - 1
    data_score.loc[:,'return_per_trade'] = _

    adjustcount = len(value_per_trade) - 1 #因为加了一列
    daycount = len(set(x.date() for x in data_per_trade.index))


    cash_value = data_score[['value']]
    cashflow_temp = cash_value.copy()
    cashflow_temp = cashflow_temp.resample('d').last().dropna() # 转为日数据
    cashflow_temp['simple_return'] = cashflow_temp / cashflow_temp.shift(1)-1
    return_annual = (cashflow_temp['value'][-1]/cashflow_temp['value'][0]-1)  * 365 / (cash_value.index[-1]- cash_value.index[0]).days
    std_annual = cashflow_temp['simple_return'].std() * np.sqrt(252)
    sharpe_annual = (return_annual - 0.02) / std_annual
    sttc_rslt = pd.DataFrame(data = [return_annual, std_annual, sharpe_annual, 
        np.max(pd.DataFrame(cash_value).cummax() - pd.DataFrame(cash_value),axis=0)[0],
        np.max((pd.DataFrame(cash_value).cummax() - pd.DataFrame(cash_value))/
        pd.DataFrame(cash_value).cummax(),axis=0)[0],
        adjustcount/ daycount, (data_score.loc[:,'return_per_trade'] > 0).sum() / adjustcount],
        index = ['收益率(年化)','标准差(年化)','夏普比率(年化)','最大回撤水平','最大回撤比率','平均每日开仓次数','胜率'])
    sttc_rslt = round(sttc_rslt,4)
    return data_score, sttc_rslt
