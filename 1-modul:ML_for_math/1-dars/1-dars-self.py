def vec_add(v1,v2):
    if len(v1) == len(v2) :
        l = [ v1[i]+v2[i] for i in range(len(v1))]
        return l
    else:
        return "vektorlar uzunligi mos kelish kerak!"

print(vec_add([1,2,3],[1,2,3]))



def vec_scale(c,v):
    l=[]
    for n in v :
        l.append(n*c)
    return l

print(vec_scale(3,[2,6,3]))


    
        
def vec_sub(u,v):
   
   return vec_add(u,vec_scale(-1,v))

print(vec_sub([1,2,34],[2,3,4]))   
    