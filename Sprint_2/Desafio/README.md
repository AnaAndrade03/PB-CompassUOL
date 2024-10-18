### 1. Primeira etapa 
#### (criando tabelas para normalização)
  Primeiramente, criei todas tabelas que julguei necessárias com suas respectivas pks e fk. 

![evidenciauno](../Evidências/desafio1.png)
![evidenciatwo](../Evidências/desafio2.png)

### 2. Segunda etapa 
#### (alocando dados nas tabelas criadas)
  Depois disso inseri os dados contidos na tb_locação para as novas tabelas relacionais criadas dando atenção ao item kmcarro que foi usado um subselect para selecionar apenas a quilometragem mais atual do carro na tabela normalizada.

![evidenciatrois](../Evidências/desafio3.png)

### 3. Terceira etapa 
#### (Criando a modelagem dimensional)
  Depois de terminada a modelagem relacional, parti para a modelagem dimensional usando as tabelas que foram normalizadas na modelagem relacional,. criando views para as tabelas dimensões e fato

![evidenciavier](../Evidências/desafio4.png)

#### Tabelas e views no banco de dados

![evidenciacinque](../Evidências/desafio7.png)

### Diagrama das tabelas criadas na modelagem 
#### modelagem relacional

![evidenciacinque](../Evidências/desafio5.png)

#### modelagem dimensional 

![evidenciacinque](../Evidências/desafio6.png)
  
