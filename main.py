import hashlib
# Hash is cc03e747a6afbbcbf8be7668acfebee5

md5_hash = input("Enter your hash: ")
hash_file = input("File name: ")
try:
    word_file = open(hash_file)
except:
    print("file not found")
    quit()
for word in word_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    if digest == md5_hash:
        print(word)
        break
