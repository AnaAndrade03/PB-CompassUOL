E12
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
Observação: Apenas vendas com status concluído.

with vendedor as (
    select cdvdd,
           sum(vendas.qtd * vendas.vrunt) as valor_total_vendas
    from tbvendas as vendas
    where status = 'Concluído'
    group by cdvdd
    order by valor_total_vendas
    limit 1
)

select distinct
    dep.cddep,
    dep.nmdep,
    dep.dtnasc,
    valor_total_vendas

from tbdependente as dep
    left join vendedor
        on dep.cdvdd = vendedor.cdvdd

where valor_total_vendas >0
order by valor_total_vendas
