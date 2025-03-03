print("\n ==== PROGRAM KONVERSI TEMPERATUR ==== \n")

celcius = float(input("masukkan suhu dalam celcius : "))
print('suhu adalah ',celcius, 'celcius')

#Reamur
reamur = (4/5) * celcius
print('suhu dalam reamur adalah :',reamur,'reamur')

#fahrenheit
fahrenheit = (9/5) * celcius + 32
print('suhu dalam fahrenheit adalah :',fahrenheit,'fahrenheit')

#kelvin
kelvin = celcius + 273.15
print("suhu dalam kelvin adalah :",kelvin,"kelvin")

# Program dari fahrenheit ke kelvin

fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))
print("suhu adalah : ",fahrenheit,"fahrenheit")
celcius = (5/9)*(fahrenheit-32)
kelvin = celcius + 273.15

print("suhu dalam kelvin adalah", kelvin,"kelvin")


# Program dari kelvin ke fahrenheit

kelvin = float(input("Masukkan suhu dalam kelvin : "))
print('suhu adalah : ',kelvin,"kelvin")
celcius = kelvin - 273.15
fahrenheit =(9/5) * celcius + 32
print('suhu dalam fahrenheit adalah : ',fahrenheit,'fahrenheit')