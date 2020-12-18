import os
from datetime import datetime
'''
这是一个示例文件，请不要直接运行。
'''

'''
main_handler 的启动模式
'''
from Arknights.helper import ArknightsHelper
from collections import OrderedDict
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--ep", default = "1-7")
parser.add_argument("-c", "--credit", default = False)
args = parser.parse_args()
credit = args.credit
ep = args.ep
date = datetime.today()
weekday = date.weekday()

if weekday == 6 or weekday == 5:
    refill_with_item = True
else:
    refill_with_item = False

TASK_LIST = OrderedDict()
print(weekday)
#TASK_LIST['building'] = 1
if credit:
    TASK_LIST['credit'] = 1
TASK_LIST[ep] = 3000
TASK_LIST['daily'] = 1
Ark = ArknightsHelper()
Ark.main_handler(task_list=TASK_LIST, refill_with_item = refill_with_item)
