# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:02:31 2024

@author: Fairuz Maulidya
"""

print(''' =================
Nama: Fairuz Maulidya||
NIM: 064002300018    ||
=================''')

import datetime
import pytz

def my_decorator(inner):
    def inner_decorator():
        # Mendapatkan waktu UTC
        utc_now = datetime.datetime.now(pytz.utc)
        # Mengubah waktu UTC menjadi UTC+7
        jakarta_tz = pytz.timezone('Asia/Jakarta')
        jakarta_now = utc_now.astimezone(jakarta_tz)
        print("Timezone:", jakarta_tz.zone)
        print("Tanggal:", jakarta_now.strftime('%Y-%m-%d'))
        print("Waktu:", jakarta_now.strftime('%H:%M:%S.%f')[:-3])

        inner()

        # Menampilkan waktu setelah fungsi dijalankan
        utc_now = datetime.datetime.now(pytz.utc)
        jakarta_now = utc_now.astimezone(jakarta_tz)
        print("\nBerubah Menjadi")
        print("Tanggal:", jakarta_now.strftime('%Y-%m-%d'))
        print("Waktu:", jakarta_now.strftime('%H:%M:%S.%f')[:-3])

    return inner_decorator

@my_decorator
def decorated():
    print("After")

if __name__ == "__main__":
    decorated()
