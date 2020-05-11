### Docker方式部署

```
部署做以下设定，可以根据情况修改：
项目文件夹名称：SimilarityProject
Docker镜像名称：python-ps:1.0
Docker容器名称：SimilarityProject
项目代码备份目录：code_bak
```



#### 第一次部署前置条件 --- 制作镜像

```
鉴于以下几个原因：
1. Python的安装在Linux可能会根据不同的环境而安装方法不同，系统依赖库等问题，可能造成Python环境的部署耗费大量时间。
2. 相似词模型的运行需要的依赖包需要联网下载，
建议使用Docker的部署方式，需要制作模型运行环境的Python镜像。这样在Linux机器之上部署时不需要再安装Python以及系统依赖包
```

制作步骤如下：

1. 确认Docker环境是否具备

   ```
   如果不具备Docker环境，请安装Docker
   ```

2. 准备Dockerfile相关文件

   ```
   需要在可以联网的机器上制作Docker镜像
   1. copy文件到可以联网的系统
   2. 进入到Dockerfile所在目录，通过该文件可以制作一个Python的镜像，其中包含了Python环境以及该项目依赖的的所有Python库。
   
   注意：Dockerfile文件与requirements-web在同一目录中
   ```
   
3. 运行命令制作Docker镜像

   ```
   # 进入Dockerfile文件所在目录
   # 运行命令：docker build -t [镜像标签] [Dockerfile路径]
   # 这里镜像标签为python-ps:1.0，Dockerfile路径为当前路径，也即“.”
   > docker build -t python-ps:1.0 .
   
   ‘.’代表当前目录，不可省略
   ```

4. 验证镜像制作成功

   ```
   # 运行命令
   > docker images
   # 运行后 可以看到名称为 “python-ps” 的镜像即为成功
   ```

5. 导出镜像，便于分发

   ```
   # 运行以下命名，导出镜像
   > docker save -o /home/用户名/iamges/python-ps.tar python-ps:1.0
   # -o 指定输出目录
   ```

#### 初始/第一次部署

1. 导入镜像

   ```
   # 运行以下命名，导入镜像
   > docker load < /home/用户名/iamges/python-ps.tar
   # 其中 " < " 后面为镜像路径
   ```

2. 验证导入镜像成功

   ```
   # 运行命令
   > docker images
   # 运行后 可以看到名称为 “python-ps” 的镜像即为成功
   ```

3. 项目代码部署

   ```
   将项目的代码目录拷贝到要部署的目录（这里以/home/用户名为例）下即可
   > cd /home/用户名
   > mkdir SimilarityProject
   # 将项目代码以及模型文件上传到该目录下
   ```

4. 启动项目的Docker容器

   ```
   # 切换到项目目录
   > cd /home/[用户名]/SimilarityProject
   # 创建并运行容器
   > docker run -d -p 8090:8099 --name SimilarityProject -v $PWD/model:/usr/src/app/model -v $PWD/code:/usr/src/app/code -w /usr/src/app/code python-ps-slim:1.0 python run_web.py
   ```



#### 设置容器跟随服务器重启而重启

服务器重启后，需要容器内的服务也随之一起重启，从而避免因服务器故障而重新启动，可通过以下两个步骤完成

1. 设置Docker随服务器重启

   ```
   通过将Docker服务加入服务器初始启动服务里面来完成：
   > systemctl enable docker.service
   ```

2. 设置容器随Dokcer重启

   ```
   方式一：在运行容器时加入参数--restart=always
   举个例子：
   > docker run -d -p 8090:8099 --name=SimilarityProject --restart=always -v $PWD/model:/usr/src/app/model -v $PWD/code:/usr/src/app/code -w /usr/src/app/code python-ps-slim:1.0 python run_web.py
   
   方式二：如果容器已经创建，可以试用如下命令更新容器
   如果容器已经创建，可以试用如下命令更新容器
   > docker container update --restart=always [容器名字/容器ID]
   举个例子：
   > docker container update --restart=always SimilarityProject
   ```



#### 版本更新部署

1. 情况一：代码更新，将最新版本代码替换

   ```
   # 备份之前项目文件
   > mv -p code ./code_bak
   > 复制新代码到此目录
   ```

2. 情况二：模型更新，将最新的模型文件进行替换

3. 重启项目的Docker容器

   ```
   > dockder restart SimilarityProject
   ```


