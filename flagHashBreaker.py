import hashlib
salt = "20b919258d31"
hashed = "f306d9b89b4ec90f6024323f4ce6fb33"
answer = []
with open("7-letter-words.txt","r") as file:
    for line in file:
        word = line.strip()
        saltedWord = word + salt
        hash_object = hashlib.md5(saltedWord.encode())
        if hashed == hash_object.hexdigest():
            answer.append(word)

print(answer)

