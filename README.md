# Trabalho de aprendizado de máquinas
#### Rafael de Oliveira Jarczewski - 1901570170

## -----------------------
## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cluster.py      
## -----------------------

Para a confexão desse trabalho foi feito um algortimo principal cluster.py que irá aplicar de fato a clusterização.
Para qualquer nova execução os arquivos com os clusters descobertos serão armazenados na pasta "novos_testes"

## Um breve exemplo de execução:

| ~$python3 cluster.py -cn 3 -f arquivo_de_entrada.py -d ',' -v True

*  -cn define a quantidade clusters desejado
*  -f define o arquivo que de entrada
*  -d define qual seria o separador para os itens
*  -v ativara a vizualização em tempo real da convergência dos clusters

## -----------------------
## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graph.py        
## -----------------------

Esse arquivo pega os dados salvos em quadrado.dat com a chamada da método multiplos_testes e produz o calculo para o melhor k juntamente com o gráfico

<img src="https://github.com/rafaeloj/Clustering/blob/master/3.MopsiLocationsUntil2012-Finland_clusters_gerados/soma_total_dos_quadrados.png" width="500"><img src="https://github.com/rafaeloj/Clustering/blob/master/2.MopsiLocations2012-Joensuu_Clusters_gerados/grupos_formados.png" width="500">
