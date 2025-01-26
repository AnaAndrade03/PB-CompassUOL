### Desafio Final: Entrega 4.

### 1. Primeira etapa.
#### (Criando e configurando o primeiro job para processar o arquivo CSV)

- *Processei apenas o arquivo sobre séries porque não irei usar o arquivo sobre filmes na minha análise.*

![evidenciauno](../Evidências/Evidências_Desafio/01.png)
![evidenciauno](../Evidências/Evidências_Desafio/02.png)

- *definindo variável de ambiente para mehor visualização no código*

![evidenciauno](../Evidências/Evidências_Desafio/03.png)

### 1.1 código que processa o arquivo CSV e faz algumas alterações no mesmo.

- *deleção de colunas sobre atores que não serão usadas*
- *conversão de datatype para melhor manipulação futuramente*
- *filtragem de registros a partir de 2010*
- *filtragem de séries que continham pelo menos um dos gêneros (Sci-Fi ou Fantasia)*
- *deleção de linhas repetidas*

![evidenciauno](../Evidências/Evidências_Desafio/04.png)
![evidenciauno](../Evidências/Evidências_Desafio/05.png)
![evidenciauno](../Evidências/Evidências_Desafio/06.png)

### 2. Segunda etapa.
#### (Criando e configurando o segundo job para processar os arquivos JSON.)

![evidenciauno](../Evidências/Evidências_Desafio/07.png)
![evidenciauno](../Evidências/Evidências_Desafio/08.png)

- *definindo variável de ambiente para mehor visualização no código*

![evidenciauno](../Evidências/Evidências_Desafio/09.png)

### 2.2 código que processa os arquivos JSON (três top 10, ordenados cada um por uma variável).

- *A alteração nos arquivos foi a coluna "Provedores de Streaming", deixando-as com uma melhor visualização*

![evidenciauno](../Evidências/Evidências_Desafio/10.png)
![evidenciauno](../Evidências/Evidências_Desafio/11.png)
![evidenciauno](../Evidências/Evidências_Desafio/12.png)

### 3. Terceira etapa.
#### (Rodandos os jobs)

![evidenciauno](../Evidências/Evidências_Desafio/13.png)
![evidenciauno](../Evidências/Evidências_Desafio/14.png)

### 4. Quarta etapa.
#### (Resultados: Caminhos no padrão determinado do bucket)

![evidenciauno](../Evidências/Evidências_Desafio/15.png)
![evidenciauno](../Evidências/Evidências_Desafio/16.png)

### 5. Resultados. 
#### (Criando database e crawler para checagem de resultados no athena)

![evidenciauno](../Evidências/Evidências_Desafio/17.png)

### 6. Resultados.
#### (Tabelas criadas depois do crawler rodado)

![evidenciauno](../Evidências/Evidências_Desafio/18.png)

### 7. Resultados.
#### (Tabela do CSV)
![evidenciauno](../Evidências/Evidências_Desafio/19.png)
![evidenciauno](../Evidências/Evidências_Desafio/20.png)

### 7. Resultados.
#### (Tabela dos JSONS)
![evidenciauno](../Evidências/Evidências_Desafio/21.png)
![evidenciauno](../Evidências/Evidências_Desafio/22.png)
