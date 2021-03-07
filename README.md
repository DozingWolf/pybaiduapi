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
1. 取增值税发票
2. 百度地图圆形缓冲区查询POI

## 文件目录结构
```
pybaiduapi
├─conf    配置文件
├────para.conf    主配置文件
├─demodata    测试数据
├─designdoc    设计资料
├─output    输出文件
├─storage    sqlite3文件存储位置
├────Token.db    token存储文件
├─main.py    窗体main
├─customizetool.py    自定义的一些工具函数
├─getbaidutoken.py    取百度api所需要的ak、sk等认证密钥工具
└─getvatinvoicedtl.py    baidu ai 发票票面ocr接口
```