E08
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o 
status concluída. As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select 
	vendedor.cdvdd,
    vendedor.nmvdd

from tbvendedor as vendedor
left join tbvendas as vendas 
on vendedor.cdvdd = vendas.cdvdd

where vendas.status like 'Concluído'
group by vendas.cdvdd 
having count (vendas.cdvdd) >= 1
order by count (vendas.cdvdd) DESC
limit 1
