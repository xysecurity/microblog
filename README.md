# Welcome to XY's Microblog!


这是我在学习Python Web相关知识，并且使用FLask框架自己动手做的一个开源项目。

这个博客实现了用户登录、用户注册、发送博文、关注与被关注、用户主页、用户信息编辑、邮件发送等功能。

如果你愿意拿去学习使用（学习用途），请毫不犹豫的Clone。

这个项目会根据我学习的知识不断更新，感谢关注。

注：图片水印为我的个人微信公众号，欢迎查询关注。

This is my DIY open source project when I am learning about Python Web and using FLask framework.

This blog realizes the functions of user login, user registration, sending blog posts, follow and unfollow, user home page, user information editing, mail sending and so on.

If you are willing to use it (learning use), please do not hesitate to Clone.

This project will be updated constantly according to my learning knowledge. Thank you for your attention.

Note: image watermark is my personal WeChat Subscription . Welcome following.

## 如何使用  How to use

进入文件主目录，输入如下命令，创建数据库表，注意，需要提前配置好MySQL环境，端口为默认的3306。

Enter the file home directory, input the following command, create a database table, note that you need to configure the MySQL environment in advance, the port is the default 3306.

>./python createdb.py 


若命令行无报错，说明创建成功。

打开app目录，输入如下命令启动网站。

If the command line does not report an error, the creation is successful.

Open the app directory and input the following command to start the website.

>./python run.py

## 主要功能 Major functions

### 用户登录 User login

![Alt text](https://github.com/xysecurity/microblog/raw/master/image/login.png)

### 用户注册 User registration

![Alt text](https://github.com/xysecurity/microblog/raw/master/image/register.png)

### 发表博文 Sending blog posts
用户登录后，自动显示用户自己发表的以及关注的其他用户的博文，按照时间顺序排列。

After the user logs in, the blog posts of user and following users are automatically displayed in chronological order.

![Alt text](https://github.com/xysecurity/microblog/raw/master/image/login-in.jpg)

### 关注与取关Follow and unfollow

用户登录后，可以选择打开其他用户的界面，如未关注，可以点击关注按钮进行关注，关注后该用户发表的博文将显示在登录用户的主页。如登录用户已经关注了该用户，则可以点击取关按钮取消关注该用户。

假如用户A关注了用户B，则系统自动发送关注通知给用户B，取关则没有通知。

After the user logs in, he can choose to open the webpage of other users. If the user is not followed by current user, he can click the follow button to follow. 

After the following, the blog post published by the user will be displayed on the login user's homepage. If the logged-in user has followed the user, he can click the unfollow button to cancel the following.

If user A follows user B, the system automatically sends a notification of following to user B, and there is no notification for the unfollow.

![Alt text](https://github.com/xysecurity/microblog/raw/master/image/follow.jpg)

### 邮件发送 Mail sending
用户被关注后，系统将自动发送邮件给被关注用户，系统管理员首先需要在config.py文件中配置好系统发信邮箱的用户名和密码。

After the user is followed, the system will automatically send the email to the user who is being followed. 

The system administrator first needs to configure the username and password of the system sending email in the config.py file.

![Alt text](https://github.com/xysecurity/microblog/raw/master/image/email.jpg)

### 个人主页 User home page
打开个人主页时，系统将自动判断当前登录用户与打开用户的界面。若相同，则出现编辑用户信息按钮，若不同，则可以选择关注与取关，具体按钮根据当前用户是否关注该用户而定。

用户信息下面为该用户发表过的博文。

When opening personal home page, the system will automatically distinguish the current login user and the opened user.

If they are the same, the Edit User Information button appears. 

If they are different, he can choose to follow and unfollow. The specific button depends on whether the current user is following the user.

Below the user information is the blog post that the user has posted.

![Alt text](https://github.com/xysecurity/microblog/raw/master/image/personal.jpg)


### 信息更改 User information editing
用户在打开个人界面时，可以点击编辑按钮，修改个人的信息，如个人简介，用户昵称等，更改后数据将同步发送至数据库。

When the user visits the personal webpage, he can click the edit button to modify the personal information, such as personal profile, user nickname, etc.

The data will be sent to the database synchronously after the change.

![Alt text](https://github.com/xysecurity/microblog/raw/master/image/edit.png)

## 个人声明

这个项目为个人学习及展示记录用，整个项目并不成熟，也没有实现复杂的功能，大佬勿笑。

This project is used for personal learning and presentation. 

The whole project is not mature, and it does not implement complex functions.

Please don't laugh at me.
