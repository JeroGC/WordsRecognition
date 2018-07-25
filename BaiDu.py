#安装百度的aip，pip install baidu_aip，调用aip做图像中文字的识别
from aip import AipOcr
import configparser


class BaiDuAPI:
    #调用百度云的API实现图片文字的识别
    def __init__(self,filePath):  #注意！！！两条下划线
        #实例化configparser
        target=configparser.ConfigParser()
        #读取ini文件
        target.read(filePath)
        #读取工单信息
        #target.get第一个参数是section，第二个参数是键名，返回对应值
        #每一个应用的下面三个值不一样，实时更改
        app_id=target.get('工单密码','APP_ID')
        api_key=target.get('工单密码','API_KEY')
        secret_key=target.get('工单密码','SECRET_KEY')
        
        #APPID AK SK
        APP_ID=app_id
        API_KEY=api_key
        SECRET_KEY=secret_key
        
        #传递到AipOcr里面
        self.client=AipOcr(APP_ID,API_KEY,SECRET_KEY)
        #self.client=AipOcr('11564658','alzBCjQotb4Bk8rZLZcO2cWG','IDCCuEUydqI5RivrCuRamY0cKXjPEcon')

    
    def picture2Text(self,filepath):
        image=self.getFileContent(filepath)
        #调用通用的文字识别，图片参数为本地图片
        texts=self.client.basicGeneral(image)
        #print(texts)
        allTexts=''
        #得到的text分排显示了，需要连接一下
        for words in texts['words_result']:
            allTexts=allTexts+''.join(words.get('words',''))
        return allTexts
            
    @classmethod
    def getFileContent(self,filepath):
        with open(filepath,'rb') as fp:
            return fp.read()
        
if __name__=='__main__':
    baiduapi=BaiDuAPI(
            r'C:\Users\Administrator\.spyder-py3\screenshot\password.ini')
    #aiduapi=BaiDuAPI
    text=baiduapi.picture2Text(
            r'C:\Users\Administrator\.spyder-py3\screenshot\imageGrab.png')
    print(text)