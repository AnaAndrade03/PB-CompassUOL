
E09
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas 
estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

select 
	vendas.cdpro,
    vendas.nmpro

from tbvendas as vendas

where (vendas.dtven between '2014-02-03' and '2018-02-02') and (vendas.status = 'Concluído')
order by vendas.nmpro
limit 1
