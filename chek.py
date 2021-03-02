import re 
# import codecs
# fileObj = codecs.open( "ch.txt", "r", "utf_8_sig" )
# text = fileObj.read() # или читайте по строке

file=open("C:\\python\\PP2\\w4\\bill.txt","r")
text=file.read()
Binpattern=r"\nБИН.*(?P<BIN>\b\d+)"
Ndspattern=r"\nНДС Серия.*(?P<NDS>\b\d+)"
Bintext=re.search(Binpattern, text).group("BIN")
Ndstext=re.search(Ndspattern,text).group("NDS")
itempatterntext=r"(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itmepattern=re.compile(itempatterntext)
for i in re.finditer(itmepattern,text):
    print(i.group("total2"))
file.close()