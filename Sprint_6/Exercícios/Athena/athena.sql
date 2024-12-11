-- criação da tabela 
CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.minhatabela(
  Nome STRING,
  Sexo STRING,
  Total INT, 
  Ano INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION 's3://bucketdesafio/dados/'

-- consulta teste 
SELECT nome
FROM meubanco.minhatabela
WHERE ano = 1999 
ORDER BY total 
LIMIT 15;

-- consulta lista com os 3 nomes mais usados em cada década desde o 1950 até hoje 
WITH Decenarios AS (
    SELECT 
        nome,
        sexo,
        total,
        ano,
        FLOOR(ano / 10) * 10 AS decada
    FROM meubanco.minhatabela
    WHERE ano >= 1950
),
RankedNames AS (
    SELECT 
        decada,
        nome,
        SUM(total) AS total_decada,
        ROW_NUMBER() OVER (
            PARTITION BY decada ORDER BY SUM(total) DESC
        ) AS rank
    FROM Decenarios
    GROUP BY decada, nome
)
SELECT 
    decada,
    nome,
    total_decada,
    rank
FROM RankedNames
WHERE rank <= 3
ORDER BY decada ASC, rank ASC;

