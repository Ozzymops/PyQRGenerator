@ECHO off

SET VENV=".venv"

IF NOT EXIST "%VENV%\scripts\activate.bat" (
	pip.exe install virtualenv
	ECHO Creating virtual environment...
	python.exe -m venv %VENV%
)

IF NOT EXIST "%VENV%\scripts\activate.bat" (
	EXIT /B 1
)

CALL "%VENV%\scripts\activate.bat"

ECHO Updating requirements...
pip.exe install -r requirements.txt

cls

ECHO Starting...
flet run