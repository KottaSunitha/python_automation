with open(r"C:\Users\sk21163\Downloads\world.txt") as f:
    s = " "
    word = input("Enter the searching word : ")
    count = 1

    while s:
        s = f.readline()
        l = s.split()
        if word in l:
            print(f"Line number : {count} : {s}")
        count += 1
