det gen(ic):
    ac,r,t =[],['r'+str(i) for i in range 8,],0
    for l in ic:
        r,e= map(str.strip, l.split("="))
