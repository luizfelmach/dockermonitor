# dockermonitor

*PARA QUE SERVE?*

Este script foi criado com o intuito de monitorar os containers docker e enviar um email caso algum dos containers encerre o servico com o status code diferente de 0.


*COMO FUNCIONA?*

## Encerrar o programa
 **Este programa está rodando em background, portanto, para encerrar sua execução é necessário realizar os seguintes passos**

 - Digite o comando *top* no terminal. Este comando mostrará todos os processos em execução na VM e suas respectivas informações.
 - Procure pela execução com o nome *python3* realizado pelo user *pet* e o número de seu PID
 - Substitua a palavra PID no comando a seguir pelo respectivo numero: "kill PID"


## Trocar o remetente
 - Para trocar o remetente do email enviado pelo script, substitua o email do campo RECEIVER no arquivo *.env* que se encontra na pasta root do projeto. Lembre-se de que o arquivo *.env* é oculto e pode ser visto utilizando o comando *ls -a*.


## Executar o programa
 - Como estamos numa conexao via SSH, se executarmos o programa normalmente ou mesmo em segundo plano com o "&" no final, assim que fecharmos a conexão, a execucao se encerrará. Sendo assim, entre na pasta *src* e digite o comando abaixo:

```bash
nohup python3 main.py &
```


*!OBSERVACOES*
 - Caso a senha de aplicativo do email petengcomp.ufes@gmail.com seja alterada, lembre-se de alterá-la no ".env" tambem (:
 - Dentro da pasta *test* há um código para buildar um container de teste. Este container comeca a rodar e em alguns segundos gera um erro. O intuito e rodar este container e verificar se o script registra sua paralização.
 - Dentro da pasta *src* ha um arquivo chamado *nohup.out*. Este arquivo é responsavel por guardar os logs da execução do programa que esta em background, portanto, não mexa neste arquivo.
