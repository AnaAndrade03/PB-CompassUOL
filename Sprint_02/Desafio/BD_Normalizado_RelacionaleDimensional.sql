--criando tabelas 
------------------
--tabela cliente
CREATE TABLE cliente ( 
	id_cliente int,
	nome_cliente varchar,
	cidade_cliente varchar,
	estado_cliente varchar,
	pais_cliente varchar,	
PRIMARY KEY (id_cliente)

);
--tabela vendedor 
CREATE TABLE vendedor ( 
	id_vendedor int,
	nome_vendedor varchar,
	sexo_vendedor smallint,
	estado_vendedor varchar,
PRIMARY KEY (id_vendedor)

);
--tabela locação 
CREATE TABLE locacao ( 
	id_locacao int,
	data_locacao datetime,
	hora_locacao time,
	quantidade_diaria int,
	valor_diaria decimal,
	data_entrega date,
	hora_entrega time,
	id_cliente int,
	id_vendedor int,
	id_carro int,
	id_combustivel int,
PRIMARY KEY (id_locacao)
FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
FOREIGN KEY (id_vendedor) REFERENCES vendedor (id_vendedor)
FOREIGN KEY (id_carro) REFERENCES carro (id_carro)

);
--tabela carro pk and fk
CREATE TABLE carro ( 
	id_carro int,
	km_carro int,
	classificacao_carro varchar,
	marca_carro varchar,
	modelo_carro varchar,
	ano_carro int,
	id_combustivel int,
		
PRIMARY KEY (id_carro)
FOREIGN KEY (id_combustivel) REFERENCES combustivel (id_combustivel)

);
	
);
--tabela combustivel 
CREATE TABLE combustivel ( 
	id_combustivel int,
	tipo_combustivel varchar,

PRIMARY KEY (id_combustivel)

);

--alocando dados nas tabelas criadas 
-------------------------------------
--tabela carro 
--selecionando apenas a quilometragem mais alta como item kmcarro
INSERT INTO carro (id_carro, km_carro, classificacao_carro, marca_carro, modelo_carro,ano_carro,id_combustivel)
SELECT DISTINCT idCarro, (SELECT MAX(kmCarro)
FROM tb_locacao tb_locacao2 
WHERE tb_locacao2.idcarro = tb_locacao.idCarro 
GROUP BY idCarro) AS kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel 
FROM tb_locacao 

-- tabela cliente 
INSERT INTO cliente (id_cliente, nome_cliente, cidade_cliente, estado_cliente, pais_cliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente FROM tb_locacao 

-- tabela combustivel 
INSERT INTO combustivel (id_combustivel, tipo_combustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel FROM tb_locacao 

-- tabela locacao
INSERT INTO locacao (id_locacao, data_locacao, hora_locacao, quantidade_diaria, valor_diaria, data_entrega, hora_entrega, id_cliente, id_vendedor, id_carro, id_combustivel)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCLiente,idVendedor, idCarro, idCombustivel FROM tb_locacao

--Modelagem dimensional 
-- Criando views para tabelas dimensão

--dim carro
CREATE VIEW dim_carro AS 
SELECT id_carro AS id_carro,
       km_carro AS km_carro,
       classificacao_carro AS classificacao_carro,
       marca_carro AS marca_carro,
       ano_carro AS ano_carro,
       id_combustivel AS id_combustivel
       FROM carro c;
      
-- dim cliente
CREATE VIEW dim_cliente AS 
SELECT id_cliente AS id_cliente,
       nome_cliente AS nome_cliente,
       cidade_cliente AS cidade_cliente,
       estado_cliente AS estado_cliente,
       pais_cliente AS pais_cliente
       FROM cliente c;
      
-- dim combustivel 
CREATE VIEW dim_combustivel AS 
SELECT id_combustivel AS id_combustivel,
       tipo_combustivel AS tipo_combustivel
       FROM combustivel c;
      
--dim vendedor 
CREATE VIEW dim_vendedor AS 
SELECT id_vendedor AS id_vendedor,
       nome_vendedor AS nome_vendedor,
       sexo_vendedor AS sexo_vendedor,
       estado_vendedor AS estado_vendedor 
       FROM vendedor v;     


-- criando view da fato
CREATE VIEW fato_locacao AS 
SELECT id_locacao AS id_locacao,
	   id_cliente AS id_cliente,
       id_vendedor AS id_vendedor,
       id_carro AS id_carro, 
       id_combustivel AS id_combustivel,
       data_locacao AS data_locacao,
       hora_locacao AS hora_locacao,
       quantidade_diaria AS quantidade_diaria,
       valor_diaria AS valor_diaria,
       data_entrega AS data_entrega,
       hora_entrega AS hora_entrega
       FROM locacao l;
      
       
   SELECT *
   FROM locacao l       
 
   
   
   