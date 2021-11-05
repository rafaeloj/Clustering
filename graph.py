import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("variancia.dat",sep=' ')
    # print(np.array(data)[::,1:2:])
    plt.xlabel('Numero de clusters')
    plt.ylabel('Soma total dos quadrados intra-clusters')
    axis_x = np.array(data)[::,0:1:]
    axis_y = np.array(data)[::,1:2:]
    x1 = axis_x[0]
    y1 = axis_y[0]
    x2 = axis_x[-1]
    y2 = axis_y[-1]
    x0 = axis_x[0]
    y0 = axis_y[0]
    y_y = (y2 - y1)*x0
    x_x = (x2 - x1)*y0
    x_y = x2*y1
    y_x = y2-x1
    dist = np.sqrt((y2-y1)**2 + (x2-x1)**2)
    result = np.abs(y_y - x_x + x_y - y_x)/dist
    index = 2 # primeiro cluster
    for i in range(1,len(axis_x)):
        x0 = axis_x[i]
        y0 = axis_y[i]
        y_y = (y2 - y1)*x0
        x_x = (x2 - x1)*y0
        x_y = x2*y1
        y_x = y2-x1
        dist = np.sqrt((y2-y1)**2 + (x2-x1)**2)
        aux = np.abs(y_y - x_x + x_y - y_x)/dist
        if(aux > result):
            result = aux
            index = (i+2) # +2 Porque para meus testes eu começo com 2 clusters
    print(f"O ponto mais dinstante entre as retas é correspondente ao cluster {index}")
    plt.title('case_study_psychiatrist')
    plt.plot([axis_x[0],axis_x[-1]],[axis_y[0],axis_y[-1]],label='ligação entre os extremos')
    plt.plot(axis_x,axis_y,label='Curva das somas quadráticas')
    plt.plot(axis_x,axis_y,'bo')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()