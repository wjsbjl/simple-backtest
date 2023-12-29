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
- [精选文章](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1357158295060217858&__biz=MzI1MTQ2Njc5OQ==#wechat_redirect)
    - 我主要关注的是tick回测，所以看的这篇[vn.py社区精选8 - Tick数据载入和策略回测](https://mp.weixin.qq.com/s/yh6s-8bNonJjgv97HOFsFg)