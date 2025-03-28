# main.py -- put your code here!
# display.py -- Test displays with ssd1306 controller
from machine import I2C, Pin, ADC
import ssd1306
import os
import time
import math
import onewire
from AXP2101 import AXP2101


##Setup oled
oled_width = 128
oled_height = 64
i2c = I2C(0, mode=I2C.MASTER, pins=('G21','G22'), baudrate=100000)


### Sensor de turbidez e temperatura

##Declaração Variáveis
temperatura = 0
turbidez = 0

## Setup Sensor turbidez
adc=ADC(0, bits=9)     
apin = adc.channel(pin='G36', attn=ADC.ATTN_11DB)   

## Setup Sensor Temperatura
ow = onewire.OneWire(Pin('G14'))
devices = ow.scan()
temp = onewire.DS18X20(ow)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


while True:
    time.sleep(1)
    #Info Turbidez
    turbidez = apin.voltage()
    print(turbidez)
    turbidez = (turbidez * 100) / 2078
    turbidez = 100 - turbidez
    print("Turbidez = {} %".format(turbidez))   


    #Info Temperature
    if temp.roms:
        rom = temp.roms[0]  # Usar o primeiro sensor encontrado
        temp.start_conversion(rom)  # Inicia a leitura
        time.sleep(1)
        temperatura = temp.read_temp_async(rom)  # Obtém a temperatura
        print("Temperatura: {}".format(temperatura))
    else:
        print("Nenhum sensor DS18B20 encontrado!")

    if turbidez > 50:
        PMU.setChargingLedMode(AXP2101.XPOWERS_CHG_LED_BLINK_4HZ)
    else:
        PMU.setChargingLedMode(AXP2101.XPOWERS_CHG_LED_BLINK_1HZ)

    oled.fill(0)
    oled.show()

    if turbidez > 20 and turbidez < 40:
        print("Água pouco turva")
        oled.text("P.Turva",85,35,70,5)
    elif turbidez > 41 and turbidez < 60:
        print("Água turva")
        oled.text("Turva" ,85,35,70,5)
    elif turbidez > 60:
        print ("Água muito turva")
        oled.text("M.Turva" ,85,35,70,5)
    else:
        print("Água limpa") 
        oled.text("Limpa" ,85,55,70,5)

    oled.text("Temperatura:",2,10,70,5)
    oled.text("{}".format(temperatura),2,19,35,5)
    oled.text("Turbidez:" ,2,35,70,5)
    oled.text("{}".format(turbidez) ,2,44,35,5)
    oled.show()

    





