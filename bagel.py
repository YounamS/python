import random 

x = random.randrange(100,999)
print(x)



guess = 0
while guess != 3:
   y =int(input('three digit number :'))
   guess += 1
   print(guess)
   for a ,b in enumerate(str(x)):
    for c , d in enumerate(str(y)):
        if a == c and b == d:  
            print('fermi')
            break
        elif b != d :
           continue   
        elif b == d and a != c :
            print('pico')
       
else:
  print('used all your guess, answer :' ,x)
        

