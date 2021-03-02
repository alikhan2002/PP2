# sub меняет символ в тексте, который мы желаем
# \s знак 
import re
txt="The rain in Spain"
x=re.sub("\s","9",txt)
print(x)