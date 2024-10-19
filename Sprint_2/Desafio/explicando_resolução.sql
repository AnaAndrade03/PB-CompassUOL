Resolução desafio SQL
-Primeiramente foi disponibilizado um arquivo que continha um banco de dados com apenas uma tabela que continha
todos registro de uma concessionário de aluguel de veiculos automotivos

-Comecei fazendo as primeiras normalizaçoes criando tabelas para as entidades e suas respectivas informaçoes,
criei então a tabela "carro", "cliente", "combustivel", "locação", e "vendedor" com suas respecctivas pks e fks,
dando atenção as tabelas locação que contem uma pk e 3 fks e a tabela carro ue contem uma pk e uma fk, o id combustivel
é a pk na tabela combustivel já que o tipo combustivel não era cabivel estar na tabela carro pois ele não dependende
inteiramente da pk id_carro.

-Depois de todas tabelas criadas comecei inserindo todos arquivos que pertenciam as entidades nas tabelas,
na tabela carro foi inserido apenas a quilomatragem mais atual do carro alugado considerando assim essa informação 
uma caracteristica do carro, nas outras tabelas também foram inseridas as caracterias de cada entidade com algumas 
mudanças de nomenclatura.

-Com a tabela normalizada na forma relacional parti para a modelagem dimensional, para isso fiz uso da criação de views, com isso criei uma 
view dimensão de quatro tabelas e uma view da tabela fato. 
