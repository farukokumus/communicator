import numpy as np 

# arrays way to define 
a= np. array([1,2.3],dtype="float64")
b= np.zeros((3,3),dtype="int64")
b1= np.ones((3,2),dtype="int64")*64
# if you are using shallow copy that will be = operator, it is going to change the original list and content. if you want real copies 
# need to use deep copy. Shallow copy only create new variable that points to same reference. But deepcopy create variable and recursively fill inside it
acopy= a.copy() # copy is important otherwise when change the value in acopy it will affect the a itself
acopy[1]=100
c= np.random.rand(5,3)
d= np.random.randint(-5,20,(3,3))
f= d.reshape((1,9))


# some properties 
print(a.ndim)
print(b.shape)
print(b.size)
print(acopy.dtype)



# indexing
print(c[:,:]) #all c and r
print(c[2:-1,:]) # 2nd r until last except last all c
print(c[2:-1,-1]) # only last column

# some math 
e=np.matmul(c,d)
print(d*2)
print(d+5)
print(np.cos(d))
print(d**2)


# stats 
print(np.min(d))
print(np.max(d,axis=0))
print(np.min(d,axis=1))

# stacking
print("stacking")
print(np.vstack((b,d)))

# advnced indexind
final = np.vstack((b,d))
print(final[(final > 0) & (final <10)])


print(a)
print(b)
print(b1)
print(acopy)
print(f)


