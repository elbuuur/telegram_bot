@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5285906181:AAFyBecEjJV9_Y802Gvtk9boTuZ2UzKREUc

python bot_telegram.py

pause
