@echo off
:TRYAGAIN
ECHO Checking connection, please wait...
PING -n 1 www.google.com | find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESS
IF     ERRORLEVEL 1 goto :TRYAGAIN
:SUCCESS
python .\completion_check.py %ComputerName% | find "Detected Completion" >NUL
IF NOT ERRORLEVEL 1 goto :START

:START
python .\simulate_click.py %ComputerName% | find "CRAWLING SUCCESSFULLY FINISHED !" >NUL
IF NOT ERRORLEVEL 1 goto :DONE

:DONE
shutdown.exe /s /t 00
pause
