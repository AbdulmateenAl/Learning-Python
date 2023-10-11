def up_low(s):
    upp = 0
    low = 0
    # Remove space from string
    s = s.replace(' ', '')
    for i in s:
        if i.isupper():
            upp+=1
        elif i.islower():
            low+=1
    print(s)
    return f"No of upper case char = {upp} and No of lower case char = {low}"

print(up_low('Hello Mr, Rogers, how are you this fine Tuesday'))