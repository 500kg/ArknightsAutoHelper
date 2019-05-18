# Arknghts Auto Helper
> 明日方舟辅助脚本，当然只是开发阶段

## 0x01 ADBShell 
基于夜神模拟器集成了多种adb操作方法，可以进行安卓辅助开发。当然你要在电脑端跑

### 运行须知

#### config.py
```python
ADB_ROOT = r"D:\Program Files\Nox\bin"
ADB_HOST = "127.0.0.1:62001"
SCREEN_SHOOT_SAVE_PATH = "D:\\python_box\\shaobao_adb\\screen_shoot\\"
STORAGE_PATH = "D:\\python_box\\shaobao_adb\\storage\\"

# arknights INFO
ArkNights_PACKAGE_NAME = "com.hypergryph.arknights"
ArkNights_ACTIVITY_NAME = "com.u8.sdk.U8UnityContext"
```

如想要二次开发，请修改`config.py`下的相关参数。以绝对路径为佳。

关于修改方法和样例代码，可以参考`ArknightsHelper_examples.py`下的代码和说明


#### 依赖包


```python
# python 版本 3.6 + 
Package    Version
---------- --------
certifi    2019.3.9
chardet    3.0.4
idna       2.8
Pillow     6.0.0
pip        10.0.1
requests   2.21.0
setuptools 39.1.0
soupsieve  1.9.1
tesserocr  2.4.0
urllib3    1.24.2
```

### 目前支持的功能

 - ADB 指令
 - 点击动作
 - 拖动动作
 - 截图动作
 - 获取子图
 - 子图与目标子图比较

## 0x02 ArknightsHelper
> 需要安装OCR模块

### 快速启动！快乐护肝！

之后通过这样的代码就可以迅速开始战斗，你需要手动选关。到如下画面
```python
from Arknights import ArknightsHelper
Ark = ArknightsHelper()
Ark.module_battle_slim(c_id='4-8', set_count=8)
# c_id 是战斗章节
# set_count 是战斗次数
```
![TIM截图20190513101009.png-1013.8kB][4]

理论上该模块比完整的模块稳定并且不容易被系统检测。并且该模块所有的点击序列都是随机化的，不容易被检测

### 任务清单功能

通过传入任务清单可以执行一系列任务。
目前支持的关卡请看在click_location.LIZHI_CONSUME中的关卡章节。
基本上里面的所有章节都测试过，但是总有一些奇奇怪怪的状况发生。并且请不要让你的自律翻车。不然就没了

```python
from Arknights import ArknightsHelper
from collections import OrderedDict

TASK_LIST = OrderedDict()
TASK_LIST['LS-4'] = 10
Ark = ArknightsHelper()
Ark.main_handler(TASK_LIST)
```

### 未安装OCR模块的用法
如果你没有安装OCR模块，需要在初始化时候赋予初值，该值为你当前的理智。
由于系统不知道你啥时候升级，所以减好了还需要重新设置。

```python
from Arknights import ArknightsHelper
from collections import OrderedDict

TASK_LIST = OrderedDict()
TASK_LIST['LS-4'] = 10
Ark = ArknightsHelper(100)# 
Ark.main_handler(TASK_LIST)
```

### 关于后续的想法

目前所有功能基本完善了，我也用的比较爽了。总之刷材料啥的都没啥问题。

之后可能会用 WXPYTHON 写个GUI。另外会写个访问好友基建的脚本。

### 自定义开发与更多功能

详情请联系作者或者提出你的issue！祝大家玩的愉快

欢迎来加好友

QQ 2454225341

## 0x03 关于一些常见的问题

TODO

  [4]: http://static.zybuluo.com/shaobaobaoer/27owy5sd99gk0ciqzgdrnnee/TIM%E6%88%AA%E5%9B%BE20190513101009.png