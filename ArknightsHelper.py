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
TASK_LIST['1-7'] = 20
TASK_LIST['building'] = 1
TASK_LIST['daily'] = 1
Ark = ArknightsHelper()
Ark.main_handler(task_list=TASK_LIST,clear_tasks=True)
