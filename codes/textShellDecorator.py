
# enter your name    
print ("Enter your name: ")
name = input().lower()

## replace all digits(numbers) only 
# import re 
# name = re.sub("\d", "", name)

# # replace special chars only 
# name = name.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})

# keep digits only 
# # name = filter(lambda x: x.isdigit(), name)

# https://stackoverflow.com/questions/23996118/replace-special-characters-in-a-string-python
# replace all numbers and special chars: just add in the list of chars below 
name = name.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+1234567890"})


x=1
y=1
    
canvas = []

for i in range(40):
    canvas.append([])
    for j in range(40):
        canvas[i].append(" ")

def a(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x][y+i]="#"
        canvas[x+2][y+i]="#"

def b(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,3):
        canvas[x][y+i] ="#"
    for i in range(3):
        canvas[x+i][y+2]="#"
    for i in range(1,4):
        canvas[x+2][y+i]="#"
    for i in range(3,5):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+4][y+i]="#"

def c(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,4):
        canvas[x][y+i]="#"
    for i in range(1,4):
        canvas[x+4][y+i]="#"
    
def d(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,3):
        canvas[x][y+i]="#"
    for i in range(1,4):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+4][y+i]="#"
    
def e(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,3):
        canvas[x][y+i]="#"
    for i in range(1,3):
        canvas[x+2][y+i]="#"
    for i in range(1,3):
        canvas[x+4][y+i]="#"
    
def f(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,4):
        canvas[x][y+i]="#"
    for i in range(1,3):
        canvas[x+2][y+i]="#"
    
def g(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,4):
        canvas[x][y+i]="#"
    for i in range(2,4):
        canvas[x+2][y+i]="#"
    for i in range(1,3):
        canvas[x+4][y+i]="#"
    for i in range(2,5):
        canvas[x+i][y+3]="#"
    
def h(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(5):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+2][y+i]="#"
    
