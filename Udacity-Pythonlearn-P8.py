# To check if there are any obscene words in your file and if there is what are those words

import urllib.request

def read_text():
    Data_Profanity = open("Data.txt")
    b = Data_Profanity.read().split()
    #print(b)
    Data_Profanity.close()
    check_profanity(b)

def check_profanity(b):
    data=[]
    output1 = "FALSE"
    for i in b:
        i = i.rstrip('()')
        a = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+i)
        output=str(a.read())
        if "true" in output:
            output1= "TRUE"
            data.append(i)

    if output1 == "TRUE":
        print("Please check your file for obscene word (or words): "+str(data))
    else:
        print("No obscene words found")
    a.close()

read_text()

