from PIL import Image

def pcm_to_binary(pcm_list):
    binary_data = ''.join(format(abs(sample), '08b') for sample in pcm_list)
    return binary_data

def binary_to_pcm(binary_data):
    pcm_list = [int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)]
    return pcm_list

def hide_pcm_in_image(image_path, pcm_list, output_path):
    binary_data = pcm_to_binary(pcm_list)

    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    print('\nUkuran Piksel penampung : ',len(pixels))
    print('\nUkuran PCm yang akan disisipkan',len(binary_data))

    if len(binary_data) > len(pixels):
        raise ValueError("Cipherteks terlalu besar untuk gambar ini")

    for i in range(len(binary_data)):
        pixel_value = list(pixels[i])
        pixel_value[-1] = int(format(pixel_value[-1], '08b')[:-1] + binary_data[i], 2)
        pixels[i] = tuple(pixel_value)

    img.putdata(pixels)
    img.save(output_path)

def recover_pcm_from_image(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_data = ''.join(format(pixel[-1], '08b')[-1] for pixel in pixels)
    pcm_list = binary_to_pcm(binary_data)

    return pcm_list



def recover_original_pcm_from_image(image_path,num_samples):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_data = ''.join(format(pixel[-1], '08b')[-1] for pixel in pixels)
    original_pcm_list = [int(binary_data[i:i+8], 2) for i in range(0, num_samples*8, 8)]

    return original_pcm_list


"""
# Contoh penggunaan
pcm_list = [-1, 2, -3, 4, -5, 6, -7, 8, 9, 10]
image_path = 'picture.png'
output_image_path = 'gambar_hasil_steganografi.png'

# Menyisipkan data PCM ke dalam gambar
hide_pcm_in_image(image_path, pcm_list, output_image_path)

# Mengambil data PCM dari gambar
recovered_pcm = recover_pcm_from_image(output_image_path)



recovered_original_pcm = recover_original_pcm_from_image(output_image_path, 10)


print("Data PCM yang Dikembalikan:", recovered_pcm)
print("Ukuran pixels recover : ",len(recovered_pcm))
print("Data PCM Sblmnya:", pcm_list)
print("Data PCM Asli:", recovered_original_pcm)
"""