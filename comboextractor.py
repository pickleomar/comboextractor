#textwithcombos=input("Drag your text file here or type in its path")
from time import sleep
def listing(s):
    k=''
    for i in s:
        k += i
    return k
def stopby(line,sym,assignement,value):
    count=0
    liststart = []
    listend = []
    num = line.find(sym)
    if num == -1:
        return True
    else:
        if sym == '@':
            if assignement == '+':
                while True:
                    count+=1
                    if num+count == len(line):
                        break
                    end=line[num+count]
                    if end in '|": /\\;()[]{}-,~^':
                        if value == "1":
                            return num+count
                        break
                    listend.append(end)
            elif assignement == '-':
                while True:
                    if num+count == 0:
                        break
                    count -= 1
                    start=line[num+count]
                    if start in '|": /\\;()[]{}-,~^':
                        break
                    liststart.append(start)
        if sym== ':':
            if assignement == '+':
                while True:
                    count += 1
                    if num+count == len(line):
                        break
                    end = line[num + count]
                    if end in '|": /\\;()[]{}-,~^':
                        break
                    listend.append(end)
            elif assignement == '-':
                while True:
                    if num + count == 0:
                        if value == '1':
                            return int(num + count)
                        break
                    count -= 1
                    start = line[num + count]
                    if start in '|": /\\;()[]{}-,~^!':
                        if value == '1':
                            return int(num + count)
                        break
                    liststart.append(start)
    liststart.reverse()
    return (liststart+listend)
def email_pass():
  linex= open(directory, 'r',encoding='utf-8')
  combo = []
  for i in linex.readlines():
      x= i.replace('\n','')
      p=stopby(x, '@', '+', '1')
      q=stopby(x[p::], ':', '+', '0')
      #combo.append(q)
      if q == True:
          continue
      if p == True:
          continue
      pasw = listing(q)
      email = listing(stopby(x, '@', '-', '0') + ['@'] + stopby(x, '@', '+', '0'))
      combo.append(email+':'+pasw)
  return combo
def username_pass():
    lines= open(directory,'r',encoding='utf-8')
    combo=[]
    for i in lines.readlines():
        x=i.replace('\n','')
        q= stopby(x[stopby(x,':','-','1')::],':','+','0')
        if q == True:
            continue
        username= listing(stopby(x,':','-','0'))
        passw= listing(q)
        combo.append(username+':'+passw)
    return combo
def main():
    choice = input("Choose the type of your leeching:\n1.Email and password combo\n2.Username and password combo\n: ")
    c = open('combo.txt', 'w+',encoding='utf-8')
    if choice == '1':
        for i in email_pass():
            c.write(i+'\n')
    elif choice == "2":
        for i in username_pass():
            c = open('combo.txt', 'a')
            c.write(i+'\n')
    else:
        print('Wrong choice Try again :')
directory=input('Insert your text file directory or just drag it here: ')
if directory == '':
    directory = 'accounts.txt'
else:
    directory = directory.replace("'", '')
main()
