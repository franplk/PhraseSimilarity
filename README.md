```
该项目基于Gensim的Word2vec词向量模型，通过平均向量，编辑距离，词移距离等相关理论基础，编写的相似性计算方法。
旨在提供不同的计算方式，以及灵活的模型选择方式。
```



### 短语相似度对比

使用方式如下：
```
from model import PhraseSimilarity

sim_obj = PhraseSimilarity(model_path='[自定义模型]')
sim_obj.compare(sen1, sen2)

```



### 模型路径配置

该项目的模型文件是通过 Gensim 的word2vec模型训练， 支持模型自定义。用户可以根据自己的语料进行训练后，在配置文件中定义MODEL_PATH路径既可。

```
{
  "MODEL_PATH": "E:/TestFiles/work2vec/model/model_50_3_sg1.bin"
}
```



### API接口

如果需要通过网络方式访问，可以通过已经提供的API接口进行调用。

对外统一使用接口的方式调用，为保证接口的安全性问题，接口调用时可以使用Token验证，项目中已经提供了Token的验证，可自行使用。

下面列出了系统提供的所有接口以及使用方式。

```
注意：接口前缀统一为 '/api/'，下面说明中均省略前缀。
```

| 接口名称       | 接口地址           | 接口说明 |
| -------------- | ------------------ | -------- |
| 短语相似度比较 | /similarity/compare | 两个短语之间的相似度对比 |
| 多短语相似对比 | /similarity/compare/<mode> | mode分为map和mat类型 |



### 参考项目

[Synonyms](https://github.com/huyingxi/Synonyms)