# Ganjoor !!
import sqlite3
import random
#.................................................
#این تابع جهت درست فرم گرفتن کارکتر ها و کلمات فارسی ایجاد شده
import arabic_reshaper
from bidi.algorithm import get_display
def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted
#.................................................
def ganjoor_poet() :
    id_column = 1 #جهت درست کردن ستون ها با ترتیب عددی صحیح است و استفاده در دیکشنری
    for i in range(1 , 1000) : # جهت خواندن اسامی تمام شعرا
        conn = sqlite3.connect('ganjoor.db')
        cur = conn.cursor()
        cur.execute("SELECT name FROM poet WHERE id = ?", (i,))# برای اینکه هر بار ستر جدیدی را بخواند ، از آی دی استفاده کردیم
        st = str(cur.fetchone())#تبدیل هرچی که هست به رشته برای قابل قبول بودن در تابع عربیک
        if st != 'None':
            dictionary_sample = {
                id_column : convert(st)
            }
            id_column+=1
            print(dictionary_sample)
        i+=1 

print("Hello , Welcome To Ganjoor\n")
print("Would you like to see the list of poets? (Yes / No)")
see_poet = input()
if see_poet == 'yes' or see_poet == 'Yes' or see_poet == 'Ye' or see_poet == 'ye' or see_poet == 'y' or see_poet == 'Y' :
    ganjoor_poet()
else :
    print("Do you want to enter the name yourself? (Yes / No)")
    select_poet = input()
    if select_poet == 'yes' or select_poet == 'Yes' or select_poet == 'Ye' or select_poet == 'ye' or select_poet == 'y' or select_poet == 'Y' :
        poet = input("poet's name : ")
    else :
        print("GoodBye !")