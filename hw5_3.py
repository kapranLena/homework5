
x = input('your text')
with open('config', 'r') as cf:
     for line in cf:
         if x in line:
          print(line)
          break
     else:
         print('False')

with open('config', 'r') as cf:
    text = cf.read()
    x = input("from")
    y = input("to")
text = text.replace(x, y)

with open ('config', 'w') as cf:
     cf.write(text)

with open('config', 'r', encoding='utf-8') as cf:
    txt = cf.read()
    print(type(txt))
    print(txt)


