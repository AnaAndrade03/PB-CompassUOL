#!/bin/bash
cd /home/ana-andrade/Documents/Projetos/ecommerce
#criação do diretório de vendas
echo "criando diretorio de vendas.."
mkdir vendas

#movendo o arquivo para pasta de vendas 
cp dados_de_vendas.csv vendas

#criando diretporio backup dentro do diretorio vendas
mkdir vendas/backup

#copia do dados_de_vendas.csv para backup mundando o seu nome + data dinamica
cp dados_de_vendas.csv vendas/backup/dados_de_vendas-$(date +"%Y%m%d").csv

# dentro do backup renomeio 
cd vendas/backup
mv dados_de_vendas-$(date +"%Y%m%d").csv backup-dados-$(date +"%Y%m%d").csv

cat <<EOF > relatorio-$(date +"%Y%m%d").txt
Data do sistema operacional: $(date +"%Y/%m/%d %H:%M")
Data do primeiro registro de vendas: $(awk -F, 'NR==2 {print $5}' backup-dados-$(date +"%Y%m%d").csv)
Data do ultimo registro de venda: $(awk -F, 'END {print $5}' backup-dados-$(date +"%Y%m%d").csv)
Quantidade total de itens diferentes vendidos: $(awk -F, 'NR>1 {print $2}' backup-dados-$(date +"%Y%m%d").csv | sort |uniq | wc -l)

Primeiras dez linhas do arquivo:
$(head -n10 backup-dados-$(date +"%Y%m%d").csv)
EOF

#comprimindo o arquivo backup de dados e deletando a orgem (backup de dados)
zip -m backup-dados-$(date +"%Y%m%d").zip backup-dados-$(date +"%Y%m%d").csv

#deletando dados de vendas 
cd ..
rm dados_de_vendas.csv


