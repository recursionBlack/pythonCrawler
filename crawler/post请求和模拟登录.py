
import requests
# 1.post请求

# post请求：登录注册，传输大文本内容
# requests.post(url, data)
# data参数接收一个字典

# get 跟post的区别
# get请求---比较多
# post请求---比较少

# get请求直接向服务器发送请求，获取响应内容
# post请求是先给服务器一些数据，然后再获取响应


# get请求携带参数---params
# post请求携带参数---data


# 2.cookie 模拟登录
# 登录后找到url
# cookie跟请求头加一块


# 3.post请求举例 -- 金山翻译
# import json
# url = "https://service.iciba.com/chat/authority/web?client=6&key=1000006&timestamp=1752666571092&signature=1d1edd8347efe6a3faede83889ba9799"
#
# # 请求头
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
# }
#
# # 构建data参数字典
# post_data = {
#     'from': 'zh',
#     'to': 'en',
#     'q': '中文'
# }
#
# res = requests.post(url, headers=headers, data=post_data)
# print(res.text)
#
# # 解析数据
# # 将json数据转换为python字典
# dic = json.loads(res.text)
# print(type(dic))
# print(dic["out"])

# 4.session  -- 自动处理cookie

session = requests.session()    # 实例化session对象
# response = session.post(url, data=data)

# 使用session访问登录后的页面
# session.get(url.text)


# 1.对访问登录后才能访问的页面去进行抓包
# 2.确定登录请求的url地址，请求方法和所需参数
# 3.确定登录后才能访问的页面url和请求方法
# 4.利用requests.session完成代码

# 5.cookie池

# user-agent池：短时间内，多次发出请求，每次请求都用不同的用户代理，防止被服务器认为是爬虫
# cookie池：每一个cookie就代表一个账号

# cookie有有效期
# session不用担心有效期的问题

# cookie跟session的区别：
# 1.cookie数据放在客户的浏览器上，session数据放在服务器上
# 2.cookie不是很安全，别人可以分析存在在本地的cooker并进行cookie欺骗，考虑到安全性应该用session
# 3.session会在一定时间内保存在服务器上，考虑到减轻服务器方面，应当使用cookie
# 4.可以考虑将登录信息等重要信息放在session，其他信息如果需要保存，可以放在cookie中