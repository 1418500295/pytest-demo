import base64

from Crypto.Cipher import AES


class AesUtil(object):

    __key = ""
    __iv = ""

    @staticmethod  #加密两次
    def encrypt2(data):
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        data = pad(data)
        # 字符串补位
        cipher = AES.new(AesUtil.__key.encode('utf8'), AES.MODE_CBC, AesUtil.__iv.encode('utf8'))
        encryptedbytes = cipher.encrypt(data.encode('utf8'))
        # 加密后得到的是bytes类型的数据
        encodestrs = base64.b64encode(encryptedbytes)
        en_ds = base64.b64encode(encodestrs)
        # 使用Base64进行编码,返回byte字符串
        enctext = en_ds.decode('utf8')
        # 对byte字符串按utf-8进行解码
        return enctext

    @staticmethod  #加密一次
    def encrypt1(data):

        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        data = pad(data)
        # 字符串补位
        cipher = AES.new(AesUtil.__key.encode('utf8'), AES.MODE_CBC, AesUtil.__iv.encode('utf8'))
        encryptedbytes = cipher.encrypt(data.encode('utf8'))
        # 加密后得到的是bytes类型的数据
        encodestrs = base64.b64encode(encryptedbytes)
        # en_ds = base64.b64encode(encodestrs)
        # 使用Base64进行编码,返回byte字符串
        enctext = encodestrs.decode('utf8')
        # 对byte字符串按utf-8进行解码
        return enctext

    # 解密
    @staticmethod
    def decrypt(data):
        data = data.encode('utf8')
        encodebytes = base64.decodebytes(data)
        # en_data = base64.decodebytes(encodebytes)
        # 将加密数据转换位bytes类型数据
        cipher = AES.new(AesUtil.__key.encode('utf8'), AES.MODE_CBC, AesUtil.__iv.encode('utf8'))
        text_decrypted = cipher.decrypt(encodebytes)
        unpad = lambda s: s[0:-s[-1]]
        text_decrypted = unpad(text_decrypted)
        # 去补位
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted
