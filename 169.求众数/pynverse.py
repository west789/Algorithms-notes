import math
print(math.e)
print(math.exp(1))
print(math.log(100, 10))

def get_u(v):
    u = math.log((((
            (math.pow(math.e, (-0.67))-1)*(math.pow(math.e, (-0.67*0.05*v))-1))/(math.pow(math.e, (-0.67*v))-1))+1), math.e)/(-0.67)
    return u


v = [
0.059432505,
0.057326712,
0.055138524,
0.05310435,
0.052917526,
0.050809527,
0.049089562,
0.047159739,
0.046868242,
0.047502104,
0.046464732,
0.044731852,
0.05142956,
0.061063463,
0.06108599,
0.058785725,
0.057402951,
0.065348051,
]
u=[]
v1 = [1]
for item in v:
    vitem =8.0551*math.pow(10, (-6))+0.91166*item+0.1738 
    u1 = get_u(vitem)
    u.append(u1)
print(u)
