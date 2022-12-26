# dockermonitor

*PARA QUE SERVE?*
Este script foi criado com o intuito de monitorar os containers docker e enviar um email caso algum dos containers encerre o servico com o status code diferente de 0.


*COMO FUNCIONA?*

## Encerrar o programa
 **Este programa estárodando em background, portanto, para encerrar sua execucao e necessario realizar os seguintes passos**

 - Digite o comando "top" no terminal. Este comando ira mostrar todos os processos em execucao na VM e suas respectivas informacoes
 - Procure pela execucao com o nome "python3" realizado pelo user "pet" e o numero de seu PID
 - Substitua a palavra PID no comando a seguir pelo respectivo numero: "kill PID"


## Trocar o remetente
-> Para trocar o remetente do email enviado pelo script, substitua o email do campo RECEIVER no arquivo ".env" que se encontrar na   pasta root do projeto.Lembre-se de que o arquivo ".env" e oculto e pode ser visto utilizando o comando "ls -a".


## Executar o programa
 - Como a estamos numa conexao via ssh, se executarmos o programa normalmente ou mesmo em segundo plano com o "&" no final, assim que fecharmos a conexao, a execucao se encerrara. Sendo assim, entre na pasta src e digite o comando abaixo:

```bash
nohup python3 main.py &
```


*!OBSERVACOES*
 - Caso a senha de aplicativo do email petengcomp.ufes@gmail.com seja alterada, lembre-se de altera-la no ".env" tambem (:
 - Dentro da pasta "test" Ha um codigo para buildar um container de teste. Este container comeca a rodar e em alguns segundos gera um erro. O intuito e rodar este container e verificar se o script registra sua paralizacao.
 - Dentro da pasta "src" ha um arquivo chamado "nohup.out". Este arquivo e responsavel por guardar os logs da execucao do programa que esta em background, portanto, nao mexa neste arquivo.
