a=[(1,12),(4,1),(12,10),(3,0)]
def get_second_element(x):
    return x[1]
     
a.sort(key=get_second_element)
print(a) #output:[(3, 0), (4, 1), (12, 10), (1, 12)]


b=[(1,12),(4,1),(12,10),(3,0)]
def get_second_element(x):
    return x[0]
     
b.sort(key=get_second_element)
print(a) #output:[(3, 0), (4, 1), (12, 10), (1, 12)]

data=[(1,2,12),(3,1,14),(1,1),(5,2,0)]

def get_third_element(y):
    return y[-1]
data.sort(key=get_third_element)
print(data) #output:[(5, 2, 0), (1, 1), (1, 2, 12), (3, 1, 14)]

data.sort(key=get_third_element,reverse=True)
print(data) #output:[(3, 1, 14), (1, 2, 12), (1, 1), (5, 2, 0)]

a=[10,12,11,1,10]
a.reverse()
print(a)

c=[1,2,3,4]
d=c
print(c is d)

d.append(5)
print(c)

d=c.copy()
d.append(6)
print(d)