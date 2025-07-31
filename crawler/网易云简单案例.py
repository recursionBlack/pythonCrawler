
import requests
# 1.获取单张图片
# 找到目标url
# url = "https://p5.music.126.net/obj/wonDlsKUwrLClGjCm8Kx/61205048731/f381/e627/4f6e/878de3342893d28f73c26bb4a20f590c.jpg?imageView&quality=89"
#
# # 构建请求头字典
# headers = {
#     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
# }
#
# # 发送请求，获取响应
# res = requests.get(url, headers=headers)
# # print(res.content)
#
# # 保存图片
# with open("网易云.jpg","wb") as f:
#     f.write(res.content)    # 二进制数据

# 2.获取单首歌曲


# 3.获取单个mv

# 4.获取贴吧单页

# url = "https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%80%E6%88%AE%E5%B0%96%E5%A1%94&fr=search"
#
# headers = {
#     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
# }
#
# res = requests.get(url, headers=headers)
# # print(res.text)
#
# with open("杀戮尖塔.html", "wb") as f:
#     f.write(res.content)

# 6.改写为面向对象

class Tieba:
    def __init__(self):
        self.url = "https://tieba.baidu.com/f?"
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
        }

    # 发送请求
    def send(self, parmas):
        res = requests.get(self.url, headers=self.headers, params=parmas)
        return res.text

    # 保存数据
    def save(self, page, cont):
        with open(f"{page}.html", "w", encoding="utf-8") as f:
            f.write(cont)

    def run(self):
        word = input("请输入贴吧名：")
        pages = int(input("请输入页数："))

        for page in range(pages):
            params = {
                "kw": word,
                "pn": page * 50
            }

            # 循环执行
            data = self.send(params)
            self.save(page, data)

te = Tieba()
te.run()
# 不让爬，被反爬了