def i(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
#    for i in range(3):
#        canvas[x][y+i]="#"
#    for i in range(3):
#        canvas[x+4][y+i]="#" 
     
def j(x,y,c=canvas):
    for i in range(1,4):
        canvas[x+i][y+2]="#"
    for i in range(1,4):
        canvas[x][y+i]="#"
    canvas[x+4][y+1]="#" 

def k(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(3):
        canvas[x+2+i][y+1+i]="#"
        canvas[x+i][y+3-i]="#"
    
def l(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y] ="#"
    for i in range(1,4):
        canvas[x+4][y+i] ="#"

def m(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    canvas[x][y+1]="#"
    canvas[x+1][y+2]="#"
    canvas[x][y+3]="#"
    for i in range(5):
        canvas[x+i][y+4]="#"
    
def n(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    canvas[x+2][y+2]="#"
    canvas[x+1][y+1]="#"
    for i in range(5):
        canvas[x+i][y+3]="#"  

def o(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,3):
        canvas[x][y+i]="#"
    for i in range(5):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+4][y+i]="#"
 
def p(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,3):
        canvas[x][y+i]="#"
    for i in range(3):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+2][y+i]="#" 

def q(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,3):
        canvas[x][y+i]="#"
    for i in range(5):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+4][y+i]="#"
    canvas[x+5][y+4]="#"
    canvas[x+3][y+2]="#"
      
def r(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(1,3):
        canvas[x][y+i]="#"
    canvas[x+4][y+3]="#"
    canvas[x+3][y+2]="#"
    canvas[x+2][y+1]
    for i in range(3):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+2][y+i]="#" 

def s(x,y,c=canvas):
    for i in range(3):
        canvas[x+i][y]="#"
    canvas[x+2][y+1]="#"
    canvas[x+2][y+2]="#"
    for i in range(1,4):
        canvas[x][y+i]="#"
    for i in range(3):
        canvas[x+2+i][y+3]="#"
    for i in range(3):
        canvas[x+4][y+i]="#"

def t(x,y,c=canvas):
    for i in range(1,5):
        canvas[x+i][y+2]="#"
    for i in range(5):
        canvas[x][y+i]="#"

def u(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(5):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+4][y+i]="#"

def v(x,y,c=canvas):
    for i in range(4):
        canvas[x+i][y]="#"
    for i in range(4):
        canvas[x+i][y+3]="#"
    for i in range(1,3):
        canvas[x+4][y+i]="#"
      
def excl(x,y,c=canvas):
    for i in range(3):
        canvas[x+i][y] ="|"
    canvas[x+4][y] ="@"
    
def w(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y]="#"
    for i in range(5):
        canvas[x+i][y+4]="#"
    canvas[x+4][y+1]="#"
    canvas[x+4][y+3]="#"
    canvas[x+3][y+2]="#"
    
def xx(x,y,c=canvas):
    for i in range(5):
        canvas[x+i][y+i]="#"
    for i in range(5):
        canvas[x+i][y+4-i]="#"

def yy(x,y,c=canvas):
    for i in range(2):
        canvas[x+i][y+i]="#"
    for i in range(5):
        canvas[x+i][y+4-i]="#"

def z(x,y,c=canvas):
    for i in range(4):
        canvas[x][y+i]="#"
    for i in range(5):
        canvas[x+i][y+4-i]="#"
    for i in range(5):
        canvas[x+4][y+i]="#"
    
def heart(x,y,c=canvas):
    for i in range(4):
        canvas[x+i+2][y+i] = "@"
    for i in range(4):
        canvas[x-i+5][y+i+4] = "@"
    for i in range(2):
        canvas[x][y+1+i] = "@"
        canvas[x][y+5+i] = "@"
    canvas[x+1][y] = "@"
    canvas[x+1][y+7] = "@"
    canvas[x+1][y+3] = "@"
    canvas[x+1][y+4] = "@"

#heart(1,1)
#heart(1,15)
#heart(1,30)
#heart(23,1)
#heart(23,15)
#heart(23,30)




alpha = "abcdefghijklmnopqrstuvwxyz"

for kk in range(len(name)):
    ltr = name[kk]
    if y > 37:
        kk -=1
        x += 8
        y = 1
    if ltr == " ":
        x+= 8
        y = 1
    else:
        if alpha.index(ltr) == 0:
            a(x,y)
            y+=5
        if alpha.index(ltr) == 1:
            b(x,y)
            y+=5
        if alpha.index(ltr) == 2:
            c(x,y)
            y+=5
        if alpha.index(ltr) == 3:
            d(x,y)
            y+=5
        if alpha.index(ltr) == 4:
            e(x,y)
            y+=4
        if alpha.index(ltr) == 5:
            f(x,y)
            y+=5
        if alpha.index(ltr) == 6:
            g(x,y)
            y+=5
        if alpha.index(ltr) == 7:
            h(x,y)
            y+=5
        if alpha.index(ltr) == 8:
            i(x,y)
            y+=2
        if alpha.index(ltr) == 9:
            j(x,y)
            y+=5
        if alpha.index(ltr) == 10:
            k(x,y)
            y+=5
        if alpha.index(ltr) == 11:
            l(x,y)
            y+=5
        if alpha.index(ltr) == 12:
            m(x,y)
            y+=6
        if alpha.index(ltr) == 13:
            n(x,y)
            y+=5
        if alpha.index(ltr) == 14:
            o(x,y)
            y+=5
        if alpha.index(ltr) == 15:
            p(x,y)
            y+=5
        if alpha.index(ltr) == 16:
            q(x,y)
            y+=5
        if alpha.index(ltr) == 17:
            r(x,y)
            y+=5
        if alpha.index(ltr) == 18:
            s(x,y)
            y+=5
        if alpha.index(ltr) == 19:
            t(x,y)
            y+=6
        if alpha.index(ltr) == 20:
            u(x,y)
            y+=5
        if alpha.index(ltr) == 21:
            v(x,y)
            y+=5
        if alpha.index(ltr) == 22:
            w(x,y)
            y+=6
        if alpha.index(ltr) == 23:
            xx(x,y)
            y+=6
        if alpha.index(ltr) == 24:
            yy(x,y)
            y+=6
        if alpha.index(ltr) == 25:
            z(x,y)
            y+=6


for i in range(len(canvas)):
    print("".join(canvas[i]))
    