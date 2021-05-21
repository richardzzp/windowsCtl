import win32gui
import win32con
import win32api

if __name__ == '__main__':
    handle=win32gui.FindWindow("MSPaintApp",None)
    print("窗口句柄为："+str(handle))
