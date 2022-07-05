def ip_to_num(ip):
    a = ip.split('.')
    for i in range(len(a)):
        a[i] = str(bin(int(a[i])))[2:]
    for x in range(len(a)):
        while len(a[x]) !=8:
            a[x] = "0"+a[x]    
    b=int("".join(a),2)

    return b

ip_to_num('192.168.1.1')



def num_to_ip(num):
    b=[0,0,0,0]
    a=str(bin(num)[2:])
    while len(a)!=32:
        a = "0"+a
    b[0]=str(int(a[:8],2))
    b[1]=str(int(a[8:16],2))
    b[2]=str(int(a[16:24],2))
    b[3]=str(int(a[24:32],2))
    c=".".join(b)

    return c


num_to_ip(2 ** 32 - 1)