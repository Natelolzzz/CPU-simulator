from random import random
from math import ceil
from time import sleep
import os
import linecache
Reg1 = Reg2 = Reg3 = Reg4 = Reg5 = Reg6 = Reg7 = Reg8 = Clock = 0
LineNo = 1
RAM = []

def PrintMEM(Target):
    global Reg1,Reg2,Reg3,Reg4,Reg5,Reg6,Reg7,Reg8,RAM
    if Target == 'Reg1':
        print(Reg1)
    if Target == 'Reg2':
        print(Reg2)
    if Target == 'Reg3':
        print(Reg3)
    if Target == 'Reg4':
        print(Reg4)
    if Target == 'Reg5':
        print(Reg5)
    if Target == 'Reg6':
        print(Reg6)
    if Target == 'Reg7':
        print(Reg7)
    if Target == 'Reg8':
        print(Reg8)
    if Target == 'RAM':
        print(RAM)
    if Target == 'ALL':
        PrintMEM('1')
        PrintMEM('2')
        PrintMEM('3')
        PrintMEM('4')
        PrintMEM('5')
        PrintMEM('6')
        PrintMEM('7')
        PrintMEM('8')
        PrintMEM('RAM')

def SaveMEM(Target, Value):
    global Reg1,Reg2,Reg3,Reg4,Reg5,Reg6,Reg7,Reg8,RAM
    if Target == 'Reg1':
        Reg1 = Value
    if Target == 'Reg2':
        Reg2 = Value
    if Target == 'Reg3':
        Reg3 = Value
    if Target == 'Reg4':
        Reg4 = Value
    if Target == 'Reg5':
        Reg5 = Value
    if Target == 'Reg6':
        Reg6 = Value
    if Target == 'Reg7':
        Reg7 = Value
    if Target == 'Reg8':
        Reg8 = Value
    if Target == 'RAM' :
        RAM.append(Value)
    if Target == 'ALL':
        SaveMEM('Reg1', Value)
        SaveMEM('Reg2', Value)
        SaveMEM('Reg3', Value)
        SaveMEM('Reg4', Value)
        SaveMEM('Reg5', Value)
        SaveMEM('Reg6', Value)
        SaveMEM('Reg7', Value)
        SaveMEM('Reg8', Value)
        SaveMEM('RAM', Value)

def MEMtest():

    A = ceil(random()*10)
    SaveMEM('Reg1', A)
    SaveMEM('Reg2', A)
    SaveMEM('Reg3', A)
    SaveMEM('Reg4', A)
    SaveMEM('Reg5', A)
    SaveMEM('Reg6', A)
    SaveMEM('Reg7', A)
    SaveMEM('Reg8', A)
    SaveMEM('RAM', A)
    if Reg1 == A:
        print('Reg1 Ok')
    sleep(3)
    if Reg2 == A:
        print('Reg2 Ok')
    sleep(3)
    if Reg3 == A:
        print('Reg3 Ok')
    sleep(3)
    if Reg4 == A:
        print('Reg4 Ok')
    sleep(3)
    if Reg5 == A:
        print('Reg5 Ok')
    sleep(3)
    if Reg6 == A:
        print('Reg6 Ok')
    sleep(3)
    if Reg7 == A:
        print('Reg7 Ok')
    sleep(3)
    if Reg8 == A:
        print('Reg8 Ok')
    sleep(3)
    for items in RAM:
        if items == A:
            print('RAM OK')

    SaveMEM('ALL', 0)
    ResetRAM()
    print('MEMtest Complete')

