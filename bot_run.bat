@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

python bot_telegram.py

pause
