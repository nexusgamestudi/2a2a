import psutil
import GPUtil
import cpuinfo
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_status(usage):
    return "Healthy ✅" if usage < 85 else "High Load ⚠️"

cpu_info = cpuinfo.get_cpu_info()
cpu_model = cpu_info['brand_raw']

while True:
    clear()
    print("CPU Model:", cpu_model)

    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_status = get_status(cpu_usage)
    print(f"CPU Usage: {cpu_usage:.1f}% -> {cpu_status}")

    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        gpu_usage = gpu.load * 100
        gpu_status = get_status(gpu_usage)
        print(f"GPU Usage: {gpu_usage:.1f}% -> {gpu_status}")
    else:
        print("No GPU detected ⛔")

    time.sleep(1)
