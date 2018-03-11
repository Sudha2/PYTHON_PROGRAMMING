f2=open("text1.txt","r+")
f2.read(int(input()))
print(f2.read())
f2=open("text1.txt","w+")
print(f2.write("one hundred twenty three"))
f2.close()


