
with open("/usr/share/dict/words","r") as dict, open("7-letter-words.txt","w") as sevenletterwords:
    for line in dict:
        word = line.strip()
        if len(word) == 7: 
            sevenletterwords.write(word + '\n')