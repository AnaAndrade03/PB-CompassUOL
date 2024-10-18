E06
Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select 
	aut.codautor,
    aut.nome,
    (count (li.autor)) as quantidade_publicacoes
    
    FROM autor as aut
left join livro as li 
on aut.codautor = li.autor
    
group by li.autor 
order by quantidade_publicacoes desc
limit 1
