def persistance(angka):   

   
    kali = 1
    jumlah = 0
    total = []

    if 0 < angka < 10:
            print(f'{angka} is already digit')

    elif angka < 0:
            print(f'please input positive number only')


    else:
        total.append(1)
        b = True
        while b == True:
            for i in [int(i) for i in str(angka)]:
#                 total.append(1)
                kali *= i
            if kali < 9:
                b = False
            else:
                total.append(1)


            angka= kali
            kali =1

        print(sum(total))
persistance(39)
persistance(999)
persistance(4)
persistance(-12)
