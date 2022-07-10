@echo off
cls
for /r C:\Users\33652\Desktop\ %%a in (*) do if "%%~nxa"=="gameorno.py" set p=%%~dpnxa
IF defined p (
    python %p%
    ping 1.1.1.1 -n 5 > nul
    exit
)
echo "gameornot.py not found"