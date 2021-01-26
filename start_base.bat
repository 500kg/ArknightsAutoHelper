echo ArknightsAutoHelper is going to run in 60 seconds, if you don't need it, close this cmd.
@echo off
timeout 60
rem 修改ArknightsAutoHelper的路径和盘符
cd /D C:\Github\ArknightsAutoHelper

rem 修改雷电模拟器的路径
set emuPath=D:\Program Files\Nox\bin
set adb_service=127.0.0.1:62001
set username=%1%
set password=%2%
set c_id=%3%
rem echo -clone:Nox_2
set start_time=0
:A
echo running for %username%
timeout 30
rem 打开雷电模拟器
start "" "%emuPath%"\Nox.exe
timeout 120
rem 打开明日方舟
"%emuPath%"\adb.exe -s %adb_service% shell am start -n com.hypergryph.arknights/com.u8.sdk.U8UnityContext
timeout 60
rem 点击展示页
"%emuPath%"\adb.exe -s %adb_service% shell input tap 932 679
timeout 30
rem 点击账号管理
"%emuPath%"\adb.exe -s %adb_service% shell input tap 932 679
timeout 10
rem 点击账号登录
"%emuPath%"\adb.exe -s %adb_service% shell input tap 411 507
timeout 10
rem 点击账号
"%emuPath%"\adb.exe -s %adb_service% shell input tap 637 435
timeout 10
rem 输入账号
"%emuPath%"\adb.exe -s %adb_service% shell input text %username%
timeout 10
rem 点击账号
"%emuPath%"\adb.exe -s %adb_service% shell input tap 637 435
timeout 10
rem 点击密码
"%emuPath%"\adb.exe -s %adb_service% shell input tap 637 482
timeout 10
rem 输入密码
"%emuPath%"\adb.exe -s %adb_service% shell input text %password%
timeout 10
rem 点击密码
"%emuPath%"\adb.exe -s %adb_service% shell input tap 637 482
timeout 10
rem 点击登录
"%emuPath%"\adb.exe -s %adb_service% shell input tap 640 575
timeout 60

C:\Users\shism1\Anaconda3\envs\Ark\python.exe ArknightsHelper.py -u %username%

if %errorlevel% equ 1 (
timeout 2
if %start_time% lss 3 (
timeout 2
taskkill /f /im nox.exe
set /a start_time+=1
goto A
)
)
timeout 10
rem 关闭雷电模拟器
taskkill /f /im nox.exe