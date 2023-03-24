candidates = []
with open("7-letter-words.txt","r") as file:
    for line in file:
        word = line.strip()
        if (word[0] == "H" or
            "l" in word or
            sum([ord(letter)-ord("a")+1 for letter in list(word.lower())]) != 42):
            continue
        
        candidates.append(word)

print(candidates)
