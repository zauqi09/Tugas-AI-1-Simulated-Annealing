import random
import math

def probs(solusi,akhir,T):
	return 2.71828**(-(akhir-solusi))/T

def accurate(fa,fr):
    return (1-math.fabs((fa-fr)/fr))*100

def simulate(x1,x2):
	return -(math.fabs(math.sin(x1)*math.cos(x2)*math.exp(math.fabs(1-(math.sqrt(math.pow(x1,2)+(math.pow(x2,2)))/math.pi)))))

def varacak():
    return random.uniform(-10,10)

T0 = 1000000
T1 = 0
Tdingin = 0.9999
fr = -19.2085

x1,x2 = varacak(),varacak()
solusi = simulate(x1,x2)


while (T0>T1):
	y1,y2 = varacak(),varacak()
	akhir = simulate(y1,y2)
	if (solusi>akhir):
		solusi = akhir
		akurat = accurate(solusi,fr)
		print ("solusi :",solusi,", akurasi :",akurat,"%")
	elif (probs(solusi,akhir,T0)>random.random()):
		x1=y1
		x2=y2
	T0 *= Tdingin
