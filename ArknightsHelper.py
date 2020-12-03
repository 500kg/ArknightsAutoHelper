import os

'''
这是一个示例文件，请不要直接运行。
'''

'''
main_handler 的启动模式
'''
from Arknights.helper import ArknightsHelper
from collections import OrderedDict

TASK_LIST = OrderedDict()
TASK_LIST['CE-5'] = 5
TASK_LIST['4-8'] = 10
TASK_LIST['building'] = 10
TASK_LIST['daily'] = 10
Ark = ArknightsHelper()
Ark.get_building()
#Ark.main_handler(task_list=TASK_LIST,clear_tasks=True)
