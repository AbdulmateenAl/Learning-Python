string = "1.2.3.4"
i = 0
for i in range(len(string)):
    if string[i] == ".":
        string = string[:i] + string[i+1:]
        print(string)
    else:
        print(string)