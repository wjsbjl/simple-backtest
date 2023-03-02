# 总思路：t-2时刻获得仓位(利用了t-2的bar)，在t-1时刻的open进行交易，持有到t时刻open，计算收益
# 规则：
    # 1. 计算信号时，可以用当前(t时刻)的bar
    # 2. 信号和目标持仓时同期的
    # 3. 利用次日开盘进行交易from tqdm import trange
# TODO:删掉每日最后一个交易点点数据
from math import sin
from math import log
import numpy as np
import pandas as pd
import os
from datetime import datetime
if not os.path.exists('./result/'):   #os：operating system，包含操作系统功能，可以进行文件操作
    os.mkdir('./result/') #如果存在那就是这个result_path，如果不存在那就新建一个
from bkt_sgnl2pos import read_futdata
from bkt_sgnl2pos import _gt
from bkt_pos2value import pos2value
from bkt_value2sttc import value2sttc_short
from bkt_value2sttc import value2sttc_long
from tqdm import trange

if __name__ == '__main__':
    start = datetime.now()
    # 交易数据读取
    IC0 = read_futdata('IC期货')
    IC1 = read_futdata('IC期货(1)')

    # sgnl_cal，本文档中这部分是手算信号值
    data = IC0
    date_index = sorted(list(set([str(x)[:10] for x in data.index])))
    X4_out = []
    for i in trange(len(date_index)):
        _ = date_index[i]
        daily_data = len(data.loc[_,'future_close'])+1
        X4_out.append(list(range(1,daily_data)))
    X4_out = np.array(X4_out).reshape((-1))
    sgnl = _gt(data['future_close'].apply(sin),pd.Series(X4_out,index = data.index).apply(log))
    sgnl_ori = pd.DataFrame(sgnl,index = data.index,columns = ['sgnl'])
    sgnl_ori.to_csv('./result/sgnl.csv')

    # sgnl2pos
    # _ = pd.read_csv('./result/sgnl.csv',index_col=0)
    # sgnl_adjusted = sgnl2pos(_)
    # sgnl_adjusted.to_csv('./result/sgnl_adjusted.csv')

    # pos2value (函数内部用了sgnl2pos)
    data_score = pos2value(IC0,sgnl_ori)
    data_score.to_csv('./result/data_score.csv') # 1.418033471	1.410876263

    sttc_short = value2sttc_short(data_score) # 返回收益率/最大回撤

    trade_detail, sttc_long = value2sttc_long(data_score)
    trade_detail.to_csv('./result/long1.csv')
    sttc_long.to_csv('./result/long2.csv')

    end = datetime.now()
    elapsed = end - start
    print("Time elapsed:", elapsed) 

