__author__ = 'dgxd4'
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    import settings

class parse:
    tree = ET.parse('sample.xml')

    root = tree.getroot()
    factors=[]
    facilities=[]
    resources=[]
    values=[]
    totals=[]
    costs = [0.12,2, 0.04,0.5,5,15,0.03,0.05,3,6,10]
    e = 322
    y=0
    w=0

# extract the factors and values from the "sample.XML" file

    for fac in root.iter('fac'):
        y=y+1
        for child in fac:
            resources.append(child.tag)
            factors.append(float(child.text))

    for value in root.iter('value'):
        w=w+1
        for child in value:
            facilities.append(child.tag)
            values.append(float(child.text))

    x=len(factors)
    z=len(values)
    y = x/z
    z=11

    for a in range(x):
        totals.append(0)


#calculate totals(*1000000)
    for d in range (z):
        totals[d] = (factors[d]*values[0]*e)/1000
    for d in range (z):
        totals[12+d] = (factors[12+d]*values[1]*e)/1000
    for d in range (z):
        totals[24+d] = (factors[24+d]*values[2]*e)/1000
    for d in range (z):
        totals[36+d] = (factors[36+d]*values[3]*e)/1000
    for d in range (z):
        totals[48+d] = (factors[48+d]*values[4]*e)/1000
    for d in range (z):
        totals[60+d] = (factors[60+d]*values[5]*e)/1000
    for d in range (z):
        totals[72+d] = (factors[72+d]*values[6]*e)/1000
    for d in range (z):
        totals[84+d] = (factors[84+d]*values[7]*e)/1000
    for d in range (z):
        totals[96+d] = (factors[96+d]*values[8]*e)/1000
    for d in range (z):
        totals[108+d] = (factors[108+d]*values[9]*e)/1000
    for d in range (z):
        totals[120+d] = (factors[120+d]*values[10]*e)/1000
    for d in range (z):
        totals[132+d] = (factors[132+d]*values[11]*e)/1000
    for d in range (z):
        totals[144+d] = (factors[144+d]*values[12]*e)/1000
    for d in range (z):
        totals[156+d] = (factors[156+d]*values[13]*e)/1000
    for d in range (z):
        totals[168+d] = (factors[168+d]*values[14]*e)/1000
    for d in range (z):
        totals[180+d] = (factors[180+d]*values[15]*e)/1000
    for d in range (z):
        totals[192+d] = (factors[192+d]*values[16]*e)/1000
    for d in range (z):
        totals[204+d] = (factors[204+d]*values[17]*e)/1000
    for d in range (z):
        totals[216+d] = (factors[216+d]*values[18]*e)/1000
    for d in range (z):
        totals[228+d] = (factors[228+d]*values[19]*e)/1000
    for d in range (z):
        totals[240+d] = (factors[240+d]*values[20]*e)/1000
    for d in range (z):
        totals[252+d] = (factors[252+d]*values[21]*e)/1000
    for d in range (z):
        totals[264+d] = (factors[264+d]*values[22]*e)/1000
    for d in range (z):
        totals[276+d] = (factors[276+d]*values[23]*e)/1000
    for d in range (z):
        totals[288+d] = (factors[288+d]*values[24]*e)/1000
    for d in range (z):
        totals[300+d] = (factors[300+d]*values[25]*e)/1000
    totals[11] = 0
    totals[23] = 0
    totals[35] = 0
    totals[47] = 0
    totals[59] = 0
    totals[71] = 0
    totals[83] = 0
    totals[95] = 0
    totals[107] = 0
    totals[119] = 0
    totals[131] = 0
    totals[143] = 0
    totals[155] = 0
    totals[167] = 0
    totals[179] = 0
    totals[191] = 0
    totals[203] = 0
    totals[215] = 0
    totals[227] = 0
    totals[239] = 0
    totals[251] = 0
    totals[263] = 0
    totals[275] = 0
    totals[287] = 0
    totals[299] = 0
    totals[311] = 0
    for d in range(z):
        totals[11] = totals[11] + (totals[d]*costs[d])
        totals[23] = totals[23] + (totals[12+d]*costs[d])
        totals[35] = totals[35] + (totals[24+d]*costs[d])
        totals[47] = totals[47] + (totals[36+d]*costs[d])
        totals[59] = totals[59] + (totals[48+d]*costs[d])
        totals[71] = totals[71] + (totals[60+d]*costs[d])
        totals[83] = totals[83] + (totals[72+d]*costs[d])
        totals[95] = totals[95] + (totals[84+d]*costs[d])
        totals[107] = totals[107] + (totals[96+d]*costs[d])
        totals[119] = totals[119] + (totals[108+d]*costs[d])
        totals[131] = totals[131] + (totals[120+d]*costs[d])
        totals[143] = totals[143] + (totals[132+d]*costs[d])
        totals[155] = totals[155] + (totals[144+d]*costs[d])
        totals[167] = totals[167] + (totals[156+d]*costs[d])
        totals[179] = totals[179] + (totals[168+d]*costs[d])
        totals[191] = totals[191] + (totals[180+d]*costs[d])
        totals[203] = totals[203] + (totals[192+d]*costs[d])
        totals[215] = totals[215] + (totals[204+d]*costs[d])
        totals[227] = totals[227] + (totals[216+d]*costs[d])
        totals[239] = totals[239] + (totals[228+d]*costs[d])
        totals[251] = totals[251] + (totals[240+d]*costs[d])
        totals[263] = totals[263] + (totals[252+d]*costs[d])
        totals[275] = totals[275] + (totals[264+d]*costs[d])
        totals[287] = totals[287] + (totals[276+d]*costs[d])
        totals[299] = totals[299] + (totals[288+d]*costs[d])
        totals[311] = totals[311] + (totals[300+d]*costs[d])

