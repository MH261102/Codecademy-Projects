#Temperature Conversions
def celsius_to_fahrenheit(celsius):
    return (1.8 * celsius) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

#Volume Conversions
def litres_to_gallons(litres):
    return litres * 0.264172
def gallons_to_litres(gallons):
    return gallons * 3.78541
def millilitres_to_fluid_ounces(millilitres):
    return millilitres * 0.033814
def fluid_ounces_to_millilitres(fluid_ounces):
    return fluid_ounces * 29.5735

#Length Conversions
def metres_to_feet(metres):
    return metres * 3.28084
def feet_to_metres(feet):
    return feet * 0.3048
def centimetres_to_inches(centimetres):
    return centimetres * 0.393701
def inches_to_centimetres(inches):
    return inches * 2.54
def kilometres_to_miles(kilometres):
    return kilometres * 0.621371
def miles_to_kilometres(miles):
    return miles * 1.60934

#Weight Conversion
def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462
def pounds_to_kilograms(pounds):
    return pounds * 0.453592
def grams_to_ounces(grams):
    return grams * 0.035274
def ounces_to_grams(ounces):
    return ounces * 28.3495

#Speed Conversions
def kmh_to_mph(kmh):
    return kmh * 0.621371
def mph_to_kph(mph):
    return mph * 1.60934

#Area Conversions
def m2_to_ft2(m2):
    return m2 * 10.7639
def ft2_to_m2(ft2):
    return ft2 * 0.092903
def acres_to_m2(acres):
    return acres * 4046.86
def m2_to_acres(m2):
    return m2 * 0.000247105

#Time Conversions
def min_to_secs(min):
    return min * 60
def secs_to_min(secs):
    return secs / 60
def hours_to_min(hours):
    return hours * 60
def min_to_hours(min):
    return min / 60

print ("What type of unit do you want to convert?")
print ("1 = Temperature")
print ("2 = Volume")
print ("3 = Length")
print ("4 = Weight")
print ("5 = Speed")
print ("6 = Area")
print ("7 = Time")
unit_type = input("Type: ")

if unit_type == "1":
    print ("Which conversion do you want to do?")
    print ("1 = Celsius to Fahrenheit")
    print ("2 = Fahrenheit to Celsius")
    print ("3 = Celsius to Kelvin")
    print ("4 = Kelvin to Celsius")
    conversion_type = input("Conversion type: ")

    if conversion_type == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit")
    elif conversion_type == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius")
    elif conversion_type == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} degrees Celsius is {kelvin} Kelvin")
    elif conversion_type == "4":
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin} Kelvin is {celsius} degrees Celsius")
    else:
        print("Invalid conversion type")

elif unit_type == "2":
    print("Which conversion do you want to do?")
    print("1 = Litres to Gallons")
    print("2 = Gallons to Litres")
    print("3 = Millilitres to Fluid Ounces")
    print("4 = Fluid Ounces to Millilitres")
    conversion_type = input("Conversion type: ")

    if conversion_type == "1":
        litres = float(input("Enter volume in Litres: "))
        gallons = litres_to_gallons(litres)
        print(f"{litres} Litres is {gallons} Gallons")
    elif conversion_type == "2":
        gallons = float(input("Enter volume in Gallons: "))
        litres = gallons_to_litres(gallons)
        print(f"{gallons} Gallons is {litres} Litres")
    elif conversion_type == "3":
        millilitres = float(input("Enter volume in Millilitres: "))
        fluid_ounces = millilitres_to_fluid_ounces(millilitres)
        print(f"{millilitres} Millilitres is {fluid_ounces} Fluid Ounces")
    elif conversion_type == "4":
        fluid_ounces = float(input("Enter volume in Fluid Ounces: "))
        millilitres = fluid_ounces_to_millilitres(fluid_ounces)
        print(f"{fluid_ounces} Fluid Ounces is {millilitres} Millilitres")
    else:
        print("Invalid conversion type")

elif unit_type == "3":
    print("Which conversion do you want to do?")
    print("1 = Metres to Feet")
    print("2 = Feet to Metres")
    print("3 = Centimetres to Inches")
    print("4 = Inches to Centimetres")
    print("5 = Kilometres to Miles")
    print("6 = Miles to Kilometres")
    conversion_type = input("Conversion type: ")

    if conversion_type == "1":
        metres = float(input("Enter length in Metres: "))
        feet = metres_to_feet(metres)
        print(f"{metres} Metres is {feet} Feet")
    elif conversion_type == "2":
        feet = float(input("Enter length in Feet: "))
        metres = feet_to_metres(feet)
        print(f"{feet} Feet is {metres} Metres")
    elif conversion_type == "3":
        centimetres = float(input("Enter length in Centimetres: "))
        inches = centimetres_to_inches(centimetres)
        print(f"{centimetres} Centimetres is {inches} Inches")
    elif conversion_type == "4":
        inches = float(input("Enter length in Inches: "))
        centimetres = inches_to_centimetres(inches)
        print(f"{inches} Inches is {centimetres} Centimetres")
    elif conversion_type == "5":
        kilometres = float(input("Enter length in Kilometres: "))
        miles = kilometres_to_miles(kilometres)
        print(f"{kilometres} Kilometres is {miles} Miles")
    elif conversion_type == "6":
        miles = float(input("Enter length in Miles: "))
        kilometres = miles_to_kilometres(miles)
        print(f"{miles} Miles is {kilometres} Kilometres")
    else:
        print("Invalid conversion type")

