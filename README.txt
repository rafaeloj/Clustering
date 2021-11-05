# Trabalho de aprendizado de máquinas
# Rafael de Oliveira Jarczewski - 1901570170


# Ainda estou aprendendo como organizar um "projeto", então o que eu pensei nesse momento foi produzir um readme.txt para cada pasta
#eles ficaram curtos, e talvez sejam redundantes, ainda estou experimentanto modelos de organização.

# -----------------------
#        cluster.py      
# -----------------------

# Para a confexão desse trabalho foi feito um algortimo principal cluster.py que irá aplicar de fato a clusterização
#muitos detalhes de como utilizar se encontram no relatório. 
# Para qualquer nova execução os arquivos com os clusters descobertos serão armazenados na pasta "novos_testes"
# Um breve exemplo de execução:

| ~$python3 cluster.py -cn 3 -f arquivo_de_entrada.py -d ',' -v True

*  -cn define a quantidade clusters desejado
*  -f define o arquivo que de entrada
*  -d define qual seria o separador para os itens
*  -v ativara a vizualização em tempo real da convergência dos clusters

# -----------------------
#        graph.py        
# -----------------------

# Esse arquivo pega os dados salvos em quadrado.dat com a chamada da método multiplos_testes 
# e produz o calculo para o melhor k juntamente com o gráfico
