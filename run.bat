
start cmd /k " ipconfig | findstr /R /C:"IPv4 Address" && mysite.exe runserver 0.0.0.0:8000 --noreload"
