import platform
import psutil
import cpuinfo

print(f"arsitektur: {platform.architecture()} ")
print(f"nama device pengguna: {platform.node()} ")
print(f"seri: {platform.machine()} ")
print(f"menggunkan os : {platform.platform()} ")

my_cpuinfo = cpuinfo.get_cpu_info()

print(f"cpunya : {my_cpuinfo['brand_raw']}")
print(f"kecepatan  : {my_cpuinfo['hz_actual_friendly']}")

print(f"total ram adalah {psutil.virtual_memory().total /1024 /1024 / 1024 :3f} gb " )