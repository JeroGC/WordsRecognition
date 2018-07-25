from PIL import ImageGrab,Image
import keyboard #监控键盘
from time import sleep
import sys
from BaiDu import BaiDuAPI
from getText import GetText

#获取剪切板上的图片信息并保存到本地
def screenShot():
    #QQ截图按住Ctrl+A+alt截图，enter完成截图
    if keyboard.wait(hotkey='ctrl+alt+a')==None:
        if keyboard.wait(hotkey='enter')==None:
            sleep(0.01)
            #获取剪切板的图像内容
            im=ImageGrab.grabclipboard()
            #判断im的类型是否为图片
            if isinstance(im,Image.Image):
                im.save('imageGrab.png')
            else:
                print('重新截图')
    else:
        print('请按Ctrl+A+Alt来截图识别文字')

if __name__=='__main__':
    baiduapi=BaiDuAPI(r'C:\Users\Administrator\.spyder-py3\screenshot\password.ini')
    #baiduapi=BaiDuAPI
    
    #maxsize for循环是为了可以循环截图，一直不结束程序
    for _ in range(sys.maxsize):
    
        screenShot()
        
        text=baiduapi.picture2Text(r'C:\Users\Administrator\.spyder-py3\screenshot\imageGrab.png')
        
        print(text)
        GetText.setText(text)
        GetText.getText()