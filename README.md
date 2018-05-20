### 安装python3和python3的虚拟环境
1. ubuntu下输入命令安装python3虚拟环境
```
sudo pip3 install virtualenv
```
默认使用pip的话会安装python2的虚拟环境。
----------------------------------------------------------------------------
### Windows下配置python web环境(ubuntu下同理)
首先
```
git clone https://github.com/piaoliangkb/Flask-facelabel.git
```
1. cmd切换到Flask-facelabel-master目录下，输入virtualenv venv新建虚拟环境。
> ubuntu下 sudo virtualenv venv
2. 输入venv\Scripts\activate进入虚拟环境，进入成功之后左则会显示(venv)
> ubuntu下输入 source venv/bin/activate
输入python --version检查python版本是否为python3

![](https://upload-images.jianshu.io/upload_images/11146099-709184b9f510089f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 之后输入pip install -r requirements.txt安装需要的包，安装成功后显示
![](https://upload-images.jianshu.io/upload_images/11146099-1bfa12040d7b9155.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> sudo pip install -r requirements.txt

4. 输入python facelabel.py，浏览器输入127.0.0.1:5000可以正常访问网页。
![](https://upload-images.jianshu.io/upload_images/11146099-aa3d8bdc7b9c8fd7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> sudo python facelabel.py
--------------------------------------------------------------------
### 之后修改matlab和python中的文件路径

5. matlab程序里边保存图片的位置改为当前工程目录下的static\faceImg
![](https://upload-images.jianshu.io/upload_images/11146099-33076e71d4f6a852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（这里改为绝对路径，我这个图是相对路径，不同电脑不一样）
6. 打开facelabel.py文件，修改![](https://upload-images.jianshu.io/upload_images/11146099-ed6117d5a52bb7e4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)为当前工程目录下static/faceImg文件夹。
7. 先跑matlab跑出人脸序列文件，然后打开网页，每个序列最多显示8张图片，下边是当前文件夹的名字。后边是修改框。

---------------------------------------------------------------------------------------------------
### ubuntu下配置nginx
1. 安装nginx
```
sudo apt-get install nginx
```
2. 修改nginx配置文件  
nginx配置文件在/etc/nginx/nginx.conf
```
sudo vi /etc/nginx/nginx.conf
```
在http模块中加入如下部分：
```
server {
        listen 80;
        server_name ip;

        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}

```
![](https://upload-images.jianshu.io/upload_images/11146099-7a8de6ea76c22291.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- listen后可以为任意数字，表示监听端口
- server_name输入局域网内ip地址
- location后照抄

3. nginx启动
```
sudo nginx
```
或者
```
sudo service nginx start
```
4. 修改配置之后nginx需要重启
```
sudo nginx -s reload
```

----------------------------------------------------------------------------------------
### 安装gunicorn建立python web app和nginx之间关系
1. 在web项目下进入虚拟环境，安装gunicorn
```
sudo pip install gunicorn
```
2. 输入如下命令启动python程序
```
sudo gunicorn -w 4 -b 127.0.0.1:8000 facelabel:app
```
- -w 4表示启动4个worker处理网络请求
- 127.0.0.1:8000需要与nginx.conf中proxy_pass一致
