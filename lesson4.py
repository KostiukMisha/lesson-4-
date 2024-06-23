temperature = float(input('write temperature '))
Fahrenheit = ((temperature * 9/5) + 32)
if temperature > -273.15:
    print (Fahrenheit)
elif temperature < -273.15:
    print ("Error: Temperature below absolute zero (-273.15°C)")
