waktu50Cm = [175.2, 145.4, 175.3, 175.3, 175.2]
waktu60Cm = [197.2, 197.3, 197.3, 197.3, 197.5]
waktu40cm = [149.4, 149.5, 149.2, 149.6, 149.1]
waktu30cm = [119.6, 119.9, 119.6, 119.5, 119.7]

totalData = len(waktu50Cm)
himpunanPercepatanGravitasi = []
percepatanGravitasi = 0
for i in range(totalData):
    percepatanGravitasi = 0.6/(0.2*waktu60Cm[i]*0.001 + 0.5*waktu60Cm[i]*0.001*waktu60Cm[i]*0.001)
    himpunanPercepatanGravitasi.append(percepatanGravitasi)

print(himpunanPercepatanGravitasi)