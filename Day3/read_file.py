fobj = open('r1.log','r')
wobj = open('r3.log','w')

s = fobj.read() # reading from r1.log file
wobj.write(s)   # write to r3.log file

fobj.close()
wobj.close()


with open('r1.log','r') as fobj:
    with open('r4.log','w') as wobj:
        L = fobj.readlines()
        for var in L:
            wobj.write(f"data -> {var}")


print("End of the line")