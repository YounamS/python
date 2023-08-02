x = list('abcdefghijklmnopqrstuvwxyz')
y = str(input('your message :'))
z = int(input('0 to 24 :'))
u = input('if you like e(encrypt) or d(decrypt):')
e =[]
d =[]

if u == 'e':
  for a in list(y):
    for b in x:
       c = x.index(b) + z
       if a == b and c <= 25 :
          e.append(x[c])
       elif a == b and c > 25 :
          e.append(x[c-26])
  print(e)
  print(''.join(e))

if u == 'd':
  for a in list(y):
    for b in x:
       c = x.index(b) - z
       if a == b and c <= 25 :
          d.append(x[c])
       elif a == b and c > 25 :
          d.append(x[c-26])
  print(d)
  print(''.join(d))


           