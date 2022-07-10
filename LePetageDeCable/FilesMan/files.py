import os
absolute_path = os.path.abspath(__file__) #get path without file name


with open(f"{os.path.dirname(absolute_path)}/data", "w") as data:
    for i in range (1,6):
        data.write(f"test {i} hehe\n")

with open(f"{os.path.dirname(absolute_path)}/data", "r") as data:
    count = 0
    for lines in data:
        print(f"Ligne {count+1} : {lines}")
        count += 1
    

    