#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
class Robot(object):
    def __init__(self) :
        self.MD = LargeMotor("outD")
        self.ME = LargeMotor("outC")
        self.IR = InfraredSensor()
        self.GY = GyroSensor()

        self.IR.mode = "IR-PROX"
        self.GY.mode = "GYRO-ANG"

    def Led(self) :
        while True :
            self.Leds.set_color(Leds.RIGHT, Leds.ORANGE)
            sleep(1)
    
    def GYRO(self) :
        print("Ângulo: %d" %(self.GY.value()))
        Ang = self.GY.value() + 87
        while Ang != self.GY.value() :
            self.MD.run_forever(speed_sp = 100)
            self.ME.run_forever(speed_sp = 300)
            self.Led()
        
    def Direita(self) :
        print("Distância: &d" %(self.IR.value()))
        if self.IR.value() <= 10 :
            self.GYRO()
    
    def Main(self) :
        while True :
            self.MD.run_forever(speed_sp = 300)
            self.ME.run_forever(speed_sp = 300)
            self.Direita()
        
Robot().Main()
