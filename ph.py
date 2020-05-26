#!/usr/bin/env python3
import os
import re
import subprocess
import threading
import time


def hint(appname, usage):
    appname = appname.replace("'", "")
    '''  ' remove '''
    try:
        uygulama = appname.split("/")[-1]
        # print(uygulama)
    except ValueError:
        uygulama = appname.strip()
    uyari = "\"UYARI !\""
    mesaj = "\"Yüksek CPU kullanımı tespit edildi \n{} %{} \"".format(uygulama, usage)
    komut = "notify-send "+uyari+" "+mesaj+" -t 6000 -i hint"
    if uygulama not in EXCEPTS:
        os.system(komut)


def check_prc():
    # çalışan süreçler
    dizi = []
    bash_out = subprocess.check_output("ps aux", stderr=subprocess.STDOUT, shell=True)
    satirlar = bash_out.splitlines()
    for i in satirlar:
        dizi.append(re.sub(r'([\s]+)', ' ', str(i)))
    dizi.pop(0)
    # ilk satırı sil
    for i in dizi:
        sutunlar = i.split(" ")
        cpu_usage, name = float(sutunlar[2]), str(sutunlar[10])
        if cpu_usage > HIGH:
            findapp = threading.Thread(target=hint, args=(name, cpu_usage))
            findapp.start()


def main():
    while 1:
        check_prc()
        time.sleep(3)


HIGH = 90
EXCEPTS = ["firefox", "chrome", "chromium", "java", "inox", "QtWebEngineProcess"]

if __name__ == '__main__':
    main()
