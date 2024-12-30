### Desafio Final: Entrega 2.

### 1. Primeira etapa.
#### (Criando camada do tmdb para uso no lambda.)
- *Arquivo Dockerfile*
- *Criação da imagem*
  
![evidenciauno](../Evidências/Evidências_Desafio/01.png)

- *Criação do container, pastas e instalação da api no pacote que será transformado em camada*

![evidenciauno](../Evidências/Evidências_Desafio/02.png)
![evidenciauno](../Evidências/Evidências_Desafio/03.png)

- *Zipando a pasta e fazendo uma copia para o path definido*

![evidenciauno](../Evidências/Evidências_Desafio/04.png)
![evidenciauno](../Evidências/Evidências_Desafio/05.png)

### 2. Segunda etapa.
#### (Subindo apasta zipada para um bucket no S3.)
![evidenciauno](../Evidências/Evidências_Desafio/07.png)

- *Criação da função-tmdb*

![evidenciauno](../Evidências/Evidências_Desafio/06.png)

- *Criação da camada*
- *Adicionando camada*

![evidenciauno](../Evidências/Evidências_Desafio/08.png)

### 3. Terceira etapa.
#### (Definindo variável de ambiente para melhor prática no código)

![evidenciauno](../Evidências/Evidências_Desafio/10.png)

### 4. Quarta etapa.
#### (Elaboração do código para coleta de dados da API e produção dos arquivos json a serem enviados para o bucket anas-data-lake)

- *Prints no vscode local para melhor visualização*

![evidenciauno](../Evidências/Evidências_Desafio/11.png)
![evidenciauno](../Evidências/Evidências_Desafio/12.png)
![evidenciauno](../Evidências/Evidências_Desafio/13.png)

### 5. Resultados. 
#### (Código rodado no lambda com sucesso)
![evidenciauno](../Evidências/Evidências_Desafio/14.png)
![evidenciauno](../Evidências/Evidências_Desafio/15.png)

- (Caminhos no bucket e diretórios corretos como solicitado)

![evidenciauno](../Evidências/Evidências_Desafio/16.png)
![evidenciauno](../Evidências/Evidências_Desafio/17.png)
![evidenciauno](../Evidências/Evidências_Desafio/18.png)

### 6. Resultados.
#### (Arquivos gerados pelo código depois de feito download na maquina local)
![evidenciauno](../Evidências/Evidências_Desafio/19.png)
![evidenciauno](../Evidências/Evidências_Desafio/20.png)
![evidenciauno](../Evidências/Evidências_Desafio/21.png)
