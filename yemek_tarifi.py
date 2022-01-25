# -*- coding: utf-8 -*-
import pymysql.cursors
db = pymysql.connect(
    host ="localhost",
    user = "root",
    password ="",
    db="yemek_tarif",
    charset="utf8",
    cursorclass =pymysql.cursors.DictCursor)


baglanti = db.cursor()
baglanti.execute('SELECT * FROM yemek')
yemekler = baglanti.fetchall()

for i in yemekler:
    print("Yemek Ad: " + i['yemek_ad'] + " *** " + "Malzeme: " + i['malzeme'] + "Tarifi " + " *** " + i['tarif'])








