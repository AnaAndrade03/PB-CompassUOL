E05
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

select distinct autor.nome
	from autor 
	left join livro 
on autor.codautor = livro.autor
	left join editora 
on livro.editora = editora.codeditora
	left join endereco
on editora.endereco = endereco.codendereco

where endereco.estado not in ('RIO GRANDE DO SUL', 'PARANÁ')
order by autor.nome
