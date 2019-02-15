print(format("Temp","20"), format("Wind Speed","^19"), format("Wind Chill",">30"))
Temp = 20
Wind_Speed = 19
Wind_Chill = 4.60

print(format(Temp,"<20,.2f"), format(Wind_Speed,"^19,.2f"),format(Wind_Chill,">30,.2f"))
Temp = 0
Wind_Speed = 5
Wind_Chill = -10.51


print(format(Temp,"<20,.2f"), format(Wind_Speed,"^19,.2f"), format(Wind_Chill,">30,.2f"))
Temp = -15.00
Wind_Speed = 25.00
Wind_Chill = -44.15

print(format(Temp,"<20,.2f"), format(Wind_Speed,"^19,.2f"), format(Wind_Chill,">30,.2f"))

print('--------------------------------------------------------------------------------')

print()
x = 0 
for x in range(6):
    print()
    air_temp = float(input('What is the temperature for which you want to calculate a wind chill index:'))
    
    wct_index = 35.74 + 0.6215 * air_temp - 35.75 \
            * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    print('For a temperature of', air_temp,'and a wind speed of',air_speed,', the wind chill index', format(wct_index,'.2f'))
     if wct_index < 40 or wct_index >20:
        print("Just a breeze!")
    elif wct_index < 19 or wct_index > -20:
        print("It's chilly outside")
    elif wct < -20:
        print("Now we are freezing!")
