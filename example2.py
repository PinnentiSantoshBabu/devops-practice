det gen(ic):
    ac,r,t =[],['r'+str(i) for i in range 8,],0
    for l in ic:
        r,e= map(str.strip, l.split("="))
        for op ,ins in [('+','ADD'),('-','SUB'),('*','MUL')]:
            if op in e:
                a,b = map(str.strip,e.split(op))
                ac.append(f"{ins} {r[t%8]},{a},{b}")
                break
        else:
            ac.append(f"MOV {r[t%8]},{e}")
        ac.append(f"MOV {r} {r[t%8]}")
        t+=1
    return ac
ic=["t1=a+b","t2=c+d","t3=t1*t2"]
for line in gen(ic):
    print(line)
