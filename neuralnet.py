import numpy as np
import neurolab as nl
import database
import csv

class NeuralNet:

    def __init__(self, db):
        inputData = []
        for row in db.getTableSnapshot("LocationHistory"):
            strOut += str(row[1]) + "\t" + str(row[2]) + "\n"
            inputLine = [row[1], row[2]]
            inputData.append(inputLine)
        self.net = nl.net.newff([[0, 1], [0, 1]], [4, 1], transf=[nl.trans.LogSig()] * 2)
        target = [0, 1]
        error = self.net.train(inputData,target, epochs=500, show=100, goal=0.02)
        #out = self.net.sim()
        self.net.train.train_gdx()

    def simulate(self, input):
        out = self.net.sim(input)
        return out
