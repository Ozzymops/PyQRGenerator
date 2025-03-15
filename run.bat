:: Start
@ECHO OFF
CD .venv/Scripts
CALL activate
CD ../..

:: Input
SET /p NAME=Naam: 
SET /p BDAY=Geboortedatum [dd-mm-yyyy]: 
SET /p TELN=Telefoonnummer: 

:: End
py pyqr.py "%NAME%" "%BDAY%" "%TELN%"
SET /p WAIT=Finished. Press ENTER to exit.