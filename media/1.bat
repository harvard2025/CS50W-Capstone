@echo off
color 0a


setlocal enabledelayedexpansion

set "count=1"

:find_next_folder
if exist "D:\proggraming\Web Development\PrroCoders\V%count%" (
    set /a count+=1
    goto find_next_folder
)

set /a count-=1
code "D:\proggraming\Web Development\PrroCoders\V%count%\PrroCoders"

cd 'D:\proggraming\Web Development\PrroCoders'