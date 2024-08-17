# new file creation

# f = open('sample.txt','w')
# f.write('hello world')
# f.close()
# f1 = open("sample1.txt",'w')
# f1.write("dear world")
# f1.write("\nhow are you")#multi line 
# f1.close()

# already file editing but old content removed

# f2 = open("sample1.txt","w")
# f2.write("arshad nadeem 14 aug")
# f2.close()

# appending with old content while writing

# f = open('sample1.txt','a')
# f.write('\n i am fine again')
# f.close()

# writing multi lines using a list
# l = ['dafd\n','safdar\n','hayat\n','rawa']
# f = open('sample.txt','w')
# f.writelines(l)
# f.close

# reading a file

f = open('sample.txt','r')
s = f.read()#insert char like 10 inside read to read only 10 char
print(s)
f.close

# 