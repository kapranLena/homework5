
x = input('your text')
with open('config', 'r') as cf:
     for line in cf:
         if x in line:
          print(line)
          break
     else:
         print('False')

y = open('config', 'a')
new_config = input('your new configur')
y.writelines(new_config)
y.close()

with open('config', 'r', encoding='utf-8') as cf:
    txt = cf.read()
    print(type(txt))
    print(txt)


