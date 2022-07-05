
def int32_to_ip(int32):
    b=[0,0,0,0]
    a=str(bin(int32)[2:])
    while len(a)!=32:
        a = "0"+a
    b[0]=str(int(a[:8],2))
    b[1]=str(int(a[8:16],2))
    b[2]=str(int(a[16:24],2))
    b[3]=str(int(a[24:32],2))
    c=".".join(b)

    return c