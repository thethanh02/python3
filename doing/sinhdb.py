import random

mamh = ['MH01', 'MH02', 'MH03', 'MH04', 'MH05', 'MH06', 'MH07']
masv = ['SV01', 'SV02', 'SV03', 'SV04', 'SV05', 'SV06', 'SV07', 'SV08', 'SV09', 'SV10', 'SV11', 'SV12', 'SV13', 'SV14', 'SV15', 'SV16', 'SV17', 'SV18', 'SV19', 'SV20']
nam = ['2020', '2021']
thang = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
ngay = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
lan = ['1', '2', '3']
# for i in range(7):
#     ma = '%02d'%(i)
#     print(f"'MH{i}', ")

for i in range(34):
    print(f"('{random.choice(masv)}', '{random.choice(mamh)}', {random.choice(lan)}),")