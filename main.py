print('----------------')
print('Rules:\nCelsius   : C\nFahrenheit: F\nReamur    : R\nKelvin    : K')
print('----------------')

Conversion_From = input('Conversion from: ')
Conversion_To = input('Conversion to: ')

# From Celsius
if Conversion_From == 'C' and Conversion_To == 'F':
    temperature = float(input('Celsius temperature: '))
    temperature = (9/5) * temperature + 32
    print('Temperature:', temperature, '°F')
    
elif Conversion_From == 'C' and Conversion_To == 'R':
    temperature = float(input('Celsius temperature: '))
    temperature = (4/5) * temperature 
    print('Temperature:', temperature, '°R')
    
elif Conversion_From == 'C' and Conversion_To == 'K':
    temperature = float(input('Celsius temperature: '))
    temperature += 273.15
    print('Temperature:', temperature, 'K')

# From Reamur
elif Conversion_From == 'R' and Conversion_To == 'C':
    temperature = float(input('Reamur temperature: '))
    temperature = (5/4) * temperature 
    print('Temperature:', temperature, '°C')
    
elif Conversion_From == 'R' and Conversion_To == 'F':
    temperature = float(input('Reamur temperature: '))
    temperature = (9/4) * temperature + 32
    print('Temperature:', temperature, '°F')
    
elif Conversion_From == 'R' and Conversion_To == 'K':
    temperature = float(input('Reamur temperature: '))
    temperature = (5/4) * temperature + 273.15
    print('Temperature:', temperature, 'K')
    
# From Fahrenheit
elif Conversion_From == 'F' and Conversion_To == 'C':
    temperature = float(input('Fahrenheit temperature: '))
    temperature = (5/9) * (temperature - 32)
    print('Temperature:', temperature, '°C')
    
elif Conversion_From == 'F' and Conversion_To == 'R':
    temperature = float(input('Fahrenheit temperature: '))
    temperature = (4/9) * (temperature - 32)
    print('Temperature:', temperature, '°R')
    
elif Conversion_From == 'F' and Conversion_To == 'K':
    temperature = float(input('Fahrenheit temperature: '))
    temperature = (5/9) * (temperature - 32) + 273.15
    print('Temperature:', temperature, 'K')
    
# From Kelvin
elif Conversion_From == 'K' and Conversion_To == 'C':
    temperature = float(input('Kelvin temperature: '))
    temperature -= 273.15
    print('Temperature:', temperature, '°C')
    
elif Conversion_From == 'K' and Conversion_To == 'R':
    temperature = float(input('Kelvin temperature: '))
    temperature = (4/5) * (temperature - 273.15)
    print('Temperature:', temperature, '°R')
    
elif Conversion_From == 'K' and Conversion_To == 'F':
    temperature = float(input('Kelvin temperature: '))
    temperature = (9/5) * (temperature - 273.15) + 32
    print('Temperature:', temperature, '°F')

else:
    print('Statement not relevant')