#divide the list of all totals into totals for each resource:
    totals1=[]
    d=0
    a=0
    for d in range(26):
        totals1.append(totals[a])
        a=a+12
        d=d+1

    totals2=[]
    d=0
    a=1
    for d in range(26):
        totals2.append(totals[a])
        a=a+12
        d=d+1

    totals3=[]
    d=0
    b=2
    for d in range(26):
        totals3.append(totals[b])
        b=b+12
        d=d+1

    totals4=[]
    d=0
    c=3
    for d in range(26):
        totals4.append(totals[c])
        c=c+12
        d=d+1

    totals5=[]
    d=0
    m=4
    for d in range(26):
        totals5.append(totals[m])
        m=m+12
        d=d+1

    totals6=[]
    d=0
    f=5
    for d in range(26):
        totals6.append(totals[f])
        f=f+12
        d=d+1

    totals7=[]
    d=0
    g=6
    for d in range(26):
        totals7.append(totals[g])
        g=g+12
        d=d+1

    totals8=[]
    d=0
    h=7
    for d in range(26):
        totals8.append(totals[h])
        h=h+12
        d=d+1


    totals9=[]
    d=0
    i=8
    for d in range(26):
        totals9.append(totals[i])
        i=i+12
        d=d+1

    totals10=[]
    d=0
    j=9
    for d in range(26):
        totals10.append(totals[j])
        j=j+12
        d=d+1

    totals11=[]
    d=0
    k=10
    for d in range(26):
        totals11.append(totals[k])
        k=k+12
        d=d+1

    totals12=[]
    d=0
    l=11
    for d in range(26):
        totals12.append(totals[l])
        l=l+12
        d=d+1

#calculate total resources:(in 1000000's)

    totalresources1=0
    d=0
    for d in range (26):
        totalresources1=totalresources1+totals1[d]
        d=d+1
    d=0
    totalresources2=0
    for d in range (26):
        totalresources2=totalresources2+totals2[d]
        d=d+1
    d=0
    totalresources3=0
    for d in range (26):
        totalresources3=totalresources3+totals3[d]
        d=d+1
    d=0
    totalresources4=0
    for d in range (26):
        totalresources4=totalresources4+totals4[d]
        d=d+1
    d=0
    totalresources5=0
    for d in range (26):
        totalresources5=totalresources5+totals5[d]
        d=d+1
    d=0
    totalresources6=0
    for d in range (26):
        totalresources6=totalresources6+totals6[d]
        d=d+1
    d=0
    totalresources7=0
    for d in range (26):
        totalresources7=totalresources7+totals7[d]
        d=d+1
    d=0
    totalresources8=0
    for d in range (26):
        totalresources8=totalresources8+totals8[d]
        d=d+1
    d=0
    totalresources9=0
    for d in range (26):
        totalresources9=totalresources9+totals9[d]
        d=d+1
    d=0
    totalresources10=0
    for d in range (26):
        totalresources10=totalresources10+totals10[d]
        d=d+1
    d=0
    totalresources11=0
    for d in range (26):
        totalresources11=totalresources11+totals11[d]
        d=d+1
    d=0
    totalresources12=0
    for d in range (26):
        totalresources12=totalresources12+totals12[d]
        d=d+1



    print(totals12)
    print(totalresources12)

                                                         