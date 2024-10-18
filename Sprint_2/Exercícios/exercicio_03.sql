E03
 Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade.
Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

select
    count (l.editora) as quantidade,
    e.nome,
    end.estado,
    end.cidade

from livro as l
    left join editora as e
    on l.editora = e.codeditora
    left join endereco as end
    on e.endereco = end.codendereco
group by l.editora 
order by quantidade desc
