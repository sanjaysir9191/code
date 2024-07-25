f=open("a1.txt","x")
f = open("a1.txt", "a")
f.write("Woops! I gfdgfdgfghave deletthgtgjhngdjted the content!")
f.close()

#open and read the file after the overwriting:
f = open("a1.txt", "r")
print(f.read())
