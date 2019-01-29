import psutil

cpucount = psutil.cpu_count()
print(cpucount)
cpucount = psutil.cpu_count(logical=False)
print(cpucount)
psutil
