#!/bin/bash

cd vendas/backup

for arquivos in `ls -1 relatorio-*`
do
cat $arquivos >> relatorio_final.txt
done 