from matplotlib.pyplot import show, text
import psutil
import shutil
path = 'C:'

showMemory = psutil.virtual_memory()
diskSpace = shutil.disk_usage(path)

diskSpacePercents = round(diskSpace[1] / diskSpace[0] * 100, 1) # 1 = used, 0 = total

with open("memoryCheck.txt", "a") as textFile:
    textFile.write("Free RAM:   " + str(showMemory[4]) + "\n") # 4 = free
    textFile.write("Total RAM: " + str(showMemory[0]) + "\n"*2) # 0 = total
    textFile.write("Free memory on disk: " + str(diskSpace[2]) + "\n") # 2 = free
    textFile.write("Total memory on disk: " + str(diskSpace[0]) + "\n"*2) # 0 = total
    
    if showMemory[2] > 20:
        textFile.write("Your RAM is used over 20%! It is: " + str(showMemory[2]) + "%" + "\n") # 2 = percents
    if diskSpacePercents > 20:
        textFile.write("Your disk space is used over 20%! It is: " + str(diskSpacePercents) + "%" +  "\n")
    #if diskSpace

# print("Free RAM:   ", showMemory[4])
# print("Totatl RAM: ", showMemory[0])

# print("Free memory on disk:  ", diskSpace[2])
# print("Total memory on disk: ", diskSpace[0])



