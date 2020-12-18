echo ArknightsAutoHelper is going to run in 60 seconds, if you don't need it, close this cmd.
@echo off
timeout 60
rem 修改ArknightsAutoHelper的路径和盘符
cd /D C:\Github\ArknightsAutoHelper

rem 修改雷电模拟器的路径
set emuPath=C:\LeiDian\LDPlayer4.0
set emu=dnplayer.exe 
rem set emuPath=D:\Program Files\Microvirt\MEmu
set username=%1%
set password=%2%
set c_id=%3%
echo running for %username%

rem 打开夜神模拟器
start "" "%emuPath%"\"%emu%" index=1
rem start "" "%emuPath%"\MEmu.exe
timeout 120
rem 打开明日方舟
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell am start -n com.hypergryph.arknights/com.u8.sdk.U8UnityContext
timeout 60
rem 点击展示页
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input tap 932 679
timeout 30
rem 点击账号管理
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input tap 932 679
timeout 10
rem 点击账号登录
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input tap 411 507
timeout 10
rem 点击账号
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input tap 637 435
timeout 10
rem 输入账号
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input text %username%
timeout 10
rem 点击账号
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input tap 637 435
timeout 10
rem 点击密码
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input tap 637 482
timeout 10
rem 输入密码
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input text %password%
timeout 10
rem 点击密码
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input tap 637 482
timeout 10
rem 点击登录
"%emuPath%"\adb.exe -s 127.0.0.1:5557 shell input tap 640 575
timeout 60
C:\Users\shism1\Anaconda3\envs\Ark\python.exe ArknightsHelper.py -e %c_id%
timeout 10
rem 关闭夜神模拟器
taskkill /f /im %emu%