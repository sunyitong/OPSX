from machine import Pin, I2C, PWM
import time
from ssd1306 import SSD1306_I2C
from vl53l1x import VL53L1X
import framebuf

# Caution! This value is used to hold the shutter solenoid and should be modified by self-test.
SOLENOID_THRESHOLD = 20000


def shut(apture, f="1"):
    sht.duty_u16(65535)
    time.sleep_ms(18)
    sht.duty_u16(SOLENOID_THRESHOLD) 
    motor.value(1)
    while True:
        if s3.value() == 1:
            motor.value(0)
            break

    sht.duty_u16(0)
    if f == '0':
        gap=int(apture*0.3)
        time.sleep_ms(gap)
        fl.value(1)
        time.sleep_ms(gap)
        fl.value(0)
        time.sleep_ms(gap)
    elif f == '1':
        time.sleep_ms(apture)
    elif f == 'B':
        time.sleep_ms(15)
        while True:
            time.sleep_ms(3)
            if btn.value() == 1:
                break
    elif f == 'T':
        time.sleep(100)
        while True:
            time.sleep(3)
            if btn.value() == 0:
                break
        
    sht.duty_u16(65535)
    time.sleep_ms(20)
    sht.duty_u16(SOLENOID_THRESHOLD)
    motor.value(1)
    while True:
        if s5.value() == 0:
            motor.value(0)
            sht.duty_u16(0)
            break

def plug():
    a = plugI2c.readfrom_mem(32, 0x00, 2)
    one = "%8d" %int(bin(a[0])[2:])
    two = "%8d" %int(bin(a[1])[2:])
    one = one.replace(" ","0")
    return one+two

def showFrame():
    display.fill(0)
    display.fill_rect(0, 0, 128, 11, 1)
    display.vline(51, 0, 11, 0)
    display.vline(82, 0, 11, 0)
    
def backFunc():
    showFrame()
    fullp = plug()
    ec = fullp[2:6]
    sw = fullp[0:2]
    encoder()
    switch()
    dist()
    display.show()

# iso=1 for 600 paper =0 for 70 paper
def lux(iso=1):
    h = i2c.readfrom_mem(74, 0x03, 1)
    l = i2c.readfrom_mem(74, 0x04, 1)
    luxb = bin(((h[0] << 4) | l[0]) | 4096)
    expo = 8*int(luxb[3]) + 4*int(luxb[4]) + 2*int(luxb[5]) + int(luxb[6])
    manti = 128*int(luxb[7]) + 64*int(luxb[8]) + 32*int(luxb[9]) + 16*int(luxb[10]) + 8*int(luxb[11]) + 4*int(luxb[12]) + 2*int(luxb[13]) + int(luxb[14])
    lux = 2**expo * manti * 0.045
    if iso == 0:
        if 2.5<lux<=3.52:
            return ev75
        elif 3.52<lux<=4.99:
            return ev8
        elif 4.99<lux<=7.12:
            return ev85
        elif 7.12<lux<=10.13:
            return ev9
        elif 10.13<lux<=14.21:
            return ev95
        elif 14.21<lux<=19.79:
            return ev10
        elif 19.79<lux<=27.62:
            return ev105
        elif 27.62<lux<=39.01:
            return ev11
        elif 39.01<lux<=55.48:
            return ev115
        elif 55.48<lux<=78.07:
            return ev12
        elif 78.07<lux<=105.48:
            return ev125
        elif 105.48<lux<=150:
            return ev135
        elif 150<lux<=180:
            return ev145
        elif 180<lux<=200:
            return ev15
        elif 200<lux:
            return ev16
        else:
            return ev7
    else:
        if 0.3<lux<=0.5: 
            return ev75
        elif 0.5<lux<=0.9:
            return ev8
        elif 0.9<lux<=1.2:
            return ev85
        elif 1.2<lux<=1.74:
            return ev9
        elif 1.74<lux<=2.5:
            return ev95
        elif 2.5<lux<=3.52:
            return ev10
        elif 3.52<lux<=4.99:
            return ev105
        elif 4.99<lux<=7.12:
            return ev11
        elif 7.12<lux<=10.13:
            return ev115
        elif 10.13<lux<=14.21:
            return ev12
        elif 14.21<lux<=19.79:
            return ev125
        elif 19.79<lux<=27.62:
            return ev13
        elif 27.62<lux<=39.01:
            return ev135
        elif 39.01<lux<=55.48:
            return ev14
        elif 55.48<lux<=78.07:
            return ev145
        elif 78.07<lux<=105.48:
            return ev15
        elif 105.48<lux:
            return ev16
        else:
            return ev7

