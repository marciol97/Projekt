import math as m
import matplotlib.pyplot as plt


#zadanie 1
#funckja 8

Tc=4
fs = 8000
f = 16
fi = 20

N=Tc*fs

x1=[]
y1=[]

def x(t):
    wynik = (1-t)*m.sin(2*m.pi*f*t+fi)*m.cos(4*m.pi*t)
    return wynik


for i in range(fs):
    x1.append(i/fs)
    y1.append(x(i/fs))

plt.plot(x1,y1)
plt.title("Zadanie 1")
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()



#zadanie 2
#funkcja 5

def y(t):
    wynik = (2*t*m.sin(0.5*t*m.pi)+1.5)*m.cos(9*m.pi*t+m.pi*t)
    return wynik


x2=[]
y2=[]
for i in range(fs):
    x2.append(i/fs)
    y2.append(y(i/fs))

plt.plot(x2,y2)
plt.title("Zadanie 2")
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()

def z(t):
    wynik = y(t)*x(t)+m.fabs(x(t)+2)*(m.pow(y(t), 2)+ 0.32)
    return wynik

x3=[]
y3=[]
for i in range(fs):
    x3.append(i/fs)
    y3.append(z(i/fs))

plt.plot(x3,y3)
plt.title("Zadanie 3")
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()

def v(t):
    wynik = m.sqrt(m.fabs(x(t)*z(t)+10))*(m.fabs(y(t))+1.2)*m.sin(2*m.pi*t)
    return wynik

x4=[]
y4=[]
for i in range(fs):
    x4.append(i/fs)
    y4.append(v(i/fs))

plt.plot(x4,y4)
plt.title("Zadanie 4")
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()

#zadanie 3
#funckja 4

def u(t):
    if t < 0.5 and t >=0:
        wynik = 0.9*m.sin(2*m.pi*t*8-m.pi/3)+m.log2(m.fabs(m.cos(7*m.pow(t, 2))+2.2))
    elif t < 1.9 and t >= 0.5:
        wynik = (m.sin(2*m.cos(4*m.pi*t)*m.pi*t))/(2*m.pow(t, 2)+1)
    elif t < 3.7 and t >= 1.9:
        wynik = m.pow((t-1.9), 2)-m.cos(13*t)
    elif t < 4.9 and t >= 3.7:
        wynik = 0.5*m.pow(t, 0.7)*m.sin(8*t)
    elif t < 6.4 and t >= 4.9:
        wynik = (2+m.sin(18*t))/(3+m.cos(28*t))
    return wynik

x5=[]
y5=[]
for i in range(fs):
    x5.append(i/fs)
    y5.append(u(i/fs))

plt.plot(x5,y5)
plt.title("Zadanie 5")
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()

#zadanie 4
#funckja 7

fs = 22050
Tc = 1

def b1(t):
    for h in range(1,2):
        wynik = (m.sin(m.pi*t*(2*m.pow(h, 2)+h)))/(2*m.pow(h, 2)*(2.5+m.cos(h*m.pi)-1))
    return wynik

x6=[]
y6=[]
for i in range(fs):
    x6.append(i/fs)
    y6.append(b1(i/fs))

plt.plot(x6,y6)
plt.title("Zadanie 6")
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()

def b2(t):
    for h in range(1,4):
        wynik = (m.sin(m.pi*t*(2*m.pow(h, 2)+h)))/(2*m.pow(h, 2)*(2.5+m.cos(h*m.pi)-1))
    return wynik

x7=[]
y7=[]
for i in range(fs):
    x7.append(i/fs)
    y7.append(b2(i/fs))

plt.plot(x7,y7)
plt.title("Zadanie 7")
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()

def b3(t):
    for h in range(1,20):
        wynik = (m.sin(m.pi*t*(2*m.pow(h, 2)+h)))/(2*m.pow(h, 2)*(2.5+m.cos(h*m.pi)-1))
    return wynik

x8=[]
y8=[]
for i in range(fs):
    x8.append(i/fs)
    y8.append(b3(i/fs))

plt.plot(x8,y8)
plt.title("Zadanie 8")
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()


#wykresy są 1 sekundowe sprawdzić to i uzupełnić pospisy osi i wykresów 