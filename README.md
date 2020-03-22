```
该项目基于Gensim的Word2vec词向量模型，通过平均向量，编辑距离，词移距离等相关理论基础，编写的相似性计算方法。
在Synonyms基础之上进行了修改，以便支持自定义模型的选择。
```


### 短语相似度对比



#### 初始化加载模型

```
from model import PhraseSimilarity

sim_obj = PhraseSimilarity(model_path='[自定义模型]')

model_path：该参数需要用户指定模型的地址，测试模型可以通过文档下方的模型获取下载，或者用户可以自己使用Gensim库的Word2vec模型进行训练获得
```



#### 对比两个短语

```
simlarity = sim_obj.compare(sen1, sen2)

结果解释：直接返回两个词语 sen1和sen2 的相似度值
```



#### 短语列表两两对比

方式一：返回相似度矩阵，二维数组方式

```
result = sim_obj.compare_matrix(phrase_list)

结果解释：result[i][j]表示第i个词语与第j个词语的相似度值
```
方式二：以Map的方式返回

```
sim_obj.compare_map(phrase_list)

结果解释：通过result.get('k-i-j')获取第i个词语与第j个词语的相似度值
```

### WEB方式使用

提供了Flask Web服务的访问方式。如果需要通过网络方式访问，需要运行项目web服务，然后以API接口的方式进行调用，步骤如下。



#### 配置模型路径

用户可以根据自己的语料进行训练后，在配置文件中定义MODEL_PATH路径既可。

```
{
  "MODEL_PATH": "路径/model_name.bin" # 配置word2vec模型的路径
}
```



#### 服务器设置

可以使用默认，如果需要不同端口，可以在config/server.json中进行配置。

```
{
  "HOST": "127.0.0.1", # 配置哪些IP地址可以访问，默认本机，如果外网访问配置为"0.0.0.0"
  "SERVER_PORT": 8099, # 自定义对外端口开放
  "JSON_AS_ASCII": false # 无需修改，防止JSON化时中文乱码
}
```



#### 启动web服务

```
python run_web.py
```



#### 接口访问地址

```
访问接口通过 http://localhost:8099/api访问。
注意：接口前缀统一为 '/api/'，下面说明中均省略前缀。
其中 mode[map/mat]分别对应返回数据格式为map类型和矩阵类型
```

| 接口名称       | 接口地址           | 接口说明 |
| -------------- | ------------------ | -------- |
| 短语相似度比较 | /similarity/compare | 两个短语之间的相似度对比 |
| 多短语相似对比 | /similarity/compare/[mode] | mode分为map和mat类型 |



#### 返回结果说明

```
{
  "code": 200, //code为200表示成功，其他表示API访问失败
  "message": "结果信息", // 失败后返回的信息
  "data": "相似度对比结果" // 对应各类对比，相应的返回结果
}
  
```



### 模型获取

百度网盘地址：[获取模型](https://pan.baidu.com/s/1KG7au8gwJG1hNgGOXgpOCA) 
提取码：yesd


### 参考项目

[Synonyms](https://github.com/huyingxi/Synonyms)