import steganografi as st
import subbytes as sb
import shiftrows as sr
import mixcolumn as mx
import roundkey1 as rk
import padding as pg
import matriks as mr
import numpy as np
import pcm
import os

#Input
plain_text = input('Masukkan audio yang akan dienkripsi (harus .wav!): ')

while True:    
    key = input('Masukkan kunci (harus panjangnya 16!) : ')
    if len(key)==16:
        break
    else:
        os.system('cls')
        print('Panjang kunci harus 16 karakter. Coba lagi!')
        
plain_text = f'{plain_text}.wav'

plain_text, sample_width, num_channels, frame_rate = pcm.wav_to_pcm(plain_text)

print('\n Plainteks Real : ')
print(plain_text)

masuk = []



# Menyimpan data ke dalam file teks
with open('password.txt', 'w') as file:
    file.write(f'{key}\n')
    file.write(f'{sample_width}\n')
    file.write(f'{num_channels}\n')
    file.write(f'{frame_rate}\n')
    file.write(f'{len(plain_text)}\n')



#Padding PlainText
plain_text = pg.custom_padding(plain_text)

#Konversi Plainteks dan CIpherkey ke Matriks

plainteks = mr.matriks_plainteks(plain_text)


#Transpose membentuk matriks plainteks
plainteks = [list(map(list, zip(*mat))) for mat in plainteks]

cipherkey = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        cipherkey[j][i] =ord(key[i * 4 + j])

print('\nCipherkey :')
for row in cipherkey:
    print(row)

#Ekspansi Kunci 
rkey = rk.expand(cipherkey)

print('\nPanjang Iterasi Plainteks : ',len(plainteks))


cipherteks = [[] for _ in range(len(plainteks))]


itera = 0
for plain in plainteks:
    print("\nIterasi ke-",itera)
    epoch = 0
    
    #Round Key-0
    rk.addRoundKey(plain,rkey[epoch])
    
    print('\n After RoundKey : ')
    print(plain)
    
    state = plain
    
    while(epoch < 9):
        #Operasi SubBytes
        sb.subBytes(state)
        print('\n SubBytes-' + str(epoch) + ' : ')
        print(state)
        
        #Operasi ShiftRows
        sr.shiftRows(state)
        print('\n Shifted '+ str(epoch) + ' : ')
        print(state)
        
        #Operasi MixColumn
        mx.mixcol(state)
        print('\n Mixed '+ str(epoch) + ' : ')
        print(state)
        
        epoch = epoch + 1
        
        #AddRoundKey-epoch
        rk.addRoundKey(state,rkey[epoch])
    
    #Operasi SubBytes final
    sb.subBytes(state)
    print('\n SubBytes-' + str(epoch) + ' : ')
    print(state)
    
    #Operasi ShoftRows
    sr.shiftRows(state)
    print('\n Shifted '+ str(epoch) + ' : ')
    print(state)
    
    epoch = epoch+1
    
    rk.addRoundKey(state,rkey[epoch])
    
    print('\n Cipherteks ke-' + str(itera) + ' : ')    
    print(state)
    
    cipherteks[itera] = [[state[j][i] for j in range(4)] for i in range(4)]
    itera=itera+1



cipher_text = [elem for cipher in cipherteks for row in cipher for elem in row]

pcm.pcm_to_wav(cipher_text, sample_width, num_channels, frame_rate,'cipherteks.wav')
#cs.konversi_pcm(cipher_text)

print('\n Cipherteks '+' : ')

print(cipher_text)

print('\nUkuran plainteks : ',len(plain_text))
print('\nUkuran cipherteks : ',len(cipher_text))

st.hide_pcm_in_image('input.png',cipher_text,'cipher.png')

print('\n Embedding selesai :) !')





