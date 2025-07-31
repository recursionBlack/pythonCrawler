# 1.安装      -- pip install requests

# 2.基本使用    -- 百度

import requests

# 找到目标url
# url = "http://www.baidu.com/"

# 构建请求头
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
# }


# 带上User-Agent发送请求
# headers参数接收字典形式的请求头,请求头字段名为key，值为value
# response = requests.get(url, headers=headers)
# print(response)     # <Response [200]>  200是状态码

# 打印响应内容
# response.encoding = "utf-8"
# print(response.text)    # 响应内容有乱码，requests模块会自动寻找一种解码方式去解码
# 用下面的更好
# print(response.content.decode())      # 默认utf-8
# print(response.request.headers)
# print(len(response.content.decode()))

# 3. 使用requests库保存图片

# 确定url
# url = "https://gips1.baidu.com/it/u=3088723663,373756956&fm=3042&app=3042&f=JPEG&wm=1,baiduai,0,0,13,9&wmo=0,0&w=512&h=512"
#
# # 发送请求，获取响应
# res = requests.get(url)
# # print(res.content)

# 打印响应的url
# print(res.url)
# # 打印响应对象的请求头
# print(res.request.headers)
# # 打印响应头
# print(res.headers)
# # 打印响应的编码方式
# print(res.apparent_encoding)

# 保存响应
# with open("1.jpg", "wb") as f:
#     f.write(res.content)

# 4.其他属性

# response.text 和response.content的区别
# text:     str类型， requests模块自动根据http头部对响应的编码做出有根据的推测
# content： bytes类型，可以通过decode()解码

# 5.用户代理

# 百度首页代码，爬取的比较少

# 请求头中，user-agent字段必不可少，表示客户端的操作系统以及浏览器的信息
# 添加User-Agent的目的，是为了让服务器认为是浏览器在发送请求，而不是爬虫程序在发送请求
