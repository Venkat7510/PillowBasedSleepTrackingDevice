import serial
from datetime import timedelta 
import datetime
import csv
port="/dev/ttyUSB0"
ser=serial.Serial(port, baudrate=9600)
c=1

while(True):
	newdata=ser.readline().decode("utf-8")
	#print(newdata)
	vals=newdata.split('/')
	current_time = datetime.datetime.now().replace(microsecond=0)
	chkpres=int(vals[1])
	if(chkpres>500 and c==1):
		dt1 = datetime.datetime.now().replace(microsecond=0)
		c=2
		print("_________________________________________________________________")
		print("_____________START TIME READING_________________________________")
		sleep=0
	if(chkpres<500 and c==2):
		dt2 = datetime.datetime.now().replace(microsecond=0)
		dif=dt2-dt1
		print(dif)
		t=str(dif).split(':')

		total_minutes= int(t[0])*60+int(t[1])*1 +int(t[2])/60
		rem=int((total_minutes-25)/90)
		if(total_minutes>25):
			t2=dif-timedelta(minutes = 0)
			sl=str(dif).split(':')
			sleephr=sl[0]
		else:
			sleephr=0			

		c=1
		#print(t)
		print("   ")
		print("______________________________________________________")
		print("Total Minutes: "+str(total_minutes))
		print("Sleep Hour: "+str(sleephr))
		print("REM CYCLE: "+str(rem))
		print("______________ENDING TIME READ_________________________")
		print("___________________________________________________________")
		print("  ")
		sleep=1
		
		with open(r'dta.csv','a', newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([current_time,sleep,vals[1],vals[2],vals[3],vals[4],sleephr,rem])


	print(current_time,vals)


    