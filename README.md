# BruteCaptcha

#### 介绍
用来python爆破时识别验证码
利用的是百度智能云的通用场景文字识别
#### 免费额度说明
未实名认证用户可领取 200 次/月，个人认证 1,000 次/月，企业认证 2,000 次/月。
PS：如果保留了调整前的免费额度就是50,000次/天


#### 程序流程

1.  访问图片url
2.  保存图片到path
3.  利用百度智能云的接口识别图片
4.  对识别的结果进行处理，如果有明显的错误就直接抛弃，重新识别图片


#### 使用说明
![输入图片说明](https://images.gitee.com/uploads/images/2021/1030/091833_9dc3fdb9_9789316.png "屏幕截图.png")
img_path为保存验证码的路径
url_path为获取验证码的路径
code_len为验证码的长度，如果识别出的验证码长度不对就直接丢弃
access_token是你在百度智能云获取的
char_set是判断识别出的验证码是否在这个集合里，
默认为大小写字母+数字，如果需要可以自己改

#### 使用案例
ps:注意BruteCaptcha.py要和你的程序放在同一个包里
![输入图片说明](https://images.gitee.com/uploads/images/2021/1030/092505_61149306_9789316.png "屏幕截图.png")

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


