min_temperature = 0
max_temperature = 100
step = 10

print('Celsius\tFahrenheit')

for celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = celsius * 9/5 + 32

    print(f'{celsius:7}\t{fahrenheit:10.0}')
