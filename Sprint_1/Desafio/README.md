### 1. Primeira etapa
  Primeiramente criei o diretório solicitado, movi o ariquivo dados de vendas para dentro deste dirório e logo após criei o arquivo executável.

### 2. Segunda etapa
  Depois disso já dentro do arquivo criei um scrip em bash, lá usei alguns comandos para criação de diretórios, copia e mudança de nomes de arquivos, então fiza criação do do relatório.txt onde terá algumas informações e para estas usei comandos especificos que as representasse, após isso fiz um zip em um arquivo e deletei outros solicitados.

### 3. Terceira etapa 
  Fiz o agendamento da execução no scheduler crontab para executar o arquivo processamento de vendas de segunda a quinta às 15:27.

### 4. Quarta etapa 
  Criei mais um script em bash desta vez para consolidar todos o srelatórios que seriam gerados em um só usando um loop.

### 5. Quinta etapa
  Todos os dias de execução o arquivo dados de vendas.csv era modificado manualmente.

### 6. Sexta etapa
  Depois de todas as execuções agendadas no crontab, executei manualemnte o o segubdo script que consolidade todos.

  
