@echo off
:top
cls

python compile.py tag %1 %2 %3 %4 %5 %6 %7 %8 %9
echo Press any key to restart. . .
pause>nul && goto :top

