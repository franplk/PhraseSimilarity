### Docker方式部署

```
部署做以下设定，可以根据情况修改：
项目文件夹名称：SimilarityProject
Docker镜像名称：python-ps:1.0
Docker容器名称：SimilarityProject
项目代码备份目录：code_bak
```



#### 初始/第一次部署

1. 确认Docker环境是否具备

   ```
   如果不具备Docker环境，请安装Docker
   ```

2. 制作Docker镜像

   ```
   需要在可以联网的机器上制作Docker镜像
   该目录下的Dockerfile为制作镜像的文件，通过该文件可以制作一个Python的镜像，其中包含了Python环境以及该项目依赖的的所有Python库。
   运行命令：docker build -t [镜像标签] [Dockerfile路径]
   
   > docker build -t python-ps:1.0 .
   
   ‘.’代表当前目录
   ```

3. 项目代码部署

   ```
   将项目的代码目录拷贝到要部署的目录下即可
   > cd /home/[用户名]
   > mkdir SimilarityProject
   > 将目录上传到该目录下
   ```

4. 启动项目的Docker容器

   ```
   切换到项目目录
   > cd /home/[用户名]/SimilarityProject
   运行容器
   > docker run -d -p 8090:8099 --name SimilarityProject -v $PWD/model:/usr/src/app/model -v $PWD/code:/usr/src/app/code -w /usr/src/app/code python-ps:1.0 python run_web.py
   ```



#### 版本更新部署

1. 将最新版本代码替换

   ```
   备份之前项目文件
   > mv -p code ./code_bak
   > 复制新代码到此目录
   ```

2. 重启项目的Docker容器

   ```
   > dockder restart SimilarityProject
   ```

   

#### 模型更新部署

1. 将最新的模型文件进行替换

2. 重启项目的Docker容器

   ```
   > dockder restart SimilarityProject
   ```

   