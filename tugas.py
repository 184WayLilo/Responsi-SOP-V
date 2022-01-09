#Tugas NO.1 

RAM = int(input("total kapasita RAM Anda: (GB): "))
petaBit = int(input("total peta bit Anda: (kb): "))
kapRAM1 = int(input("Kapasitas RAM yang digunakan oleh sistem operasi: "))
kapRAM2 = int(input("Kapasitas RAM yang digunakan oleh program 1: "))
kapRAM3 = int(input("Kapasitas RAM yang digunakan oleh program 2: "))

embeh = RAM * 1024
PB = embeh / petaBit
r1 = embeh - kapRAM1
r2 = embeh - kapRAM2
r3 = embeh - kapRAM3

totramT = kapRAM1+kapRAM2+kapRAM3
totramS = embeh-totramT


print("total RAM anda adalah (mb):" , embeh)
print("total petabit anda adalah (kb):" , PB)
print("total RAM yang terpakai (mb):" , totramT)
print("total RAM anda tidak terpakai (mb):" , totramS)

