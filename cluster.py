import matplotlib.pyplot as plt

import numpy as np
import argparse
import pandas as pd
from random import randint

DEFAULT_FILE = "MopsiLocations2012-Joensuu.txt"
DEFAULT_CLUSTER_NUMBER = 3
DEFAULT_CYCLES_TRAINING = 1000
DEFAULT_VISUALIZATION = False
DEFAULT_DILIMITER = ' '

class Kmeans():
    def __init__(self, data):
        self.cluster = data
        self.kmeans = []

    def init(self,number_of_cluter):
        """
            number_of_cluster: Is amount of cluster you want clustering.
            Non return, separates the data on the self.cluster in the quantity of number cluster wished
        """
        self.cluster_number = number_of_cluter
        self.colors = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        self.kcolor = [self.generate_color(6) for i in range(self.cluster_number)]

        size = len(self.cluster)

        random_number = sorted([(randint(0,size-1))+i for i in range(number_of_cluter)])
        for i in range(0,number_of_cluter):
            self.kmeans.append(self.cluster[random_number[i]:random_number[i]+1:,::][0])
        aux = [[] for j in range(0,number_of_cluter)]
        for i in range(0, len(self.cluster)):
            index = 0
            dist = self.distance(self.cluster[i], self.kmeans[0])
            for k in range(1,len(self.kmeans)):
                d_aux = self.distance(self.cluster[i], self.kmeans[k])
                if(d_aux < dist):
                    dist = d_aux
                    index = k
            aux[index].append(self.cluster[i])
        for i in range(0,self.cluster_number):
            aux[i] = np.array(aux[i])

        self.cluster = aux

    def generate_color(self,n=8):
        c = ''
        for i in range(0,n):
            c += self.colors[randint(0,len(self.colors)-1)]
        return c

    def media(self):
        """
            It's calculated the mean of clusters and save in the self.kmeans
        """
        self.kmeans = [[] for i in range(0,self.cluster_number)]
        for i in range(self.cluster_number):
            for j in range(0,len(self.cluster[i][0])):
                self.kmeans[i].append(np.sum(self.cluster[i][::,j:j+1:])/len(self.cluster[i][::,j:j+1:]))
                
    def distance(self,p1, p2):
        """
            p1: It's a point in the cluster of the database
            p2: It's a mean of a cluster
        """
        soma = 0
        for i in range(0,len(p1)):
            soma += (p1[i] -  p2[i])**2
        return np.sqrt(soma)

    def convergencia(self, cycles_number=0, v = False,time=0.5):
        """
            cycles_number: It's number of cycles for a convergention.
            v: Choosess True if you want see the process of clustering.
        """
        if cycles_number == 0:
            cycles_number = 1
            conv = True
        else:
            conv = False
            while cycles_number > 0:
                self.change = False
                aux = [[]for i in range(0,self.cluster_number)]
                self.media()
                for i in range(0, self.cluster_number):
                    for j in range(0,len(self.cluster[i])):
                        dist = self.distance(self.cluster[i][j], self.kmeans[0])
                        index = 0
                        for k in range(1,len(self.kmeans)):
                            d_aux = self.distance(self.cluster[i][j], self.kmeans[k])
                            if(d_aux < dist):
                                dist = d_aux
                                index = k
                        if index != i:
                            self.change = True
                        aux[index].append(self.cluster[i][j])
                for i in range(0,self.cluster_number):
                    aux[i] = np.array(aux[i])
                if v:
                    for i in range(0,self.cluster_number):
                        plt.plot(self.cluster[i][::,0:1:],self.cluster[i][::,1:2:],"o",color=f'#{self.kcolor[i]}')
                    plt.show(block=False)
                    plt.pause(time)

                self.cluster = aux
                # print(self.kmeans)
                if not self.change:
                    return
                if not conv:
                    cycles_number -= 1

    def soma_quad(self):
        soma = 0
        for i in range(0,self.cluster_number):
            for j in range(0,len(self.cluster[i])):
                soma += self.distance(self.cluster[i][j],self.kmeans[i])
        return soma

    def multiplos_testes(self,n):
        aux = self.cluster
        with open('quadrado.dat','w') as q:
            q.write("X Y\n")
            for i in range(2,n):
                c = Kmeans(aux)
                # c.init(args.cluster_number)
                c.init(i)
                c.convergencia(1000)
                result = c.soma_quad()
                q.write(f'{i} {result}\n')

def main():

    parser = argparse.ArgumentParser(description="Flags for program")
    parser.add_argument("--inputfile","-f",help="File with points in the Cartesian plane",default=DEFAULT_FILE,type=str)
    parser.add_argument("--delimiter","-d",help="The delimiter to separate items in the file, if the delimiter is type '\' use $ for literal character",default=DEFAULT_DILIMITER,type=str)
    parser.add_argument("--cluster_number","-cn",help="Number of cluster that you want",default=DEFAULT_CLUSTER_NUMBER,type=int)
    parser.add_argument("--cycles","-c",help="Number of cycles for training",default=DEFAULT_CYCLES_TRAINING,type=int)
    parser.add_argument("--visualization","-v   ",help="True if you want see the process of clustering",default=DEFAULT_VISUALIZATION,type=bool)

    args = parser.parse_args()
    print("Você pode selecionar argumentos para o código, para verificar quais argumentos estão disponiveis utilize --help")
    data = pd.read_csv(args.inputfile,sep=args.delimiter)

    dados = np.array(data)
    c =Kmeans(dados)
    c.init(args.cluster_number)
    c.convergencia(args.cycles,v=args.visualization)
    # c.multiplos_testes(12)
    # Caso queira vizualizar no final da convergência
    if(args.visualization == True):
        plt.title(args.inputfile)
        for i in range(0,c.cluster_number):
            plt.plot(c.cluster[i][::,0:1:],c.cluster[i][::,1:2:],"o",color=f'#{c.kcolor[i]}', label=f'K{i}')
            plt.plot(c.kmeans[i][0],c.kmeans[i][1],'o',color=f'#{c.generate_color(6)}',label=f"Centroide {i}")
        plt.legend()
        plt.show()

    # Caso queira salvar os datasets separados

    # for l,value in enumerate(c.cluster):
    #     with open(f'novos_testes/{l}.dat', 'w') as f:
    #         for j in range(0,len(value)):
    #             for k in range(0,len(value[j])):
    #                 f.writelines(f"{value[j][k]} ")
    #             f.writelines(f"\n")

if __name__=='__main__':
    main()
