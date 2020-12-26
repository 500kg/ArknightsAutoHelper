import os
from datetime import datetime
import config
import sys

'''
这是一个示例文件，请不要直接运行。
'''

'''
main_handler 的启动模式
'''
from Arknights.helper import ArknightsHelper
from collections import OrderedDict
import argparse
import win32gui
import win32con

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--ep", default = "1-7")
    parser.add_argument("-c", "--credit", default = False)
    parser.add_argument("-b", "--building", default = False)
    parser.add_argument("-u", "--user", default ='LaoBa')
    args = parser.parse_args()


    user = "user_" + args.user
    date = datetime.today()
    weekday = date.weekday()
    if weekday == 6 or weekday == 5:
        refill_with_item = True
    else:
        refill_with_item = False

    TASK_LIST = OrderedDict()
    print(weekday)
    #TASK_LIST['building'] = 1
    ep = config.get(user + '/c_id', '1-7')
    TASK_LIST[ep] = 3000
    TASK_LIST['1-7'] = 3000 #削减体力至<7
    TASK_LIST['daily'] = config.get(user + '/daily', 'True')

    TASK_LIST['building'] = config.get(user + '/building', 'False')
    TASK_LIST['credit'] = config.get(user + '/credit', 'False')
    Ark = ArknightsHelper()
    return Ark.main_handler(task_list=TASK_LIST, refill_with_item = refill_with_item)

if __name__ == '__main__':
    hwnd = win32gui.FindWindow(None,u"夜神模拟器") #返回窗口标题为Adobe Acrobat的句柄
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 1839, 1064, right - left, bottom - top, win32con.SWP_SHOWWINDOW)

    sys.exit(main())
    

