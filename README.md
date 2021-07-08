# pybaiduapi
 百度各种接口的python实现
## 准备实现的功能
1. 取增值税发票票面信息
2. ocr取普通文字
3. 图片表格转出excel
4. 百度地图圆形缓冲区查询POI
```
如果有其余想要实现的功能，可以给我留言
```
## 已经实现的功能
1. 取增值税发票,并模拟成发票二维码识别结果
2. 百度地图圆形缓冲区查询POI

## 文件目录结构
```
pybaiduapi
├─conf    配置文件
├────para.conf    主配置文件
├─demodata    测试数据
├─designdoc    设计资料
├─output    输出文件
├─input    输入文件
├─storage    sqlite3文件存储位置
├────Token.db    token存储文件，系统自动建立
├─log    系统日志
├─main.py    窗体main
├─mainfunc.py    系统入口
├─customizetool.py    自定义的一些工具函数
├─getbaidutoken.py    取百度api所需要的ak、sk等认证密钥工具
├─getvatinvoicedtl.py    baidu ai 发票票面ocr接口
└─businessfunc.py    业务逻辑封装
```

## 使用步骤
1. 安装python3 开发使用3.6.8，可以使用3.6.8或以上版本，不建议使用3.6版本以下
2. 下载本应用包，解包至电脑，文件目录路径上不能有中文字符
3. 至百度AI平台申请账户并创建应用，应用内需要包含【增值税发票识别】等本应用提供的功能
4. 记录百度提供的AK和SK，配置至./conf/para.conf配置文件内
5. 将需要识别处理的发票图片复制进./input/目录内
6. 打开终端，路径定位至本应用的根目录内
7. 在终端内执行cli：python mainfucn.py
8. 执行完成后在./output/路径内会生成invoice_list.txt文件，该文件内记录识别后的发票信息，数据记录模拟成发票票面二维码识别结果，该数据可以按用户需求来进行使用
## 注意！
1. 本应用暂时只提供增值税发票的识别功能