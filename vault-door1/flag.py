fname = 'data.txt'
lst = []
letter_flag = []
index_flag = []
dict_flag = {}
flag = ''

f = open(fname, 'r')
for i in f.read().split():
      if i != '=':
            lst.append(i)

for a in range(len(lst)):
      if a % 2 == 1:
            letter_flag.append(lst[a])
      elif a % 2 == 0:
            index_flag.append(lst[a])

m = 0
for e in index_flag:
      dict_flag.update({int(e):letter_flag[m]})
      m += 1

t = sorted(dict_flag.items())

for o in t:
      flag += o[1]

print('picoCTF{' + flag + '}')
f.close()