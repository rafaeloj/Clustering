import numpy as np
import pandas as pd
def main():
    caracteristicas = dict()
    caracteristicas =  {"1": "afeto inadequado; aparência ou comportamento", 
                        '2': "enxtrevista beligerância - negativismo;" ,
                        '3': "agitação - excitação; ",
                        '4': "retardo; ",
                        '5': "falta de emoções;" ,
                        '6': "desorganização da fala" ,
                        '7': "grandiosidade",
                        '8': 'suspeita - idéias de perseguição',
                        '9': "alucinações - delírios",
                        "10": "raiva evidente",
                        "11": "depressão",
                        "12": "ansiedade",
                        "13": "obsessão - compulsão",
                        "14": "suicídio",
                        "15": "automutilação",
                        "16": "preocupações somáticas",
                        "17": "isolamento social",
                        "18": "comprometimento da rotina diária",
                        "19": "comprometimento do tempo de lazer",
                        "20": "impulsos ou atos anti-sociais ",
                        "21": "abuso de álcool",
                        "22": "abuso de drogas",
                        "23": "desorientação",
                        "24": "comprometimento da memória",
                        "25": "pontos para a gravidade geral do distúrbio psiquiátrico",
                        "26": "Transtorno de Ansiedade",
                        "27": "Psicótico",
                        "28": "Abuso de substâncias"
    }

    for i in range(0,4):
        with open(f"caracteristicas{i}.dat",'w') as car:
            data = pd.read_csv(f"data{i}.dat")
            mat = np.array(data)
            contagem = [1 for i in range(0,28)]
            for i in range(len(mat)):
                lista = str(mat[i][0]).split()
                for j, v in enumerate(lista):
                    if(v != '0'):
                        contagem[j] += 1

            for i,v in enumerate(contagem):
                if v != 0:
                    car.write(f"{v}: {caracteristicas[f'{i+1}']} | {i+1}\n")




if __name__ =='__main__':
    main()