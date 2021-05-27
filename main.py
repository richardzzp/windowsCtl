import win32gui
import win32con
import win32api
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import sys


def click1(x, y):  # 第一种
    '''非后台'''
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_it(pos):  # 第三种，可后台
    hwnd = win32gui.WindowFromPoint(pos)
    client_pos = win32gui.ScreenToClient(hwnd, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)


def doClick(cx, cy, hwnd):  # 第四种，可后台
    long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起


if __name__ == '__main__':
    # 获取句柄
    hwnd = win32gui.FindWindow("MSPaintApp", None)
    print("窗口句柄为：%d" % (hwnd))

    # 获取标题、类名
    title = win32gui.GetWindowText(hwnd)
    clsname = win32gui.GetClassName(hwnd)
    print('窗口标题为：{}\n窗口类名为：{}'.format(title, clsname))

    # 获取坐标
    x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
    print('窗口坐标为：{},{},{},{}'.format(x1, y1, x2, y2))

    # 还原最小化
    # win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    # print('还原最小化')

    # 还原最小化 2
    # if win32gui.IsIconic(hwnd):
    #     win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    # 设置高亮
    # win32gui.SetForegroundWindow(hwnd)
    # print('设置高亮')

    # 截屏
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save("screenshot.jpg")
    print('截屏完成')

    # 列举子窗口句柄
    # hwndChildList = []
    # win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd), hwndChildList)
    # print(hwndChildList)

    # 点击
    # subHwnd = win32gui.FindWindowEx(hwnd, 0, 'MSPaintView', None)
    # print('子窗口句柄：{}'.format(subHwnd))
    # subsubHwnd = win32gui.FindWindowEx(subHwnd, 0, 'Afx:00007FF71A030000:8', None)
    # print('子子窗口句柄：{:08X}'.format(subsubHwnd))
    # doClick(700, 500, subsubHwnd)
    # # click1(700, 500)
    # print('点击完成')
