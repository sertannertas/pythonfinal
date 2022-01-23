# -*- coding: utf-8 -*-
import pymysql.cursors
db = pymysql.connect(
    host ="localhost",
    user = "root",
    password ="",
    db="pythonveritabani",
    charset="utf8",
    cursorclass =pymysql.cursors.DictCursor)


baglanti = db.cursor()
baglanti.execute('SELECT * FROM yemekler')
yemekler = baglanti.fetchall()

for i in yemekler:
    print("Yemek Adi: " + i['yemek_adi'] + " --- " + " Yemek Malzemesi: " + i['yemek_malzeme'] + " Yemek Tarifi " + " --- " + i['yemek_tarif'])








