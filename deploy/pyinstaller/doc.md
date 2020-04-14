### Pyinstaller打包部署

```
需要部署在windows机器上时，可以通过Pyinstaller打包的方式将Python的环境进行打包处理，从而在部署时，不需要在服务器上重新安装Python环境以及依赖。
```



#### 安装包制作

1. 安装Pyinstaller

   ```
   开发环境下安装 pyinstaller
   > pip install pyinstaller
   ```

2. 执行打包命令

   ```
   1. 将“package.spec”复制到项目根目录下
   2. 在开发环境终端，执行如下命令
   > pyinstaller package.spec
   ```



#### 项目部署启动

1. 项目代码部署

   ```
   上面打包完成后，在项目目录下会创建 dist 目录，该目录下就是打包完成的安装程序
   将该安装程序，复制到其他 windows 机器即完成部署。
   ```

2. 启动/访问项目

   ```
   1.启动：
   复制到其他机器上之后，进入该项目的文件夹“SimilarityProject”下面，运行 “runWeb.exe” 文件即可
   
   2.访问：
   浏览器访问 http://localhost:8099 既可
   ```

