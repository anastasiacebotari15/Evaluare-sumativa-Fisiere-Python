f,m,n,q,z,r=open('input.txt', 'r'),[],[],0,[]
for i in f:m.append(i.rstrip().split(' ')); r.append(i)
for i in m:
    print(*i)
with open('rezerva.txt', 'w') as f:
    f.writelines(rezerva)
print('/n')
for i in m:
    n.append(str(round(sum([float(a) for x in i[0:2]])/len(i[0:2]),2))+' '+i[-1])
with open('output.txt', 'a') as f:
    for i in n:
        q+=1
        print(q,i)
        f.write(str(c)+' '+i+'/n')