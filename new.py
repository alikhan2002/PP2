import re
import codecs
file= codecs.open( "raw.data", "r", encoding='utf-8' )
text = file.read() # или читайте по строке

# file = open('raw.data','r')
# text = file.read()

pattern = r"\nБИН.*(?P<BIN>\b[0-9]+).*\nНДС.*(?P<NDS>\b[0-9]+)"

x = re.compile(pattern)

for match in x.finditer(text):
    print(match)
file.close()