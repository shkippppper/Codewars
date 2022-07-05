import cmath


def tankvol(h, d, vt):
    length = vt/(3.14*(d/2)**2)
    theta = cmath.cos((d/2-h)/(d/2))
    # section_area 
    print(theta)



tankvol(5, 7, 3848)


