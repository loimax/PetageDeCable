from asyncore import write



with open("data", "w") as data:
    count = 0
    data.write(f"  test {count+1} hehe")
    count += 1
    print(data.__doc__)
with open("data", "r") as data:
    count = 0
    for lines in data:
        print(f"Ligne {count+1} : {lines}", end='')
        count += 1
    

    