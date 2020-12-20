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
    TASK_LIST['daily'] = config.get(user + '/daily', 'True')

    TASK_LIST['building'] = config.get(user + '/building', 'False')
    TASK_LIST['credit'] = config.get(user + '/credit', 'False')
    Ark = ArknightsHelper()
    return Ark.main_handler(task_list=TASK_LIST, refill_with_item = refill_with_item)

if __name__ == '__main__':
    sys.exit(main())
    

