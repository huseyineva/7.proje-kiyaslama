from ast import Bytes
from io import BytesIO
import re
from tkinter import Image
from PIL import Image
import requests

class Futbolcu():
    def __init__(self, isim, hiz, sut, pas, top_surme, defans, fizik):
        self.isim = isim
        self.hiz = hiz
        self.sut = sut
        self.pas = pas
        self.top_surme = top_surme
        self.defans = defans
        self.fizik = fizik

    def yetenek_hazirla(self):
        return ','.join([           
            str(self.hiz),
            str(self.sut),
            str(self.pas),
            str(self.top_surme),
            str(self.defans),
            str(self.fizik),
            str(self.hiz)
        ])
        

    def yetenek_gorsellestir(self):

        grafik_URL = 'https://image-charts.com/chart'

        payload = {
            'chco': '3092de',
            'chd': 't:' + self.yetenek_hazirla(),
            'chdl': self.isim,
            'chdlp': 'b',
            'chs': '480x480',
            'cht': 'r',
            'chtt': 'Futbolcu Özellikleri',
            'chl': 'hiz|sut|pas|top_surus|defans|fizik',
            'chx1':'0: |0|20|40|60|80|100',
            'chxt':'x',
            'chxr':'0,0.0,100.0',
            'chm':'B,AAAAAABB,0,0,0'
        }
        response = requests.post(grafik_URL, data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()  

    def yetenek_kiyaslama(self, hedef_futbolcu):
        grafik_URL = 'https://image-charts.com/chart'

        payload = {
            'chco': '3092de,027182',
            'chd': 't:' + self.yetenek_hazirla() + '|' + hedef_futbolcu.yetenek_hazirla(),
            'chdl': self.isim + '|' + hedef_futbolcu.isim,
            'chdlp': 'b',
            'chs': '480x480',
            'cht': 'r',
            'chtt': 'Futbolcu Özellikleri',
            'chl': 'hiz|sut|pas|top_surus|defans|fizik',
            'chx1':'0: |0|20|40|60|80|100',
            'chxt':'x',
            'chxr':'0,0.0,100.0',
            'chm':'B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0'
        }
        response = requests.post(grafik_URL, data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()   

messi = Futbolcu('Messi', 85, 92, 91, 95, 38, 65)
ronaldo = Futbolcu('Ronaldo', 89, 93, 81, 89, 35, 77)    

print(ronaldo.yetenek_kiyaslama(messi))