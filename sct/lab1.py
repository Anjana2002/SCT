#create fuzzy set
X = {'a':0.7,'b':0.5,'c':0.2}
Y = {'a':0.8,'b':0.2,'c':0.9}
Z ={}

print('Union')
for i in X and Y:
    Z[i]=max(X[i],Y[i])  
print(Z)

print('Intersection')
for i in X and Y:
     if(X[i]<Y[i]):
        Z[i]=X[i]    
     else:
        Z[i]=Y[i]
print(Z)

print('Compliment of X')
for i in X:
    Z[i]=round(1-X[i],2)
print(Z)

print('Algebraic Sum ')
for i in X and Y:
    Z[i]=round(X[i]+Y[i]-X[i]*Y[i],2)
print(Z)

print('Bounded Sum')
for i in X and Y:
    Z[i]=min(1,X[i]+Y[i])
print(Z)

print('Bounded Difference')
def bd(X,Y):
    for i in X and Y:
        Z[i]=max(0,X[i]-Y[i])
bd(X,Y)
print(Z)