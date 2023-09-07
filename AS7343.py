import smbus
import time
enable= False

class Color16Click:
    def __init__(self, bus=1):
        self.bus = smbus.SMBus(bus)
        #REG=Register than the address
        self.I2C_Address = 0x39
        self.REG_AUXID = 0x58
        self.REG_REVID = 0x59
        self.REG_ID = 0x5A
        self.REG_CFG_12 = 0x66
        self.REG_ENABLE = 0x80
        self.REG_ATIME = 0x81
        self.REG_WTIME = 0x83
        self.REG_SP_TH_L_LSB = 0x84
        self.REG_SP_TH_L_MSB = 0x85
        self.REG_SP_TH_H_LSB = 0x86
        self.REG_SP_TH_H_MSB = 0x87
        self.REG_STATUS = 0x93
        self.REG_ASTATUS = 0x94
        self.REG_DATA_0_L = 0x95
        self.REG_DATA_0_H = 0x96
        self.REG_DATA_1_L = 0x97
        self.REG_DATA_1_H = 0x98
        self.REG_DATA_2_L = 0x99
        self.REG_DATA_2_H = 0x9A
        self.REG_DATA_3_L = 0x9B
        self.REG_DATA_3_H = 0x9C
        self.REG_DATA_4_L = 0x9D
        self.REG_DATA_4_H = 0x9E
        self.REG_DATA_5_L = 0x9F
        self.REG_DATA_5_H = 0xA0
        self.REG_DATA_6_L = 0xA1
        self.REG_DATA_6_H = 0xA2
        self.REG_DATA_7_L = 0xA3
        self.REG_DATA_7_H = 0xA4
        self.REG_DATA_8_L = 0xA5
        self.REG_DATA_8_H = 0xA6
        self.REG_DATA_9_L = 0xA7
        self.REG_DATA_9_H = 0xA8
        self.REG_DATA_10_L = 0xA9
        self.REG_DATA_10_H = 0xAA
        self.REG_DATA_11_L = 0xAB
        self.REG_DATA_11_H = 0xAC
        self.REG_DATA_12_L = 0xAD
        self.REG_DATA_12_H = 0xAE
        self.REG_DATA_13_L = 0xAF
        self.REG_DATA_13_H = 0xB0
        self.REG_DATA_14_L = 0xB1
        self.REG_DATA_14_H = 0xB2
        self.REG_DATA_15_L = 0xB3
        self.REG_DATA_15_H = 0xB4
        self.REG_DATA_16_L = 0xB5
        self.REG_DATA_16_H = 0xB6
        self.REG_DATA_17_L = 0xB7
        self.REG_DATA_17_H = 0xB8
        self.REG_STATUS_2 = 0x90
        self.REG_STATUS_3 = 0x91
        self.REG_STATUS_5 = 0xBB
        self.REG_STATUS_4 = 0xBC
        self.REG_CFG_0 = 0xBF
        self.REG_CFG_1 = 0xC6
        self.REG_CFG_3 = 0xC7
        self.REG_CFG_6 = 0xF5
        self.REG_CFG_8 = 0xC9
        self.REG_CFG_9 = 0xCA
        self.REG_CFG_10 = 0x65
        self.REG_PERS = 0xCF
        self.REG_GPIO = 0x6B
        self.REG_ASTEP_LSB = 0xD4
        self.REG_ASTEP_MSB = 0xD5
        self.REG_CFG_20 = 0xD6
        self.REG_LED = 0xCD
        self.REG_AGC_GAIN_MAX = 0xD7
        self.REG_AZ_CONFIG = 0xDE
        self.REG_FD_TIME_1 = 0xE0
        self.REG_FD_TIME_2 = 0xE2
        self.REG_FD_CFG_0 = 0xDF
        self.REG_FD_STATUS = 0xE3
        self.REG_INTENAB = 0xF9
        self.REG_CONTROL = 0xFA
        self.REG_FIFO_MAP = 0xFC
        self.REG_FIFO_LVL = 0xFD
        self.REG_FDATA_L = 0xFE
        self.REG_FDATA_H = 0xFF
        self.ENABLE_FDEN = 0x40
        self.ENABLE_SMUXEN = 0x10
        self.ENABLE_WEN = 0x08
        self.ENABLE_SP_EN = 0x02
        self.ENABLE_PON = 0x01
        self.ENABLE_POFF = 0x00
    

    def Write_Register(self, register, value):
        self.bus.write_byte_data(self.I2C_Address, register, value)

    def Read_Register(self, register):
        return self.bus.read_byte_data(self.I2C_Address, register)

    def Modify_Register_Bits(self, register, bitmask, value):
        # Reads the current value of register
        Reg_Value = self.Read_Register(register)
        
        Reg_Value &= ~bitmask # Clear the bits to modify
        Reg_Value |= (value & bitmask) # Set the desired bits
        # Writes the updated value back to the register
        self.Write_Register(register, Reg_Value)
    
 
class Power_Set:
    def __init__(self):
        self.enable = False  # Initially, power set is disabled

    def enable_power_set(self):
        self.enable = True

    def disable_power_set(self):
        self.enable = False

    def power_set_function(self):
        if enable is True:
            #This is to make the PON bit to 1 which powers on the device
            self.Modify_Register_Bits(self.REG_ENABLE, self.ENABLE_PON, self.ENABLE_PON)
            print("xd")
        else:
            #This is to make the PON bit to 0 which powers off the device
            self.Modify_Register_Bits(self.REG_ENABLE, self.ENABLE_PON, 0)
            print("l")
    
        
class Spectral_Measurement_Set:
    def __init__(self, power_set_instance):
        self.power_set_instance = power_set_instance
    def perform_spectral_measurement(self):
        if enable is True:           
            self.Modify_Register_Bits(self.REG_ENABLE, self.ENABLE_SP_EN, self.ENABLE_SP_EN)
        else:
            print("Warning Power is off")






Color_Sensor = Color16Click()
power_set = Power_Set()
spectral_measurement = Spectral_Measurement_Set(power_set)
power_set.enable_power_set(Color_Sensor)
power_set.power_set_function()
spectral_measurement.perform_spectral_measurement()

