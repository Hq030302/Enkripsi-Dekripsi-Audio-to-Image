# padding.py
def custom_padding(data):
    padding_value = 16 - (len(data) % 16)
    if padding_value != 16:  # Hanya lakukan padding jika diperlukan
        data += [padding_value] * padding_value
    return data

def custom_unpadding(data):
    padding_value = data[-1]
    if padding_value > 0 and all(value == padding_value for value in data[-padding_value:]):
        return data[:-padding_value]
    else:
        # Padding tidak sesuai, kembalikan seperti semula
        return data

# Contoh penggunaan
#original_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16]
#padded_data = custom_padding(original_data)

#print("Original Data:", original_data)
#print("Padded Data:", padded_data)



#print("Padded Data:", padded_data)

#unpadded_data = custom_unpadding(padded_data)



























"""

def custom_padding(data):
    if len(data) < 16:
        padding_length = 16 - len(data)
        padding_value = ' '*padding_length #bytes([padding_length]) * padding_length
        padded_data = data + padding_value
    elif (len(data) > 16 and (len(data)%16!=0)):
        # Pilihan lain untuk padding jika data lebih dari satu blok
        padding_length = 16 - (len(data) % 16)
        padding_value = ' '*padding_length#bytes([padding_length]) * padding_length
        padded_data = data + padding_value
    elif (len(data) >= 16 and len(data)%16==0):
        # Jika panjang data sudah sesuai dengan panjang blok
        padded_data = data

    return padded_data

def custom_unpadding(padded_data):
    #padding_length = ord(padded_data[-1])
    unpadded_data = padded_data.rstrip()
    return unpadded_data

# Contoh penggunaan
#padded_string = "Hello World\x05\x05\x05\x05\x05"
#unpadded_string = custom_unpadding(padded_string)

# Contoh penggunaan
block_size = 16
short_data = 'Halo'
long_data = 'Halo Semua Saya Maliky Syailendra'
normal_data = 'MalikySyailendraMalikySyailendra'

# Padding
padded_short_data = custom_padding(short_data)
padded_long_data = custom_padding(long_data)
padded_normal_data = custom_padding(normal_data)
print(f'Padded Short Data: {len(padded_short_data)}')
print(f'Padded Long Data: {len(padded_long_data)}')
print(f'Padded Long Data: {len(padded_normal_data)}')

#hex_representation = padded_long_data.decode('utf-8')
#print(type(hex_representation))

# Unpadding
unpadded_short_data = custom_unpadding(padded_short_data)
unpadded_long_data = custom_unpadding(padded_long_data)

print(f'Unpadded Short Data: {unpadded_short_data}')
print(f'Unpadded Long Data: {unpadded_long_data}')


"""