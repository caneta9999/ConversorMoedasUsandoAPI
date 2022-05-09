import random
import pandas as pd
import bar_chart_race as bcr
import warnings
warnings.filterwarnings("ignore")
class Corrida:
    def __init__(self,tempoCorrida):
        self.tempoCorrida = tempoCorrida
        self.distancias = [[],[],[],[],[]]
        self.iniciarCorrida()
    def iniciarCorrida(self):
        contadorTempo = -1
        while not contadorTempo > self.tempoCorrida-1:
            contadorTempo += 1
            if(contadorTempo == 0):
                self.sortearVelocidade(0)
            else:
                self.sortearVelocidade()
        self.mostrarCorrida()
    def sortearVelocidade(self, tempo = 1):
        if(tempo == 0):
            for distancia in self.distancias:
                distancia.append(0)
        else:
            for distancia in self.distancias:
                distancia.append(random.randint(1,100) + distancia[-1])
    def mostrarCorrida(self):
        distanciasDataframe = pd.DataFrame(self.distancias[0],columns=['Participante 1'])
        for i in range(1,len(self.distancias)):
            distanciasDataframe['Participante ' + str(i+1)] = self.distancias[i]
        print(distanciasDataframe)
        bcr.bar_chart_race(distanciasDataframe,filename='test_barchartrace.mp4',period_length=self.tempoCorrida*200)
Corrida(10)
                    
                
