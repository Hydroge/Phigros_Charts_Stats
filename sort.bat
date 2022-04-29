@echo off                                                                                                                                  
for /r ".\" %%i in (*.png) do (
md ".\%%~ni\"
move "%%i" ".\%%~ni\"
)
pause