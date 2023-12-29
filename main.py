from backtest import Displayer, BackTester
import talib
import pickle
import pandas as pd
import numpy as np
from my_ml import apply_thresholds

class SymbolicTestor(BackTester):
    def init(self):
        self.params = {'factor': pd.Series}
        
    @BackTester.process_strategy
    def run_(self, *args, **kwargs) -> dict[str: int]:
        factor = np.array(self.params['factor'])
        long_cond = factor > 0
        short_cond = factor < 0
        self.backtest_env['signal'] = np.where(long_cond, 1, np.where(short_cond, -1, np.nan))
        self.construct_position_(keep_raw=True, max_holding_period=1200, take_profit=None, stop_loss=None)
    
if __name__ == "__main__":
    # 输入第一列价格，第二列信号
    sample_data = pd.read_csv('./data/sample_data.csv',index_col=0)
    sample_data.index = pd.to_datetime(sample_data.index)

    # 读数据
    backtest_data = pd.DataFrame(index = sample_data.index)
    backtest_data.loc[:,['Open', 'High', 'Low', 'Close', 'Volume']] = sample_data.loc[:,['Open']]
    factor = sample_data.loc[:,['signal']]
    
    # 回测环境
    comm = [0, 0.0005]
    bt = SymbolicTestor(backtest_data, transact_base='Open',commissions=(comm[0],comm[1])) # 加载数据，根据Open成交,comm是买-卖
    
    # 策略回测
    bt.run_(factor=factor.values)
    
    # 策略结果
    md = bt.summary()
    md.out_stats.to_clipboard()
    print(md.out_stats)
    md.plot_(comm=comm, show_bool=True)
    bt.fees_factor
    out_stats, holding_infos, trading_details = md.get_results()
    md.save_results(file_name=comm)
    1