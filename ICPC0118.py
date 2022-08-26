t = int(input());
for test in range(t):
    day, month = [int(day) for day in input().split()]
    if month == 12:
        astro_sign = 'Nhan Ma' if (day < 22) else 'Ma Ket'
    elif month == 1:
        astro_sign = 'Ma Ket' if (day < 20) else 'Bao Binh'
    elif month == 2:
        astro_sign = 'Bao Binh' if (day < 19) else 'Song Ngu'
    elif month == 3:
        astro_sign = 'Song Ngu' if (day < 21) else 'Bach Duong'
    elif month == 4:
        astro_sign = 'Bach Duong' if (day < 20) else 'Kim Nguu'
    elif month == 5:
        astro_sign = 'Kim Nguu' if (day < 21) else 'Song Tu'
    elif month == 6:
        astro_sign = 'Song Tu' if (day < 21) else 'Cu Giai'
    elif month == 7:
        astro_sign = 'Cu Giai' if (day < 23) else 'Su Tu'
    elif month == 8:
        astro_sign = 'Su Tu' if (day < 23) else 'Xu Nu'
    elif month == 9:
        astro_sign = 'Xu Nu' if (day < 23) else 'Thien Binh'
    elif month == 10:
        astro_sign = 'Thien Binh' if (day < 23) else 'Thien Yet'
    elif month == 11:
        astro_sign = 'Thien Yet' if (day < 23) else 'Nhan Ma'
    print(astro_sign)