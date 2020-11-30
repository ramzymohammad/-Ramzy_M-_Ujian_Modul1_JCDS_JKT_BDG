def find_short():

    kalimat = input('masukkan kalimat anda: ').split()

    panjang = []
    for i in kalimat:
        panjang.append(len(i))



    kecil = 10000000000
    for k in panjang:
        if k < kecil:
            kecil = k

    # print(kalimat)
    # print(panjang)
    # print(kecil)

    print(f'The shortest word has {kecil} char(s)')

find_short()
