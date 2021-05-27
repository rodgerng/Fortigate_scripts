@echo off
echo:config webfilter urlfilter
echo:edit 1
eccho:config entries
FOR /F "tokens=1-2 delims=" %%A IN (C:\%users%\desktop\whitelist.txt) DO (
echo    edit %%B
echo        set associated-interface "%1"
echo        set type fqdn
echo        set fqdn %%A
echo    next
)
:end
echo:end