elif unit_type == "4":
    print("Which conversion do you want to do?")
    print("1 = Kilograms to Pounds")
    print("2 = Pounds to Kilograms")
    print("3 = Grams to Ounces")
    print("4 = Ounces to Grams")
    conversion_type = input("Conversion type: ")

    if conversion_type == "1":
        kilograms = float(input("Enter weight in Kilograms: "))
        pounds = kilograms_to_pounds(kilograms)
        print(f"{kilograms} Kilograms is {pounds} Pounds")
    elif conversion_type == "2":
        pounds = float(input("Enter weight in Pounds: "))
        kilograms = pounds_to_kilograms(pounds)
        print(f"{pounds} Pounds is {kilograms} Kilograms")
    elif conversion_type == "3":
        grams = float(input("Enter weight in Grams: "))
        ounces = grams_to_ounces(grams)
        print(f"{grams} Grams is {ounces} Ounces")
    elif conversion_type == "4":
        ounces = float(input("Enter weight in Ounces: "))
        grams = ounces_to_grams(ounces)
        print(f"{ounces} Ounces is {grams} Grams")
    else:
        print("Invalid conversion type")

elif unit_type == "5":
    print("Which conversion do you want to do?")
    print("1 = Kilometers per Hour to Miles per Hour")
    print("2 = Miles per Hour to Kilometers per Hour")
    conversion_type = input("Conversion type: ")

    if conversion_type == "1":
        kmh = float(input("Enter speed in Kilometers per Hour: "))
        mph = kmh_to_mph(kmh)
        print(f"{kmh} Kilometers per Hour is {mph} Miles per Hour")
    elif conversion_type == "2":
        mph = float(input("Enter speed in Miles per Hour: "))
        kmh = mph_to_kph(mph)
        print(f"{mph} Miles per Hour is {kmh} Kilometers per Hour")
    else:
        print("Invalid conversion type")

elif unit_type == "6":
    print("Which conversion do you want to do?")
    print("1 = Square Meters to Square Feet")
    print("2 = Square Feet to Square Meters")
    print("3 = Acres to Square Meters")
    print("4 = Square Meters to Acres")
    conversion_type = input("Conversion type: ")

    if conversion_type == "1":
        m2 = float(input("Enter area in Square Meters: "))
        ft2 = m2_to_ft2(m2)
        print(f"{m2} Square Meters is {ft2} Square Feet")
    elif conversion_type == "2":
        ft2 = float(input("Enter area in Square Feet: "))
        m2 = ft2_to_m2(ft2)
        print(f"{ft2} Square Feet is {m2} Square Meters")
    elif conversion_type == "3":
        acres = float(input("Enter area in Acres: "))
        m2 = acres_to_m2(acres)
        print(f"{acres} Acres is {m2} Square Meters")
    elif conversion_type == "4":
        m2 = float(input("Enter area in Square Meters: "))
        acres = m2_to_acres(m2)
        print(f"{m2} Square Meters is {acres} Acres")
    else:
        print("Invalid conversion type")

elif unit_type == "7":
    print("Which conversion do you want to do?")
    print("1 = Minutes to Seconds")
    print("2 = Seconds to Minutes")
    print("3 = Hours to Minutes")
    print("4 = Minutes to Hours")
    conversion_type = input("Conversion type: ")

    if conversion_type == "1":
        minutes = float(input("Enter time in Minutes: "))
        seconds = min_to_secs(minutes)
        print(f"{minutes} Minutes is {seconds} Seconds")
    elif conversion_type == "2":
        seconds = float(input("Enter time in Seconds: "))
        minutes = secs_to_min(seconds)
        print(f"{seconds} Seconds is {minutes} Minutes")
    elif conversion_type == "3":
        hours = float(input("Enter time in Hours: "))
        minutes = hours_to_min(hours)
        print(f"{hours} Hours is {minutes} Minutes")
    elif conversion_type == "4":
        minutes = float(input("Enter time in Minutes: "))
        hours = min_to_hours(minutes)
        print(f"{minutes} Minutes is {hours} Hours")
    else:
        print("Invalid conversion type")
