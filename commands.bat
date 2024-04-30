@echo off
REM Comando para iniciar o servidor Flask

REM Caminho para o interpretador Python no ambiente virtual
set myenvform2\Scripts\python.exe

REM Caminho para o script Flask dentro do seu projeto
set run.py

REM Execute o servidor Flask
%PYTHON_EXE% %FLASK_SCRIPT%

rem Variável de ambiente myenvform2\Scripts\python.exe não definida
rem Variável de ambiente run.py não definida
