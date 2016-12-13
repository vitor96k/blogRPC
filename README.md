# Blog RPC

Desenvolvimento de um blog utilizando RPC para a disciplina de Sistemas Operacionais - 3º Ano Ciência da Computação

As operações permitidas no micro blogue: <br /> <br />

a) Usuários enviam post em um determinado tópico: post(@username, #tópico, texto)  <br />
b) Usuário ingressa em um determinado tópico: follow (@username, #tópico) <br />
c) Usuário deixa de seguir e de acessar um determinado tópico: unsubscribe (@username, #tópico) <br />
d) O usuário recupera todos os posts de todos os tópicos que faz parte, desde a data especificada até a data atual: retrievetime (@username, timestamp) <br />
e) O usuário recupera todos os posts, apenas do tópico identificado (o usuário deve fazer parte do tópico), desde a data especificada até a data atual: retrievetopic(@username, #tópico, timestamp) <br />


Obs: Além de utilizar RPC o programa também utiliza de uma conexão com um banco de dados (Postgres)

Autores: Vitor Palma Aderaldo e Vitor Henrique Rosa Batista de Oliveira

Feito junto com https://github.com/vhrboliveira
