@echo off
:TRYAGAIN
ECHO Checking connection, please wait...
PING -n 1 www.google.com | find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESS
IF     ERRORLEVEL 1 goto :TRYAGAIN
:SUCCESS
python .\simulate_click.py
pause