def AddMEM(Target, Value):
    global Reg1,Reg2,Reg3,Reg4,Reg5,Reg6,Reg7,Reg8,RAM
    if Target == 'Reg1':
        Reg1 = Value + Reg1
    if Target == 'Reg2':
        Reg2 = Value + Reg2
    if Target == 'Reg3':
        Reg3 = Value + Reg3
    if Target == 'Reg4':
        Reg4 = Value + Reg4
    if Target == 'Reg5':
        Reg5 = Value + Reg5
    if Target == 'Reg6':
        Reg6 = Value + Reg6
    if Target == 'Reg7':
        Reg7 = Value + Reg7
    if Target == 'Reg8':
        Reg8 = Value + Reg8
    if Target == 'ALL':
        AddMEM('Reg1', Value)
        AddMEM('Reg2', Value)
        AddMEM('Reg3', Value)
        AddMEM('Reg4', Value)
        AddMEM('Reg5', Value)
        AddMEM('Reg6', Value)
        AddMEM('Reg7', Value)
        AddMEM('Reg8', Value)
    
def SubMEM(Target, Value):
    global Reg1,Reg2,Reg3,Reg4,Reg5,Reg6,Reg7,Reg8,RAM
    if Target == 'Reg1':
        Reg1 = Value - Reg1
    if Target == 'Reg2':
        Reg2 = Value - Reg2
    if Target == 'Reg3':
        Reg3 = Value - Reg3
    if Target == 'Reg4':
        Reg4 = Value - Reg4
    if Target == 'Reg5':
        Reg5 = Value - Reg5
    if Target == 'Reg6':
        Reg6 = Value - Reg6
    if Target == 'Reg7':
        Reg7 = Value - Reg7
    if Target == 'Reg8':
        Reg8 = Value - Reg8
    if Target == 'ALL':
        SubMEM('Reg1', Value)
        SubMEM('Reg2', Value)
        SubMEM('Reg3', Value)
        SubMEM('Reg4', Value)
        SubMEM('Reg5', Value)
        SubMEM('Reg6', Value)
        SubMEM('Reg7', Value)
        SubMEM('Reg8', Value)
        
def MultiplyMEM(Target, Value):
    global Reg1,Reg2,Reg3,Reg4,Reg5,Reg6,Reg7,Reg8,RAM
    if Target == 'Reg1':
        Reg1 = Value * Reg1
    if Target == 'Reg2':
        Reg2 = Value * Reg2
    if Target == 'Reg3':
        Reg3 = Value * Reg3
    if Target == 'Reg4':
        Reg4 = Value * Reg4
    if Target == 'Reg5':
        Reg5 = Value * Reg5
    if Target == 'Reg6':
        Reg6 = Value * Reg6
    if Target == 'Reg7':
        Reg7 = Value * Reg7
    if Target == 'Reg8':
        Reg8 = Value * Reg8
    if Target == 'ALL':
        MultiplyMEM('Reg1', Value)
        MultiplyMEM('Reg2', Value)
        MultiplyMEM('Reg3', Value)
        MultiplyMEM('Reg4', Value)
        MultiplyMEM('Reg5', Value)
        MultiplyMEM('Reg6', Value)
        MultiplyMEM('Reg7', Value)
        MultiplyMEM('Reg8', Value)

if os.path.isfile('Assembly.txt') == False:
    fp = open('Assembly.txt', 'x')
    fp.close()
file = open('Assembly.txt', 'r')
while True:
    Instruction_RAW =  linecache.getline('Assembly.txt', LineNo)
    Instruction = Instruction_RAW.split(' ')
    OPCode, Target, Value = Instruction
    if OPCode == 'SaveMEM':
        SaveMEM(Target,int(Value))
    if OPCode == 'AddMEM':
        AddMEM(Target,int(Value))
        PrintMEM(Target)
    if OPCode == 'SubMEM':
        SubMEM(Target,int(Value))
        PrintMEM(Target)
    if OPCode == 'MultMEM':
        MultiplyMEM(Target,int(Value))
        PrintMEM(Target)
    if OPCode == 'PrintMEM':
        PrintMEM(Target)    
    if OPCode == 'MEMtest':
        MEMtest()
    if OPCode == 'GoTo':
        LineNo = int(Target)
    if OPCode == 'Halt':
        break
    if OPCode != 'GoTo':
        LineNo += 1
        Clock = Clock + 1
        print('Clock:', Clock)
    sleep(1)
