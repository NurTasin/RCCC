def calcRes(band1,band2,multiplier,tolerance):
	band1=float(band1)
	band2=float(band2)
	multiplier=float(multiplier)
	tolerance=float(tolerance)
	ohm1=float(((band1*10)+band2)*multiplier)
	ohmMin=ohm1-(ohm1*tolerance)
	ohmMax=ohm1+(ohm1*tolerance)
	global ohm
	if (ohm1>=1000 and ohm1<1000000):
		global extension
		ohm=ohm1/1000
		ohmMin=ohmMin/1000
		ohmMax=ohmMax/1000
		extension=" k ohm"
	elif(ohm1<1000):
		ohm=ohm1
		ohmMax=ohmMax
		ohmMin=ohmMin
		extension=" ohm"
	elif(ohm1>=1000000 and ohm1<1000000000):
		ohm=ohm1/1000000
		ohmMax=ohmMax/1000000
		ohmMin=ohmMin/1000000
		extension=' M ohm'
	elif(ohm1>=1000000000):
		ohm=ohm1/1000000000
		ohmMax=ohmMax/1000000000
		ohmMin=ohmMin/1000000000
		extension=' G ohm'

	ohm=str("%.3f"%ohm)+extension
	ohmMax=str("%.3f"%ohmMax)+extension
	ohmMin=str("%.3f"%ohmMin)+extension
	devideby1000=str(float(ohm1)/1000)

	return (ohm,ohmMax,ohmMin,devideby1000)

