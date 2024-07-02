import wave
import array

def wav_to_pcm(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        # Mendapatkan parameter dari file WAV
        sample_width = wav_file.getsampwidth()
        num_channels = wav_file.getnchannels()
        frame_rate = wav_file.getframerate()
        frames = wav_file.readframes(wav_file.getnframes())

    # Konversi data frame menjadi array PCM
    #print(frames)
    pcm_data = list(frames)
    #print(pcm_data)
    """
    print("Beberapa nilai pertama dari data PCM:", type(pcm_data))
    print("Lebar Sampel:", sample_width * 8, "bit")
    print("Jumlah Saluran:", num_channels)
    print("Laju BIngkai:", frame_rate, "Hz")
    print('\n')
    """
    return pcm_data, sample_width, num_channels, frame_rate

"""
#Contoh penggunaan:
wav_file_path = 'input.wav'
pcm_values, sample_width, num_channels, frame_rate = wav_to_pcm(wav_file_path)

# Menampilkan beberapa nilai pertama sebagai contoh
print("Beberapa nilai pertama dari data PCM:", type(pcm_values))
print("Lebar Sampel:", sample_width * 8, "bit")
print("Jumlah Saluran:", num_channels)
print("Laju BIngkai:", frame_rate, "Hz")

pcm_list = list(pcm_values)

print(pcm_list)




# Menyimpan data ke dalam file teks
with open('password.txt', 'w') as file:
    file.write(f'cipherkey: {cipherkey}\n')
    file.write(f'sample_width: {sample_width}\n')
    file.write(f'num_channels: {num_channels}\n')
    file.write(f'frame_rate: {frame_rate}\n')

"""

def pcm_to_wav(pcm_list, sample_width, num_channels, frame_rate, output_path):
    # Membuat objek wave dan mengonfigurasi parameter
    with wave.open(output_path, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(frame_rate)
        wav_file.writeframes(bytearray(pcm_list))
        
    #print(bytearray(pcm_list))
    
    

# Konversi array PCM ke format array.array
#pcm_data = array.array('h', pcm_values)

# Contoh penggunaan:
#output_wav_file_path = 'output.wav'
#pcm_to_wav(pcm_data, sample_width, num_channels, frame_rate, output_wav_file_path)
