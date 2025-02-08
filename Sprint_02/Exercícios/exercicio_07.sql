E07
Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

select 
 aut.nome

from autor as aut
left join livro as li 
on aut.codautor = li.autor
where cod is NULL