def encoder():
    if ec == EC_ZERO:
        display.text('AUTO', 10, 2, 0)
        return 'A'
    elif ec == EC_ONE:
        display.text('B', 23, 2, 0)
        return 'B'
    elif ec == EC_TWO:
        display.text('T', 23, 2, 0)
        return 'T'
    elif ec == EC_THREE:
        display.text('1/2', 15, 2, 0)
        return ev7
    elif ec == EC_FOUR:
        display.text('1/4', 15, 2, 0)
        return ev8
    elif ec == EC_FIVE:
        display.text('1/6', 15, 2, 0)
        return ev85
    elif ec == EC_SIX:
        display.text('1/8', 15, 2, 0)
        return ev9
    elif ec == EC_SEVEN:
        display.text('1/10', 10, 2, 0)
        return ev95
    elif ec == EC_EIGHT:
        display.text('1/15', 10, 2, 0)
        return ev10
    elif ec == EC_NINE:
        display.text('1/20', 10, 2, 0)
        return ev105
    elif ec == EC_A:
        display.text('1/30', 10, 2, 0)
        return ev11
    elif ec == EC_B:
        display.text('1/60', 10, 2, 0)
        return ev12
    elif ec == EC_C:
        display.text('1/125', 5, 2, 0)
        return ev13
    elif ec == EC_D:
        display.text('1/250', 5, 2, 0)
        return ev14
    elif ec == EC_E:
        display.text('1/500', 5, 2, 0)
        return ev15
    elif ec == EC_F:
        display.text('1/1000', 1, 2, 0)
        return ev16
    
def switch():
    if sw[0] == "1":
        display.text('600', 55, 2, 0)
    else:
        display.text('70', 59, 2, 0)
    if sw[1] == "1":
        display.text('OFF', 94, 2, 0)
    else:
        display.text('FLASH', 86, 2, 0)


def dist():
    display.text(str(round(tof.read()*0.001,2))+' m', 72, 23)

#基本定义
EC_ZERO = '1111'
EC_ONE = '0111'
EC_TWO = '1101'
EC_THREE = '0101'
EC_FOUR = '1110'
EC_FIVE = '0110'
EC_SIX = '1100'
EC_SEVEN = '0100'
EC_EIGHT = '1011'
EC_NINE = '0011'
EC_A = '1001'
EC_B = '0001'
EC_C = '1010'
EC_D = '0010'
EC_E = '1000'
EC_F = '0000'

ev7 = 600
ev75 = 440
ev8 = 280
ev85 =210
ev9 = 155
ev95 =120
ev10 = 97
ev105 = 70
ev11 = 48
ev115 = 40
ev12 = 33
ev125 = 29
ev13 = 25
ev135 = 23
ev14 = 21
ev145 = 20
ev15 = 19
ev16 = 18

back = "01"
front = "10"

