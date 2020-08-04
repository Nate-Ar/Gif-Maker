import os
os.system("Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
os.system('choco install python')
os.system('pip install Pillow')