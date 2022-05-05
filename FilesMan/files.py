with open("data", "w") as data:
    for i in range (1,6):
        data.write(f"test {i} hehe\n")

with open("data", "r") as data:
    count = 0
    for lines in data:
        print(f"Ligne {count+1} : {lines}")
        count += 1
    

    