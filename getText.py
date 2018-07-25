import win32con
import win32clipboard as w

class GetText:
    #用于把图像获得的文字复制到剪切板里面的类
    @staticmethod
    def getText():
        #获取剪切板上的内容
        w.OpenClipboard()
        d=w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d
        
    @classmethod
    def setText(cls,aString):
        #传递一个参数用于复制到剪切板里面
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
        w.CloseClipboard()

#if __name__=='__main__':
    