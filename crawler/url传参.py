
# user-agent池       防止反爬
# 随机调用user-agent
# import random
# 第一种:构建池
# UAlist = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
# ]
#
# print(random.choice(UAlist))

# 第二种：fake_useragent    可能会出现异常
# from fake_useragent import UserAgent
# print(UserAgent().random)

# 2.浏览器发送请求的原理
# 1.构建请求
# 2.查找缓存
# 3.准备ip地址和端口
# 4.等待tcp队列
# 5.建立tcp连接
# 6.发送http请求

# 浏览器会向服务器发送请求行，包括了请求方法，请求url，http协议

# 3.url传参

# https://www.baidu.com/s?wd=%E5%AD%A6%E4%B9%A0&rsv_spt=1&rsv_iqid=0xece0e7b7000382da&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg

# 字符串被当作url提交是，会自动进行url编码处理

# 输入 --- 学习         明文
# 发送请求的时候 ---   %E5%AD%A6%E4%B9%A0   密文

# from urllib.parse import quote, unquote
# # quote()   # 明文转密文         传入参数类型是字符串
# # unquote() # 密文转明文         传入参数类型：%xx%xx
#
# print(quote("参数"))
# print(unquote("%E5%8F%82%E6%95%B0"))


# 4.发送带参数的请求

import requests
# url = "https://www.baidu.com/s?wd=%E5%AD%A6%E4%B9%A0"
#
# headers = {
#     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
# }
#
# response = requests.get(url, headers=headers)
# print(response.content.decode())

# 通过params携带参数字典
# 1.构建请求参数字典
# 2.发送请求的时候，带上请求参数字典


url = "https://www.baidu.com/s?"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

# 构建请求参数字典
name = input("请输入关键字")
kw = {"wd": name}

res2 = requests.get(url, headers=headers, params=kw)
print(res2.content.decode())