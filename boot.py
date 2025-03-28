from machine import I2C
from AXP2101 import AXP2101

# Pinos de ligação do I2C

SDA = 'G21'
SCL = 'G22'
IRQ = 'G35'

I2CBUS = I2C(0, pins = (SDA,SCL)) # sda, scl
PMU = AXP2101(I2CBUS)
#PMU.setALDO2Voltage(3300)        # Definir tensão de alimentação saída 4 (3.3V)
#PMU.enableALDO2()               # Lora Enabled
PMU.setALDO4Voltage(3300)        # Definir tensão de alimentação saída 4 (3.3V)
PMU.enableALDO4()               # Lora Enabled