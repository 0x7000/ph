#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# ccc GNU GPLv2 ccc

import subprocess,os,re,time

def hint(appname):
	try:
		appname = appname.split("/")
		appname = appname[-1]
	except:
		appname = appname.strip()
	uyari = "\"UYARI !\""
	mesaj = "\"Yüksek CPU kullanımı tespit edildi \n%s \"" %(appname)
	komut = "notify-send "+uyari+" "+mesaj+" -t 6000 -i hint" 
	print komut
	os.system(komut)

def check_prc():
	dizi = []
	cmd = "ps aux"
	bash_out = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
	satirlar = bash_out.splitlines()
	for i in satirlar:
		i = re.sub('([\s]+)', ' ', i)
		dizi.append(i)
	dizi.pop(0)
	for i in dizi:
		i = i.split(" ")
		i,name = float(i[2]),str(i[10])
		if i > YUKSEK:
			os.system("clear")
			hint(name)
			#print "%f %s" %(i,name) 

def main():
	while 1:
		check_prc()
		time.sleep(10)
	return 0

YUKSEK = 80

if __name__ == '__main__':
	main()
	
