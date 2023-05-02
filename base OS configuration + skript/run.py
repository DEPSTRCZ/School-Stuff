import platform
import cpuinfo
import psutil
from uptime import uptime
import wmi
import subprocess

stats = wmi.WMI().Win32_VideoController()

gpustr = ""

for x, elem in enumerate(stats):
    if len(stats) > 1:
        gpustr = gpustr + "," + str(elem.wmi_property('Name').value)
    else:
        gpustr = str(elem.wmi_property('Name').value)

print("Loading...")
print(f"""
┌───────┬─────────────────────────────────────────────────────
│ Stats │                                                
├───────┘                         
│ OS: {platform.platform()}
│ Host: {platform.node()}                       
│ Architecture: {cpuinfo.get_cpu_info()["arch"]}                      
│ CPU: {cpuinfo.get_cpu_info()["brand_raw"]} ({cpuinfo.get_cpu_info()["count"]}) @ {psutil.cpu_freq(percpu=False).current:.0f}
│ GPU: {gpustr}
│ RAM: {round(psutil.virtual_memory().total / (2 ** 20), 2)}MiB
│ DISK: {round(psutil.disk_usage("/").total / (1024 ** 3), 2)}GB
│ User: {psutil.users()[0].name}
├──────┬────────────────────────────────────────────────────────────────
│ Live │
├──────┘
│ CPU: {psutil.cpu_percent()}%
│ RAM: {round(psutil.virtual_memory().used / (2 ** 20), 2)} MiB (Free: {round(psutil.virtual_memory().free / (2 ** 20), 2)}MiB)
│ DISK: {round(psutil.disk_usage("/").used / (1024 ** 3), 2)}GB (Free: {round(psutil.disk_usage("/").free / (1024 ** 3), 2)}GB)
│ UPTIME: {uptime()/3600:.2f}Hours           
└──────────────────────────────────────────────────────────────────────────────────┘
""")
print("Launching desired program....\nipconfig /all")
result = subprocess.run("ipconfig /all", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.decode("cp1252"))