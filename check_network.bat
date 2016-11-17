@echo off
:TRYAGAIN
ECHO Hello There my name is %ComputerName%
ECHO Checking connection, please wait...
PING -n 1 www.google.com | find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESS
IF     ERRORLEVEL 1 goto :TRYAGAIN
:SUCCESS
python .\completion_check.py %ComputerName% | find "Detected Completion" >NUL
ECHO Either its Crawler 1 and Continued else It detected it
IF NOT ERRORLEVEL 1 goto :START
IF     ERRORLEVEL 1 goto :NOTDONE
:START
ECHO STARTING THE CRAWLER
python .\simulate_click.py %ComputerName% | find "CRAWLING SUCCESSFULLY FINISHED !" >NUL
IF NOT ERRORLEVEL 1 goto :DONE
IF 	   ERRORLEVEL 1 goto :NOTDONE
:DONE
ECHO RESTING IN PEACE
shutdown.exe /s /t 00
pause

:NOTDONE
shutdown.exe /r /t 00
ECHO Something Just failed ! Gonna Retry 
pause