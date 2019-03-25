# https://quantdare.com/numeros-de-fibonacci/



# -----------------------------------------------------
# user inputs for # of terms in the series - the usual stuff
terms = 0
try:
    terms  = int(input("enter number of levels :"))
    print (terms)
except: 
    print('skipping user input. front-end not supported')

if not terms > 0 :
    terms = 11

# --------------------------------------------------------------------
# números de Fibonacci
a = 0
b = 1 

series = []
series.append(a)
series.append(b)

for i in range(0,terms): 
    c = a +b 
    # print (c)
    series.append(c)
    a = b 
    b = c 
print ('fibonacci series : ', series)


# --------------------------------------------------------------------
# Triángulo de Pascal
print ('this is pascal triangle: ')

print ([1])
s = [1,1]
print (s)

for i in range(2,terms):    
    # print ('n=',n)
    n= [1]
    for j in range (1,i): 
        # s.append(a)
        # print ('s=',s)
        n.append( s[j-1]+s[j])
    n.append(1)
    print(n)
    s = n 


# --------------------------------------------------------------------
# Ternas Pitagóricas (Pythagorean Triple)

## First generate all combination of numbers in the [1, terms]
a = list(range(1,terms))
print (a)
import itertools
comb = itertools.combinations(a, 2)
print (comb)
## print the combinations 
# for p in comb:
#     print (p)

print ("Pythagorean triplets")
for p in comb:
    # print ('checking', p)
    a, b = p
    c= (a**2 + b**2)**0.5 
    # print ('c= ', c)
    if c%1 == 0 :   
        print (a,b, int(c//1) )


# --------------------------------------------------------------------
# generate formulaes from pascal triangle 
print ('this is pascal triangle assisted formulae generator ')

print ([1])
s = [1,1]
print (s)

for i in range(2,terms):    
    # print ('n=',n)
    n= [1]
    for j in range (1,i): 
        # s.append(a)
        # print ('s=',s)
        n.append( s[j-1]+s[j])
    n.append(1)
    print(n)
    s = n 

    # print formulae for (a+b)^n 
    print ("Printing : (a+b)^n for n=", len(n))
    for i in range(0,len(n)): 
        print(n[i], 'a^',len(n)-i,'b^', i, '+', end =" ")

# --------------------------------------------------------------------

