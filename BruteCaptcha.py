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















