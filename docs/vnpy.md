vnpy是很有货的宝藏项目。包括bar和tick回测，有GUI界面，社区也有很好的交流氛围。这里对该项目进行简要梳理。  

## 安装
github有.sh文件，但我在mac装完不兼容，后来是按照如下方式配置的。    

- 方法1
    - 新建环境 `conda env create --name vnpy python==3.10`  
    - 切换 `conda activate vnpy`  
    - 开装 `pip install -r ./requirements.txt`
    - ta-lib `conda config --add channels conda-forge\nconda install ta-lib==0.4.24`  
- 方法2
    - 后来发现有[官方安装文档](https://www.vnpy.com/docs/cn/index.html)，哈哈  
- 方法3
    - 如果是windows，可以使用他们的客户端  
## 初步使用
- 安装后还要进行[初步配置](https://mp.weixin.qq.com/s/eoK1v-BKg-Sw2HkEgvA-4w)  
- 然后进行数据配置，我目前采用的是[米筐 RQData](https://mp.weixin.qq.com/s/6SQgVVtJ4244W4lhtzavVQ)，也可以采取[其他数据配置方法](https://www.vnpy.com/docs/cn/community/info/datafeed.html)
- 还有些使用细节，比如  
    1. 无论变量还是参数，都**必须定义在策略类中**，而非策略类的__init__函数中；
    2. 参数和变量，均只支持Python中的四种基础数据类型：**str、int、float、bool**，使用其他类型会导致各种出错（尤其注意不要用list、dict等容器）；
    3. 如果在策略逻辑中，确实需要使用list、dict之类的容器用于数据缓存，**请在__init__函数中创建这些容器。**  
- 具体还是看公众号上的入门合集 [vn.py快速入门](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1357148569324879874&__biz=MzI1MTQ2Njc5OQ==#wechat_redirect)  
<!-- - [启动总结](https://www.vnpy.com/forum/topic/7281-vnpy-de-qi-dong-liu-cheng-zong-jie) -->
## 探索tick级回测
- 我主要关注的是tick回测，看了[精选文章](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1357158295060217858&__biz=MzI1MTQ2Njc5OQ==#wechat_redirect)，还是基于level1盘口数据，而非level2真正的逐笔数据    
    - [vn.py社区精选8 - Tick数据载入和策略回测](https://mp.weixin.qq.com/s/yh6s-8bNonJjgv97HOFsFg)  
    - [vn.py社区精选21 - Tick级的委托精细化管理](https://mp.weixin.qq.com/s/ZMFIZR5ldQGbfSlICG-duQ)
    - [vn.py社区精选22 - 看完这篇，彻底学会CSV历史数据导入！](https://mp.weixin.qq.com/s/5NmGO5enaUrCHbaTBuY3Ww)
    - [数据管理和查看](https://www.vnpy.com/forum/topic/3110-vn-pyfa-bu-v2-1-1-quan-gong-neng-shu-ju-guan-li)
## 结果展示
- [CTA回测](https://www.vnpy.com/docs/cn/community/app/cta_backtester.html)结果包括四张子图，分别是账户净值、净值回撤、每日盈亏、盈亏分布。在GUI界面的统计指标区域，还有日期信息、资金盈亏、交易成本、日均数据、绩效评价几个方面的常见策略统计量。此外还可以查询委托记录、K线图表等内容。   
- 除了结果展示外，对于开发好的策略，还有“参数优化”功能，可以从穷举算法、遗传算法几个方面优化结果。

<!-- CTA回测只支持期货 -->
<!-- ## 对接华泰证券数据服务
基本信息
名称：vnpy_insight
分类：数据服务（datafeed）
作者：fsksf（康师傅）
仓库：
Github
Gitee
协议：Apache License 2.0
功能：对接【华泰证券InSight金融数据服务】的VeighNa数据服务适配器 -->