waktu50Cm = [175.2, 145.4, 175.3, 175.3, 175.2]
waktu60Cm = [197.2, 197.3, 197.3, 197.3, 197.5]
waktu40Cm = [149.4, 149.5, 149.2, 149.6, 149.1]
waktu30Cm = [119.6, 119.9, 119.6, 119.5, 119.7]


waktusensor50cm = [149.85 + 8 , 158.17+ 8, 166.5 + 8, 166.5+ 8, 149.85+ 8]
waktusensor60cm = [166.8 + 16, 166.8 + 16, 166.8 + 8, 166.8 + 8, 166.8 + 8]
waktusensor40cm = [133.2 + 8, 133.2 + 8, 141.5 + 8, 133.2 + 8, 133.2 + 8]

totalData = len(waktu50Cm)
himpunanPercepatanGravitasi = []
percepatanGravitasi = 0
for i in range(totalData):
    percepatanGravitasi = 0.4/(0.2*waktusensor40cm[i]*0.001 + 0.5*waktusensor40cm[i]*0.001*waktusensor40cm[i]*0.001)
    himpunanPercepatanGravitasi.append(percepatanGravitasi)

print(himpunanPercepatanGravitasi)