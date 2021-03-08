import re
import csv

file = open('hello.txt','r',encoding='utf-8')
text = file.read()


BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern = r"\nНДС.*(?P<NDS>\b[0-9]+)"
ZNMPattern = r"\nЗНМ.*(?P<ZNM>\b\w+)"
KASSAPattern=r"\nКасса.*(?P<KASSA>\b[0-9]+-[0-9]+)"
CHEKPattern = r"\nЧек.*(?P<Chek>\b №[0-9]+)"
DATAVREMYAPattern = r"\nВремя:*(?P<DV>.+)"
ADRESSPattern=r"\nг\.*(?P<Adress>.+)"

BINText = re.search(BINPattern, text).group("BIN")
NDSText = re.search(NDSPattern, text).group("NDS")
ZNMText = re.search(ZNMPattern, text).group("ZNM")
KASSAText = re.search(KASSAPattern, text).group("KASSA")
CHEKText = re.search(CHEKPattern, text).group("Chek")
DATAVREMYAText = re.search(DATAVREMYAPattern, text).group("DV")
ADRESSText = re.search(ADRESSPattern, text).group("Adress")

itemPatternText=r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>)"
itemPattern=re.compile(itemPatternText)

item=[["БИН","НДС","ЗНМ","Касса","Чек","Наименование товара","Цена за единиц","Кол-во","Дата и Время", "Адрес"]]
for i in re.finditer(itemPatternText, text):
    item.append([BINText, NDSText, ZNMText, KASSAText, CHEKText, i.group("name"), i.group("price"), i.group("count"), DATAVREMYAText,ADRESSText])

with open("files.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(item)
file.close()