@echo off
cd /d "%~dp0"
where py >nul 2>&1
if %errorlevel%==0 (
    py server.py
    goto :eof
)
where python >nul 2>&1
if %errorlevel%==0 (
    python server.py
    goto :eof
)
echo.
echo Python is not installed or is not available in PATH.
echo Install Python 3 and run this file again.
echo.
pause
