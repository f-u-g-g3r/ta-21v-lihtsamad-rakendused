
import psutil
import shutil
import pip._vendor.requests
path = 'C:'

showMemory = psutil.virtual_memory()
diskSpace = shutil.disk_usage(path)

diskSpacePercents = round(diskSpace[1] / diskSpace[0] * 100, 1) # 1 = used, 0 = total

# Weather API
api_key = "48e84370663b15b4520231f167f6262b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Tallinn"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = pip._vendor.requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    z = x["weather"]

with open("memoryCheck.txt", "a") as textFile:
    textFile.write("Free RAM:   " + str(showMemory[4]) + "\n") # 4 = free
    textFile.write("Total RAM: " + str(showMemory[0]) + "\n"*2) # 0 = total
    textFile.write("Free memory on disk: " + str(diskSpace[2]) + "\n") # 2 = free
    textFile.write("Total memory on disk: " + str(diskSpace[0]) + "\n"*2) # 0 = total
    
    if showMemory[2] > 20:
        textFile.write("Your RAM is used over 20%! It is: " + str(showMemory[2]) + "%" + "\n") # 2 = percents
    if diskSpacePercents > 20:
        textFile.write("Your disk space is used over 20%! It is: " + str(diskSpacePercents) + "%" +  "\n" )

    textFile.write("\n" + "Temperature in Tallinn = " + str(round(current_temperature - 273.15, 1)) + "\n")
    textFile.write("\n" + "\n" + "\n" + "\n")


