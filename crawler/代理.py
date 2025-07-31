
# 1.代理
# 代理ip是一个ip，指向的是一个代理服务器
# 代理服务器能够帮我们向目标服务器转发请求

# ip地址：精确的定位


# 2.代理： --- 正向代理 和 反向代理

# 正向代理：给客户端代理，让服务器不知道客户端的真是身份，
# 保护自己的ip地址不会被封，要封也是封代理ip
# 反向代理：给服务器做代理，让浏览器不知道服务器的真实地址，如nginx

# 2.2 实际上，理论来说分为三类的
# 1.透明代理：服务器知道我们使用了代理ip，也知道真实iop
# 2.匿名代理：服务器能够检测到使用了代理ip，但不知道真实ip
# 3.高匿代理，服务器即不能检测到使用了代理ip，也不知道真实ip

# 3.代理ip的使用

# proxies的形式：字典

# proxies = {
#     # 以键值对的形式，固定的语法，ip地址：端口号
#     'http': "http://12.34.56.79:9527",
#     "https": "https://12.34.56.79:9527"
# }

import requests
url = "https://www.baidu.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

# 构建代理字典

proxies = {
    # 第一种写法：
    'http': "12.34.56.79:9527",
    # 第二种写法：
    # "https": "https://12.34.56.79:9527"
}

res = requests.get(url, headers=headers, proxies=proxies)
print(res.content.decode())

# 代理ip无效，会自动使用本机的真是ip，所以才会访问成功
