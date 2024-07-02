def matriks_plainteks(pcm_list):
    blok_panjang = 16  # Panjang blok, sesuaikan dengan kebutuhan (misalnya, 16 untuk AES)

    # Membagi list PCM menjadi blok-blok dengan panjang blok yang diinginkan
    blok_pcm = [pcm_list[i:i+blok_panjang] for i in range(0, len(pcm_list), blok_panjang)]

    # Mengonversi setiap blok PCM menjadi matriks 4x4
    matriks_3d = []
    for blok in blok_pcm:
        matriks_4x4 = [blok[i:i+4] for i in range(0, len(blok), 4)]
        matriks_3d.append(matriks_4x4)

    return matriks_3d

def matriks_cipherteks(pcm_list):
    blok_panjang = 16  # Panjang blok, sesuaikan dengan kebutuhan (misalnya, 16 untuk AES)

    # Membagi list PCM menjadi blok-blok dengan panjang blok yang diinginkan
    blok_pcm = [pcm_list[i:i+blok_panjang] for i in range(0, len(pcm_list), blok_panjang)]

    # Mengonversi setiap blok PCM menjadi matriks 4x4
    matriks_3d = []
    for blok in blok_pcm:
        matriks_4x4 = [blok[i:i+4] for i in range(0, len(blok), 4)]
        matriks_3d.append(matriks_4x4)

    return matriks_3d

