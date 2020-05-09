import math
import heapq
import csv
def printBipedalDinosaursOrderBySpeed(filePathDinoInfo, filePathAddInfo):
    bipedalDinosaurs = {}
    g = 9.8
    with open(filePathAddInfo, 'r') as f:
        line = csv.reader(f)
        #print (line)
        while line:
            line = f.readline().strip()
            #print (line)
            if line:
                NAME, STRIDE_LENGTH, STANCE = line.split(',')
                if STANCE == "bipedal":
                    bipedalDinosaurs[NAME] = float(STRIDE_LENGTH)
    
    with open(filePathDinoInfo, 'r') as f:
        line = csv.reader(f)
        while line:
            line = f.readline().strip()
            if line:
                NAME, LEG_LENGTH, DIET = line.split(',')
                if NAME in bipedalDinosaurs:
                    STRIDE_LENGTH, LEG_LENGTH = bipedalDinosaurs[NAME], float(LEG_LENGTH)
                    bipedalDinosaurs[NAME] = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)
    
    #print ([key for key, value in sorted(bipedalDinosaurs.items(), key = lambda kv: kv[1], reverse=True) ])
    for key, value in sorted(bipedalDinosaurs.items(), key = lambda kv: kv[1], reverse=True):
        print("%s: %s" %(key, value))

printBipedalDinosaursOrderBySpeed('dataset_1.csv', 'dataset_2.csv')
