!#usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

class Robot(object) :
    def __init__(self) :
        self.rd = LargeMotor("outB")
        self.re = LargeMotor("outA")
        self.md = MediumMotor("outC")
        self.id = InfraredSensor("in4")
        self.ie = InfraredSensor("in3")
        self.cs = ColorSensor()
        self.gs = GyroSendor()

        self.id.mode = "IR-PROX"
        self.ie.mode = "IR-PROX"
        self.gs.mode = "GYRO-ANG"

        self.speed = 300
        self.ang1 = gy.value()
        self.ang3 = gy.value()
        self.cont = 0
        self.cont1 = 0

    def Conometro0(self):
        print("Tempo: %ds" % self.cont1)
        self.cont1 += 1
        sleep(1)

    def Black0(self) :
        self.rd.run_to_rel_pos(position_sp = 540, speed_sp = (self.speed * 1.5))
        self.re.run_to_rel_pos(position_sp = 540, speed_sp = (self.speed * 1.5))
        self.rd.wait_while("running")
        self.re.wait_while("running")
        self.ang2 = self.ang1 + 170
        while self.ang1 > self.ang3 :
            self.ang3 = gy.value()
            self.rd.run_forever(speed_sp = self.speed * 0.75)
            self.re.run_forever(speed_sp = -(self.speed * 0.75))

    def Red0(self):
        self.rd.run_to_rel_pos(position_sp = 540, speed_sp = (self.speed * 1.5))
        self.re.run_to_rel_pos(position_sp = 540, speed_sp = (self.speed * 1.5))
        self.rd.wait_while("running")
        self.re.wait_while("running")
        self.ang2 = self.ang1 + 85
        while self.ang2 > self.ang3 :
            self.ang3 = gy.value()
            self.rd.run_forever(speed_sp = self.speed * 0.75)
            self.re.run_forever(speed_sp = -(self.speed * 0.75))

    def Red1(self):
        self.rd.run_to_rel_pos(position_sp = 540, speed_sp = (self.speed * 1.5))
        self.re.run_to_rel_pos(position_sp = 540, speed_sp = (self.speed * 1.5))
        self.rd.wait_while("running")
        self.re.wait_while("running")
        self.ang2 = self.ang1 - 85
        while self.ang2 < self.ang3:
            self.ang3 = gy.value()
            self.rd.run_forever(speed_sp = -(self.speed * 0.75))
            self.re.run_forever(speed_sp = self.speed * 0.75)

    def Centralizar0(self):
        if self.gy.value() > self.ang1() :
            self.rd.run_forever(speed_sp = (self.speed * 0.35))
            sleep(0.3)
            self.re.run_forever(speed_sp = (self.speed * 0.35))
            sleep(0.3)
        else :
            self.re.run_forever(speed_sp=(self.speed * 0.35))
            sleep(0.3)
            self.rd.run_forever(speed_sp=(self.speed * 0.35))
            sleep(0.3)

    def Andar0(self) :
        self.rd.run_forever(speed_sp = self.speed)
        self.re.run_forever(speed_sp = self.speed)
   
    def Virar0(self) :
        self.rd.run_to_rel_pos(position_sp = 10, speed_sp = (self.speed * 0.5))
        self.re.run_to_rel_pos(position_sp = 10, speed_sp = (self.speed * 0.5))
        self.rd.wait_while("running")
        self.re.wait_while("running")
        self.ang2 = self.ang1 + 85
        while self.ang2 > self.ang3 :
            self.ang3 = gy.value()
            self.rd.run_forever(speed_sp = self.speed * 0.75)
            self.re.run_forever(speed_sp = -(self.speed * 0.75))
        sleep(0.2)
        self.rd.run_to_rel_pos(position_sp = 500, speed_sp = (self.speed * 1.5))
        self.re.run_to_rel_pos(position_sp = 500, speed_sp = (self.speed * 1.5))
        self.rd.wait_while("running")
        self.re.wait_while("running")
        sleep(0.2)
            
    def Virar1(self) :
        self.rd.run_to_rel_pos(position_sp = 10, speed_sp = (self.speed * 0.5))
        self.re.run_to_rel_pos(position_sp = 10, speed_sp = (self.speed * 0.5))
        self.rd.wait_while("running")
        self.re.wait_while("running")
        self.ang2 = self.ang1 - 85
        while self.ang2 < self.ang3 :
            self.ang3 = gy.value()
            self.rd.run_forever(speed_sp = -(self.speed * 0.75))
            self.re.run_forever(speed_sp = self.speed * 0.75)
        sleep(0.2)
        self.rd.run_to_rel_pos(position_sp = 500, speed_sp = (self.speed * 1.5))
        self.re.run_to_rel_pos(position_sp = 500, speed_sp = (self.speed * 1.5))
        self.rd.wait_while("running")
        self.re.wait_while("running")
        sleep(0.2)
            
    def Main(self) :
        self.Centralizar0()
        self.Conometro0()
        if self.cs.value() == 6 :
            self.Andar0()
        elif self.cs.value() == 5 :
            self.Red0()
            self.cont += 1
            if self.cont % 2 == 0 :
                self.andar0()
            else :
                self.Red1()
        elif self.cs.value() == 1 :
            self.Black0()
        if self.id.alue() > self.ie.value() :
            self.md.run_to_rel_pos(position_sp = 165, speed_sp = (self.speed * 0.25))
            sleep(0.4)
            self.Virar0()
            self.md.run_to_rel_pos(position_sp = -165, speed_sp = (self.speed * 0.25))
            sleep(0.4)
        else :
            self.md.run_to_rel_pos(position_sp = 165, speed_sp = (self.speed * 0.25))
            sleep(0.4)
            self.Virar1()
            self.md.run_to_rel_pos(position_sp = -165, speed_sp = (self.speed * 0.25))

Robot().Main()

#             0      1      2       3        4         5         6        7
# colors = ["nda","preto","azul","verde","amarelo","vermelho","branco","marrom"]