#基本初始化
s8 = Pin(17, Pin.IN)
s9 = Pin(16, Pin.IN)
motor = Pin(15,Pin.OUT, value=0)
s3 = Pin(14, Pin.IN, Pin.PULL_UP)
s5 = Pin(13, Pin.IN, Pin.PULL_UP)
btn = Pin(18, Pin.IN, Pin.PULL_UP)
fl = Pin(22, Pin.OUT)
sht = PWM(Pin(4))
sht.freq(20000)
sht.duty_u16(0)
apt = Pin(19, Pin.OUT, value=0)
i2c = I2C(1, scl=Pin(11), sda=Pin(10))
plugI2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)
while True:
    plugscan = bool(plugI2c.scan())
    if plugscan == True:
        try:
            display = SSD1306_I2C(128, 32, plugI2c)
            display.contrast(0)
            tof = VL53L1X(plugI2c)
            fullp = plug()
            plugFlag = 1
            fb = fullp[6:8]
            func = "1"
            if fb == back:
                while True:
                    plugscan = bool(plugI2c.scan())
                    if plugscan == False:
                        break
                    else:
                        showFrame()
                        fullp = plug()
                        ec = fullp[2:6]
                        sw = fullp[0:2]
                        if sw[1] == "0":
                            display.text('FLASH', 86, 2, 0)
                            display.text('1/30', 10, 2, 0)
                            enc = 48
                            func = "0"
                        else:
                            display.text('OFF', 94, 2, 0)
                            enc = encoder()
                            func = "1"
                            if sw[0] == "0":
                                film = 0
                                display.text('70', 60, 2, 0)
                            else:
                                film = 1
                                display.text('600', 55, 2, 0)
                            if enc == 'A':
                                enc = lux(film)                 
                                display.text(str(enc)+' ms', 8, 23)
                            elif enc == 'B':
                                func = 'B'
                            elif enc == 'T':
                                func = 'T'
                        dist()
                        display.show()
                        for i in range(350):
                            if btn.value()==0:
                                shut(enc,func)
                            time.sleep_ms(1)
                                 
                        
            elif fb == front:          
                led_one = bytearray(b'\x00\x1c\x00\x00<\x00\x00|\x00\x00\xfc\x00\x01\xfc\x00\x07\xfc\x00\x0f\xfc\x00\x1f\xbc\x00\x1e<\x00\x1c<\x00\x10<\x00\x00\x1c\x00\x00\x1c\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00\x1c\x00\x00<\x00\x00<\x00\x00>\x00\x00\x1c\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00\x1c\x00\x00<\x00\x00\x1c\x00\x00<\x00')
                led_two = bytearray(b'\x03\xfc\x00\x0f\xff\x00\x1f\xff\x80>\x0f\xc0|\x03\xe0x\x01\xe0p\x01\xe0\xf0\x00\xe0p\x00\xf0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x03\xe0\x00\x07\xc0\x00\x0f\x80\x00\x1f\x00\x00>\x00\x00~\x00\x00\xf8\x00\x01\xf0\x00\x03\xe0\x00\x0f\xc0\x00\x1f\x80\x00\x1f\x00\x00>\x00\x00|\x00\x00\xfa\x82\x80\xff\xff\xf0\xff\xff\xe0\xff\xff\xf0')
                led_three = bytearray(b'\x07\xfc\x00\x1f\xff\x00\x1f\xdf\x80>\x07\x80|\x07\xc0x\x03\xc0\xf0\x01\xc0p\x03\xe0\x00\x03\xc0\x00\x03\xc0\x00\x07\xc0\x00\x0f\x80\x00\xff\x00\x00\xfe\x00\x00\xff\x80\x01\x0f\xc0\x00\x03\xe0\x00\x01\xe0\x00\x01\xf0\x00\x00\xf0\x00\x00\xf0\x10\x00\xf0\xf0\x00\xf0\xf0\x01\xe0x\x01\xe0|\x03\xe0>\x07\xc0?\xbf\x80\x0f\xff\x00\x07\xfe\x00')
                led_four = bytearray(b'\x00\x07\x80\x00\x0f\x80\x00\x1f\x00\x00\x1f\x80\x00?\x80\x00\x7f\x80\x00\xff\x00\x00\xe7\x80\x01\xe7\x80\x03\xc7\x80\x03\x87\x00\x07\x87\x80\x0f\x07\x80\x0e\x0f\x80\x1e\x07\x00<\x07\x80x\x07\x80x\x07\x80\xf0\x07\x00\xfd\xbf\xe0\xff\xff\xf0\xff\xff\xf0\xff\xff\xf0\x00\x07\x80\x00\x07\x80\x00\x07\x00\x00\x07\x80\x00\x07\x00\x00\x07\x80\x00\x07\x80')
                led_five = bytearray(b'\x1f\xff\xc0\x1f\xff\xc0\x1f\xff\xc0?\xdb@<\x00\x00<\x00\x00<\x00\x008\x00\x008\x00\x00x\x00\x00{\xfc\x00\x7f\xff\x00\x7f\xff\x80\xfe\x0f\xc0x\x07\xc0\xf0\x03\xe0\x00\x01\xe0\x00\x01\xe0\x00\x00\xf0\x00\x01\xe0\x00\x01\xe0 \x01\xe0\xf0\x01\xe0\xf0\x01\xe0\xf0\x03\xc0|\x07\xc0~\x1f\x80?\xff\x00\x1f\xfe\x00\x03\xf8\x00')
                led_list = (led_five, led_four, led_three, led_two, led_one)
                while True:
                    showFrame()
                    fullp = plug()
                    ec = fullp[2:6]
                    sw = fullp[0:2]
                    if sw[1] == "0":
                        display.text('FLASH', 86, 2, 0)
                        display.text('1/30', 10, 2, 0)
                        enc = 48
                        func = "0"
                    else:
                        display.text('OFF', 94, 2, 0)
                        enc = encoder()
                        func = "1"
                        if sw[0] == "0":
                            film = 0
                            display.text('70', 60, 2, 0)
                        else:
                            film = 1
                            display.text('600', 55, 2, 0)
                        if enc == 'A':
                            enc = lux(film)                 
                            display.text(str(enc)+' ms', 8, 23)
                        elif enc == 'B':
                            func = 'B'
                        elif enc == 'T':
                            func = 'T'
                    display.text('SELFIE', 65, 23)
                    display.show()
                    for i in range(350):
                        if btn.value()==0:
                            display.contrast(255)
                            for i in range(5):
                                fb = framebuf.FrameBuffer(led_list[i], 20, 30, framebuf.MONO_HLSB)
                                display.fill(0)
                                display.blit(fb, 55, 0)
                                display.show()
                                time.sleep(0.8)
                                display.fill(1)
                                display.show()
                                time.sleep(0.2)
                            for i in range(5):
                                display.fill(1)
                                display.show()
                                time.sleep(0.13)
                                display.fill(0)
                                display.show()
                                time.sleep(0.13)                     
                            shut(enc,func)
                            display.contrast(0)
                        time.sleep_ms(1)
        except:
            pass
    else:
        enc = lux()
        for i in range(300):
            if btn.value()==0:
                shut(enc)
