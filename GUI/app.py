# system package import
import wx
import wx.grid
import time
# GUI package import
from GUI.Frames import *
# Ark package import
from Arknights.base import ArknightsHelper
from Arknights.click_location import MAIN_TASK_SUPPORT
# MISC package import
from collections import OrderedDict
from GUI.Misc.events import ArkThread, stop_thread
# Setting package import
from GUI.Settings import *

global enable_init_ark_on_start


class ArknightsAutoHelperGUI(wx.App):
    def __init__(self):
        # self.Index = None
        self.worker = {}
        wx.App.__init__(self)
        self.ark = None
        self.__current_active_frame = "Index"
        self.__current_lizhi_onchange_lock = False  # 理智修改锁 true 代表修改锁
        self.__is_ark_init = False
        self.__slim_battle_choice = "36理智关卡"
        self.Index.m_statusBar1.PushStatusText("最近更新: slim模式中的关卡理智消耗宜多不宜少，火蓝之心的门票也算作理智消耗")
        if enable_init_ark_on_start:
            self.start_ark(event=wx.EVT_BUTTON)
            self.Index.m_statusBar1.PushStatusText("初始化完毕")
            self.__is_ark_init = True
        else:
            self.push_status_buffer("arknights 后台辅助未初始化，请点击初始化辅助按钮")
        self.backend_buffer_push()

    def push_output_buffer(self, strings):
        self.Index.out_put_ctrl.AppendText(strings.__str__() + "\n")

    def push_status_buffer(self, strings):
        self.Index.m_statusBar1.PushStatusText(strings.__str__() + "\n")

    def start_ark(self, event):
        try:
            self.ark = ArknightsHelper(call_by_gui=True, out_put=False)
            if not enable_init_ark_on_start:
                self.ark.is_ocr_active(self.ark.CURRENT_STRENGTH)
                self.Index.m_statusBar1.PushStatusText("初始化完毕") if self.ark.ocr_active \
                    else self.Index.m_statusBar1.PushStatusText("ocr 探针侦测失败，请赋予理智初值")
                self.ark.check_game_active()
            self.__is_ark_init = True
        except Exception as e:
            self.Index.out_put_ctrl.AppendText(e)
            self.__is_ark_init = False

    def login_ark(self, event):
        if self.__is_ark_init:
            MessageDialog_CANCEL("辅助不会采取你的个人数据，登陆模块仅用于自动登陆")
            self.worker['login'] = ArkThread(ark=self.ark, func='login')
        else:
            MessageDialog_OK("请先初始化辅助")

    def restart_ark(self, event):
        if self.ark is None:
            try:
                self.ark = ArknightsHelper(call_by_gui=True, out_put=False)
                self.ark.check_game_active()
                self.__is_ark_init = True
            except Exception as e:
                self.Index.out_put_ctrl.AppendText(e)
                self.__is_ark_init = False
        else:
            self.ark.destroy()
            try:
                self.ark = ArknightsHelper(call_by_gui=True, out_put=False)
                self.ark.check_game_active()
                self.__is_ark_init = True
            except Exception as e:
                self.Index.out_put_ctrl.AppendText(e)
                self.__is_ark_init = False

    def backend_buffer_push(self):
        if self.__is_ark_init:
            buffer = self.ark.shell_log.get_buffer()
            if buffer != "":
                self.Index.out_put_ctrl.AppendText(buffer)
            if not self.__current_lizhi_onchange_lock:
                self.Index.current_lizhi.SetValue(self.ark.CURRENT_STRENGTH.__str__())
        wx.CallLater(1500, self.backend_buffer_push)

    def OnInit(self):
        # Init All frames
        self.Index = Index(parent=None)
        # Init Router
        self.__bind_router()
        self.__bind_event()
        # Show Index
        self.Index.Show(show=True)
        return True

    def __bind_event(self):
        self.Index.main_start.Bind(wx.EVT_BUTTON, self.start_main)
        self.Index.slim_start.Bind(wx.EVT_BUTTON, self.start_slim)
        self.Index.set_init_strength.Bind(wx.EVT_BUTTON, self.set_init_strength)
        self.Index.main_reset.Bind(wx.EVT_BUTTON, self.reset_main)
        self.Index.slim_reset.Bind(wx.EVT_BUTTON, self.reset_slim)
        self.Index.init_ark.Bind(wx.EVT_BUTTON, self.start_ark)
        self.Index.reboot.Bind(wx.EVT_BUTTON, self.restart_ark)
        self.Index.login.Bind(wx.EVT_BUTTON, self.login_ark)
        self.Index.main_kill.Bind(wx.EVT_BUTTON, self.kill_main)
        self.Index.slim_kill.Bind(wx.EVT_BUTTON, self.kill_slim)
        self.Bind(wx.EVT_MENU, self.show_settings, id=self.Index.change_settings.GetId())
        self.Bind(wx.EVT_MENU, self.show_info, id=self.Index.about_me.GetId())
        self.Bind(wx.EVT_CHOICE, self.get_choice, id=self.Index.slim_battle_name.GetId(), )

    def get_choice(self, event):
        self.__slim_battle_choice = event.GetString()

    def show_settings(self, event):
        MessageDialog_CANCEL(
            message="设定修改页面施工中",
            title="提示信息"
        )

    def show_info(self, event):
        MessageDialog_CANCEL(
            message="关于该项目 \n 明日方舟辅助点击脚本 \n 项目地址 https://github.com/ninthDevilHAUNSTER/ArknightsAutoHelper"
        )

    def kill_main(self, event):
        if 'main_battle' in self.worker.keys():
            if self.worker['main_battle'].is_alive():
                stop_thread(self.worker['main_battle'])
                self.push_output_buffer("主战斗模块线程关闭成功")
                del self.worker['main_battle']
            else:
                self.push_output_buffer("主战斗模块线程已提前关闭")
                del self.worker['main_battle']
        else:
            self.push_output_buffer("主战斗模块线程未开启")

    def kill_slim(self, event):
        if 'slim_battle' in self.worker.keys():
            if self.worker['slim_battle'].is_alive():
                stop_thread(self.worker['slim_battle'])
                self.push_output_buffer("简略战斗模块线程关闭成功")
                del self.worker['slim_battle']
            else:
                self.push_output_buffer("简略战斗模块线程已关闭")
                del self.worker['slim_battle']
        else:
            self.push_output_buffer("辅助战斗模块线程未开启")

    def set_init_strength(self, event):
        if not self.__current_lizhi_onchange_lock:
            self.__current_lizhi_onchange_lock = True
            self.push_output_buffer("允许修改当前理智")
        else:
            setted_lizhi = self.Index.current_lizhi.GetValue()
            if setted_lizhi.isnumeric():
                self.ark.CURRENT_STRENGTH = int(setted_lizhi)
                self.__current_lizhi_onchange_lock = False
                self.push_output_buffer("赋予理智初值 ..{}".format(setted_lizhi))
            else:
                MessageDialog_OK("赋予理智初值失败")

    def reset_main(self, event):
        self.Index.task1_battle_name.SetValue("")
        self.Index.task1_battle_time.SetValue(0)
        self.Index.task2_battle_name.SetValue("")
        self.Index.task2_battle_time.SetValue(0)
        self.Index.task3_battle_name.SetValue("")
        self.Index.task3_battle_time.SetValue(0)
        self.Index.task4_battle_name.SetValue("")
        self.Index.task4_battle_time.SetValue(0)
        return True

    def reset_slim(self, event):
        # self.Index.slim_battle_name.CurrentSelection(0)
        self.Index.slim_battle_time.SetValue(0)
        return True

    def start_main(self, event):
        if self.__is_ark_init:
            TASK_LIST = OrderedDict()
            if self.Index.task1_battle_name.GetValue() != "":
                TASK_LIST[self.Index.task1_battle_name.GetValue()] = int(self.Index.task1_battle_time.GetValue())
            if self.Index.task2_battle_name.GetValue() != "":
                TASK_LIST[self.Index.task2_battle_name.GetValue()] = int(self.Index.task2_battle_time.GetValue())
            if self.Index.task3_battle_name.GetValue() != "":
                TASK_LIST[self.Index.task3_battle_name.GetValue()] = int(self.Index.task3_battle_time.GetValue())
            if self.Index.task4_battle_name.GetValue() != "":
                TASK_LIST[self.Index.task4_battle_name.GetValue()] = int(self.Index.task4_battle_time.GetValue())
            # print(TASK_LIST)
            for _ in TASK_LIST.keys():
                if _ not in MAIN_TASK_SUPPORT:
                    MessageDialog_OK("{} 不在支持的关卡列表中".format(_), "警告")
                    return False

            if TASK_LIST.__len__() == 0:
                MessageDialog_CANCEL("未选择关卡", "提示")
                return False
            else:
                if 'main_battle' in self.worker.keys():
                    if not self.worker['main_battle'].is_alive():
                        del self.worker['main_battle']
                    else:
                        MessageDialog_OK("请先关闭主战斗模块模块")
                        return False
                if 'slim_battle' in self.worker.keys():
                    if not self.worker['slim_battle'].is_alive():
                        del self.worker['slim_battle']
                    else:
                        MessageDialog_OK("请先关闭简易战斗模块模块")
                        return False
                self.worker['main_battle'] = ArkThread(ark=self.ark, TASK_LIST=TASK_LIST)
        else:
            MessageDialog_OK("请预先初始化 ark 类")

    def start_slim(self, event):
        if self.__is_ark_init:
            c_id = self.Index.slim_battle_id_to_c_id[self.__slim_battle_choice]
            set_count = int(self.Index.slim_battle_time.GetValue())
            if 'main_battle' in self.worker.keys():
                if not self.worker['main_battle'].is_alive():
                    del self.worker['main_battle']
                else:
                    MessageDialog_OK("请先关闭主战斗模块模块")
                    return False
            if 'slim_battle' in self.worker.keys():
                if not self.worker['slim_battle'].is_alive():
                    del self.worker['slim_battle']
                else:
                    MessageDialog_OK("请先关闭简易战斗模块模块")
                    return False
            self.worker['slim_battle'] = ArkThread(ark=self.ark, c_id=c_id, set_count=set_count)
        else:
            MessageDialog_OK("请预先初始化 ark 类")

    def __bind_router(self):
        pass

    def OnRouter_change(self, event, value='Index'):
        pass


def start_app():
    ArknightsAutoHelperGUI().MainLoop()
    wx.Exit()
