#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep


class Robozin(object):

    def __init__(self):

        # analogicos
        # motors
        self.motor_D, self.motor_E = LargeMotor("outB"), LargeMotor("outA")

        # Sensors

        self.infraESQ, self.colorESQ, self.colorDIR, self.infraDIR = InfraredSensor("in1"), ColorSensor(
            "in3"), ColorSensor("in2"), InfraredSensor("in4")

        # mode

        self.infraESQ.mode, self.colorESQ.mode, self.colorDIR.mode, self.infraDIR.mode = "IR-PROX", "COL-COLOR", "COL-COLOR", "IR-PROX"

        # Globais

        self.caminho = {}

        self.curva, self.voltando, self.verdeB = False, False, False  # False Booleans

        self.velocidadeE, self.velocidadeD = 300, 300  # Velocidades

        self.angulo_in, self.variacao, self.erro_ang = self.infraESQ.value(), 100, 0  # Angulos

        self.verm, self.verd, self.azul = 0, 0, 0

        self.coratual = 10

        self.matriz = [["D","E","F"],["D","E","F"],["D","E","F"],["D","E","F"],["D","E","F"],["D","E","F"],["D","E","F"]]

        self.cont = 0

        # self.main()

    def andar(self):

        if self.infraESQ.value() >= 18 and self.infraDIR.value() <= 16:
            print("1")
            self.velocidadeE = 380
            self.velocidadeD = 260

        elif self.infraESQ.value() >= 16 and self.infraDIR.value() <= 18:
            print("2")
            self.velocidadeD = 380
            self.velocidadeE = 260

        else:
            print("3")
            self.velocidadeD = 300
            self.velocidadeE = 300
            self.velocidadeG = 300

        self.motor_D.run_forever(speed_sp=self.velocidadeD)
        self.motor_E.run_forever(speed_sp=self.velocidadeE)

    def curvaD(self):
        self.motor_E.run_to_rel_pos(position_sp=1380, speed_sp=self.velocidadeE)
        self.motor_D.run_to_rel_pos(position_sp=1380, speed_sp=self.velocidadeD / 3)
        self.motor_D.wait_while("running")
        self.motor_E.wait_while("running")
        while self.colorDIR.value() != 6 and self.colorESQ.value() != 6:
            self.motor_E.run_forever(speed_sp=self.velocidadeE)
            self.motor_D.run_forever(speed_sp=self.velocidadeD)

    def meiavolta(self):
        self.motor_E.stop()
        self.motor_D.stop()
        self.motor_D.run_to_rel_pos(position_sp=1380, speed_sp=300)
        self.motor_E.run_to_rel_pos(position_sp=-1380, speed_sp=300)
        self.motor_D.wait_while("running")
        self.motor_E.wait_while("running")
        self.cont += 1
        if self.cont == 1 :
            self.matriz.remove(self.matriz[self.colorDIR2]["D"])
        elif self.cont == 2 :
            self.matriz.remove(self.matriz[self.colorDIR2]["F"])

    def maincurva(self):
        if (self.colorDIR.value() != 6 and self.colorESQ.value() != 6) or (self.colorDIR.value() != 0 and self.colorESQ.value() != 0) :
            global self.colorDIR2 == self.colorDIR.value()
            global self.colorESQ2 == self.colorESQ.value()
            self.motor_D.run_to_rel_pos(position_sp = 500, speed_sp = self.velocidadeG)
            self.motor_E.run_to_rel_pos(position_sp = 500, speed_sp = self.velocidadeG)
            self.motor_D.wait_while("running")
            self.motor_D.wait_while("running")
            self.motor_D.run_to_rel_pos(position_sp = 690, speed_sp = -(self.velocidadeG))
            self.motor_E.run_to_rel_pos(position_sp = 690, speed_sp = self.velocidadeG)
            while self.colorDIR.value() != 6 and self.colorESQ.value() != 6 :
                self.motor_E.run_forever(speed_sp=self.velocidadeE)
                self.motor_D.run_forever(speed_sp=self.velocidadeD)
            self.main()

    def main(self):
        # Sound.beep()
        while True:
            print(self.colorDIR.value(), self.colorESQ.value())
            if self.colorDIR.value() == 6 and self.colorESQ.value() == 6:
                self.andar()
            elif self.colorESQ.value() == 0 or self.colorDIR.value() == 0:
                if self.colorDIR.value() == 0:
                    while self.colorDIR.value() == 0:
                        self.motor_D.run_forever(speed_sp=-50)
                        self.motor_E.run_forever(speed_sp=-50)
                    self.motor_E.run_to_rel_pos(position_sp=-100, speed_sp=400)
                else:
                    while self.colorESQ.value() == 0:
                        self.motor_D.run_forever(speed_sp=-50)
                        self.motor_E.run_forever(speed_sp=-50)
                    self.motor_D.run_to_rel_pos(position_sp=-100, speed_sp=400)
            elif self.colorESQ.value() == 6 and self.colorDIR.value() != 6:
                while self.colorDIR.value() != 6:
                    self.motor_E.run_forever(speed_sp=-50)
                    self.motor_D.run_forever(speed_sp=-50)
                self.motor_E.run_to_rel_pos(position_sp=40, speed_sp=300)
            elif self.colorESQ.value() != 6 and self.colorDIR.value() == 6:
                while self.colorESQ.value() != 6:
                    self.motor_E.run_forever(speed_sp=-50)
                    self.motor_D.run_forever(speed_sp=-50)
                self.motor_D.run_to_rel_pos(position_sp=40, speed_sp=300)
            else:
                if self.colorESQ.value() == 3 or self.colorDIR.value() == 3:
                    self.coratual = 3
                    self.maincurva()
            if self.matriz[self.colorDIR][0] == "D" :
                self.curvaD()
            elif self.matriz[self.colorDIR][0] == "E" :
                self.curvaE()
            elif self.matriz[self.colorDIR][0] == "F" :
                if 
                self.main()
            

    def andacarai(self):
        while True:
            self.andar()


Robozin().main()
# Robozin().andacarai()
# colors = ["nda","preto","azul","verde","amarelo","vermelho","branco","marrom"]
