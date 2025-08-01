det gen(ic):
    ac,r,t =[],['r'+str(i) for i in range 8,],0
    for l in ic:
        r,e= map(str.strip, l.split("="))
        for op ,ins in [('+','ADD'),('-','SUB'),('*','MUL')]:
            if op in e:
                a,b = map(str.strip,e.split(op))
                ac.append(f"{ins} {r[t%8]},{a},{b}")
                break
