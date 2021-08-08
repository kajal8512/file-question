# my_file1=open("question.txt","r")
# # my_file1.write("")
# print(my_file1.read())
# for x in my_file1 .append in Delhi.txt:
#     print(x)


'''my_file =open("question.txt","r")
for i in range(30):
    c=my_file.readline()
    print(c)
    if "delhi" in c:
        delhi=open("delhi.txt","a")
        delhi.write(c)
    elif "shimla" in c:
        shimla=open("shimla.txt","a")
        shimla.write(c)
    else:
        other=open("other.txt","a")
        other.write(c)'''



my_file = open("question.txt","r")
for i in my_file:
    b=my_file.readline()
    print(b)
    if "Delhi" in b:
        Delhi=open("delhi1.txt","a")
        Delhi.write(b)
    
    if "Shimla" in b:
        Shimla=open("Shimla1.txt","a")
        Shimla.write(b)
    else:
        other1=open("other1.txt","a")
        other1.write(b)






















