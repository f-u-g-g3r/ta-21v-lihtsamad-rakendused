from matplotlib.pyplot import show
import psutil
import shutil
path = 'C:'

showMemory = psutil.virtual_memory()
diskSpace = shutil.disk_usage(path)
print("Free RAM:   ", showMemory[4])
print("Totatl RAM: ", showMemory[0])

print("Free memory on disk:  ", diskSpace[2])
print("Total memory on disk: ", diskSpace[0])
