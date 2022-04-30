import psutil,cpuinfo
cpumodel=cpuinfo.get_cpu_info()['brand_raw']
cpuarch=cpuinfo.get_cpu_info()['arch']
amountram=round(psutil.virtual_memory().total / (1024.0**3), 2)