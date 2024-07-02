import steganografi as st
import invsubbytes as isb
import invshiftrows as isr
import invmixcolumn as imx
import roundkey1 as rk
import padding as pg
import matriks as mr
import numpy as np
import pcm
import os

     
# Membaca nilai cipherteks dari audio.wav


with open('password.txt', 'r') as file:
    lines = file.readlines()

    # Mendapatkan nilai-nilai yang sesuai
    key = lines[0].strip() if lines and lines[0] else None
    sample_width = int(lines[1]) if len(lines) > 1 and lines[1].strip().isdigit() else None
    num_channels = int(lines[2]) if len(lines) > 2 and lines[2].strip().isdigit() else None
    frame_rate = int(lines[3]) if len(lines) > 3 and lines[3].strip().isdigit() else None
    num_samples = int(lines[4]) if len(lines) > 4 and lines[4].strip().isdigit() else None

cipher_text = st.recover_original_pcm_from_image('cipher.png',num_samples)


#Konversi string cipherteks ke matriks
cipherteks = mr.matriks_cipherteks(cipher_text)

print('\n Cipherteks : ')
print(cipher_text)


#Transpose membentuk matriks plainteks
cipherteks = [list(map(list, zip(*mat))) for mat in cipherteks]


 
# Inisialisasi matriks 4x4 untuk cipherkey
cipherkey = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        cipherkey[j][i] =ord(key[i * 4 + j])

print('\n Cipherkey :')
for row in cipherkey:
    print(row)
    
#Ekspansi Kunci 
rkey = rk.expand(cipherkey)

print('\nTotal Cipherteks : ',len(cipherteks))

plainteks = [[] for _ in range(len(cipherteks))]

itera = 0

for ciper in cipherteks:
    
    epoch = 0
    
    #Round Key-0
    rk.addRoundKey(ciper,rkey[10-epoch])
    
    #Roundkey-0
    print(ciper)
    
    state = ciper
    
    #Operasi Invers ShiftRows
    isr.shiftRowsInv(state)
    print('\n Shifted '+ str(epoch) + ' : ')
    print(state)
    
    #operasi Invers SubBytes
    isb.subBytesInv(state)
    print('\n SubBytes-' + str(epoch) + ' : ')
    print(state)
    
    #Looping Nr-1
    while(epoch < 9):
        #Iterasi Nr-1
        epoch = epoch + 1
        rk.addRoundKey(state,rkey[10-epoch])
        
        #Operasi Invers MixColumn
        imx.mixcolInv(state)
        print('\n Mixed '+ str(epoch) + ' : ')
        print(state)
        
        #Operasi Invers ShiftRows
        isr.shiftRowsInv(state)
        print('\n Shifted '+ str(epoch) + ' : ')
        print(state)
        
        #Operasi Invers SubBytes
        isb.subBytesInv(state)
        print('\n SubBytes-' + str(epoch) + ' : ')
        print(state)
    
    #Looping Iterasi epoch terakhir
    epoch = epoch + 1
    
    #AddRoundKey
    rk.addRoundKey(state,rkey[10-epoch])
    
    #Plainteks ke-itera
    print('\n Plain ke-' + str(itera) + ' : ')    
    print(state)
    
    plainteks[itera] = [[state[j][i] for j in range(4)] for i in range(4)]
    
    #Iterasi plainteks
    itera=itera+1
    



plain_text = [elem for plain in plainteks for row in plain for elem in row]



plain_text = pg.custom_unpadding(plain_text)

print('\n Plainteks Text '+' : ')
print(plain_text)

pcm.pcm_to_wav(plain_text, sample_width, num_channels, frame_rate,'plainteks.wav')


