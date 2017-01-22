#!/usr/bin/env python3

import os
import re
import subprocess
import threading
import time

def hint(appname):
	try:
		appname = appname.split("/")
		appname = appname[-1]
	except:
		appname = appname.strip()
	#print (appname)
	uyari = "\"UYARI !\""
	mesaj = "\"Yüksek CPU kullanımı tespit edildi \n%s \"" %(appname)
	komut = "notify-send "+uyari+" "+mesaj+" -t 6000 -i hint" 
	if not appname in EXCEPTS:
		os.system(komut)

def check_prc():
	dizi = []
	bash_out = subprocess.check_output("ps aux",stderr=subprocess.STDOUT,shell=True)
	satirlar = bash_out.splitlines()
	for i in satirlar:
		i = re.sub('([\s]+)', ' ', str(i))
		dizi.append(i)
	dizi.pop(0) # ilk satırı sil
	for i in dizi:
		i = i.split(" ")
		cpu_usage,name = float(i[2]),str(i[10])
		if cpu_usage > HIGH:
			findapp = threading.Thread(target=hint(name))
			findapp.start()
			findapp.join()

def main():
	while 1:
		check_prc()
		time.sleep(5)
	return 0

HIGH = 90
EXCEPTS = ["firefox","chrome","chromium","java","inox"]

if __name__ == '__main__':
	main()
