BackTrader项目安装简单，但是基于bar(k线)回测，不支持对tick的回测。    
cerebro是回测中心，汇总数据、策略等信息。以Data Feed形式传送数据（见公众号数据篇导读）。  
对于交易，可以打印交易日志。可以下达市价单、限价单、止损单、止盈单等，并加入滑点、税费、成交量等考虑。默认“当日收盘后下单，次日以开盘价成交”。但毕竟是bar数据不是tick数据，高频回测会有较大偏差。  
在公众号“常见案例汇总”中有多因子选股的策略示例。
## 官方文档
[官方Github](https://github.com/mementum/backtrader?tab=readme-ov-file)  
[官方说明文档](https://www.backtrader.com/docu/)  
## 公众号导读
QIML公众号对官方文档进行注释导读  
[QIML Github](https://github.com/QuantWorld2022/backtrader)

各篇章汇总如下  
[Backtrader来啦：先导篇](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653315531&idx=1&sn=f003da3d862e1a13349a10e006c5e748&chksm=802da3deb75a2ac85f3c3a6164f96303b70c12d14293f59fddf9a38c39a89bf4927b90b9e9c6&token=563856683&lang=zh_CN#rd)  
[Backtrader来啦：数据篇](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653315933&idx=1&sn=0b3e71d4bf59da67d837907e05aef8cb&chksm=802da148b75a285e3aa180a23132873646bf356191befc88831639146c68027ae4ab740a5e18&scene=21#wechat_redirect)  
[Backtrader来啦：指标篇](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653316290&idx=1&sn=ae9c9d548ccbbc7855bfc69d93182b8a&chksm=802da6d7b75a2fc1bc8614797e2c6f59b8196cfa78368175032575cbfdca825fc1031c74a61c&scene=21#wechat_redirect)  
[Backtrader来啦：交易篇（上）](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653316528&idx=1&sn=24f2c06b8f7da8dee6fe40f7c65b83a6&chksm=802da7a5b75a2eb36a921917ece8f010c1f81032edaeced6a50525ca1fff0cdfa42c0f9310e8&scene=21#wechat_redirect)  
[Backtrader来啦：交易篇（下）](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653316888&idx=1&sn=1e8343ced80444f2c125fb0dc6b587a1&chksm=802da50db75a2c1bc1e94490245292570aa82261e2d9d97705194ac41544af68d7d822e7e25b&scene=21#wechat_redirect)  
[Backtrader来啦：策略篇](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653317634&idx=1&sn=e92fec0b0b5fd5f62805e7c2be5830f8&chksm=802da817b75a2101c5812a6fc9daf0b2c08ce21d882bdd3059d2e9f391432b3ac9e950d5e151&scene=21#wechat_redirect)  
[Backtrader来啦：可视化篇（重构）](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653317947&idx=1&sn=8422b62036c4a0693114f6b779fb9cde&chksm=802da92eb75a20380ed04560bf2ed947d7879d5f0f806b094dccc30cc8de83e269c73c375931&scene=21#wechat_redirect)  
[Backtrader来啦：常见案例汇总](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653330626&idx=1&sn=83bed9723d81cd6b636f3efff43db926&chksm=802d5ed7b75ad7c19927c4fce4d5da4aa39d87bf9e519f1c5e64ee4aae82cdbb55c7e5ef5c65&token=1166282202&lang=zh_CN#rd)
<!-- ## 自己笔记
- 
	- 下图是 Bcaktrader 的主要模块，Backtrader 以“大脑”cerebro 为统一的调度中心，数据、策略、回测条件等信息都会导入 cerebro 中，并由 cerebro 启动和完成回测，最后返回回测结果：![[Pasted image 20231228114727.png]]
	-   Backtrader各模块各司其职，对模块进行灵活的配置可满足绝大部分的回测需求。通常的回测流程如下：
	- **step 1：构建策略**
		- 确定策略潜在的可调参数；
	    - 计算策略中用于生成交易信号的指标；
		- 按需打印交易信息；
	    - 编写买入、卖出的交易逻辑。
	- **step 2：实例化策略引擎 cerebro，由 cerebro 来驱动回测**
		- 由 DataFeeds 加载数据，再将加载的数据添加给 cerebro；
		- 将上一步生成的策略添加给 cerebro；
		- 按需添加策略分析指标或观测器；
		- 通过运行 cerebro.run() 来启动回测；
		- 回测完成后，按需运行 cerebro.plot() 进行回测结果可视化展示。
	- 用一张图总结以上步骤：
		  ![图片|500](https://mmbiz.qpic.cn/mmbiz_png/42N1g4fYAahBOcMBDrsHY9mH5v5D8FVI69tOYHP8TyJFxvjImlRT5YibWHaWpq0cXibYzicrVEO0NcPtZ2hZHC73g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
	-  -->