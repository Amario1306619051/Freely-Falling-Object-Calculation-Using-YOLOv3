waktu50Cm = [176.6, 176.5, 177.3, 176.7, 177.4]
waktu60Cm = [200.8, 201, 200.7, 201.3, 201.7]
waktu40Cm = [147.8, 148.3, 147.8, 148.4, 148.2]
waktu30Cm = [117.2, 117.2, 117.5, 117.3, 116.9]


waktusensor50cm = [149.85 + 8 , 158.17+ 8, 166.5 + 8, 166.5+ 8, 149.85+ 8]
waktusensor60cm = [166.8 + 16, 166.8 + 16, 166.8 + 8, 166.8 + 8, 166.8 + 8]
waktusensor40cm = [133.2 + 8, 133.2 + 8, 141.5 + 8, 133.2 + 8, 133.2 + 8]

totalData = len(waktu50Cm)
himpunanPercepatanGravitasi = []
percepatanGravitasi = 0
for i in range(totalData):
    percepatanGravitasi = 0.6/(0.2*waktu60Cm[i]*0.001 + 0.5*waktu60Cm[i]*0.001*waktu60Cm[i]*0.001)
    himpunanPercepatanGravitasi.append(percepatanGravitasi)

print(himpunanPercepatanGravitasi)