st = 'Print only the words that starts with s in this sentence'

#To print words that starts with 's'
words = st.split()
#Gets the words from the string st
for i in words:
#using an if statement to check for words that starts with 's'
    if (i[0] == 's'):
        print(i)
    else:
        pass