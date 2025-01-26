### Desafio Final: Entrega 4.

### 1. Primeira etapa.
#### (Criando modelagem multidimensional no dbeaver para visualização do diagrama)

1. Preferi começar por aqui para conseguir visualizar o diagrama e conseguir pensar melhor em como queria minhas tabelas.

- *Tabelas sem modelagem.*

![evidenciauno](../Evidências/02.png)

- *Criando tabelas.*
  
![evidenciauno](../Evidências/01.png)

- *Diagrama representando a modelagem multidimensional.*

![evidenciauno](../Evidências/03.png)

- *Tabelas.*
  
![evidenciauno](../Evidências/04.png)

### 2. Segunda etapa.
#### (Criação do job Glue)

- *Realiza o processamento e transformação de dados para montar uma modelagem multidimensional.*
  
1. Faço algumas inicializações.
     
2. Defino variáveis globais.
     
3. Inicializo leitura dos arquivos que tiveram seus caminhos definidos como variáveis de ambiente.
     
![evidenciauno](../Evidências/05.png)

### 2.2

4. Faço a seleção de colunas do json e csv, renomeio colunas para melhor visualização.
  
5. Crio tabela diemnsão fazendo um join entre os dois documentos baseando-se na correspondencia entre as colunas "titulo" e "titulo_original"
 
6. A coluna "streaming" é "explodida" já que é uma lista, e caqda série pode contar com mais de um provedor de streaming.

    - *Preferi usar essa saída ao invés de criar uma tabela auxiliar, como são poucos dados não irá influir na hora de fazer as views*
  
7. Crio a tabela fato fazendo um select em quais colunas quero adicionar.

![evidenciauno](../Evidências/06.png)

### 2.3

8. Salvo minhas tabelas no caminho definido no S3.

![evidenciauno](../Evidências/07.png)

### 2.4 Visualização na plataforma da AWS e resultados.

- *Job e suas configurações pedidas.*

![evidenciauno](../Evidências/08.png)
![evidenciauno](../Evidências/09.png)

- *Definindo variáveis de ambiente.*

![evidenciauno](../Evidências/10.png)

- *Job rodado com sucesso*

![evidenciauno](../Evidências/11.png)

- *Camada Refined no S3.*

![evidenciauno](../Evidências/12.png)
![evidenciauno](../Evidências/13.png)

- *Caminhos dos parquets criados*

![evidenciauno](../Evidências/14.png)
![evidenciauno](../Evidências/15.png)
     

### 3. Terceira etapa.
#### (Criando database e crawler)

- *Database seriesrefined*

![evidenciauno](../Evidências/16.png)

- *Crawler seriesrefined rodado com criação de duas tabelas com sucesso!*

![evidenciauno](../Evidências/17.png)

- *Visualização das tabelas criadas com o crawler.*

![evidenciauno](../Evidências/18.png)

### 4. Quarta etapa.
#### (Visualização das tabelas criadas no Athena.)

![evidenciauno](../Evidências/19.png)

- *dim_series*

![evidenciauno](../Evidências/20.png)
![evidenciauno](../Evidências/21.png)

- *fato_series*

![evidenciauno](../Evidências/22.png)
![evidenciauno](../Evidências/23.png)
