from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import psycopg2

#Strings para inserir, selecionar e deletar tuplas do Banco de Dados
banco_inserir_post = "insert into posts2 (usuario,topico,texto) values (%s,%s,%s)"
banco_inserir_follow = "insert into follow2 (usuario,topico) values (%s,%s)"
banco_deletar_follow = "delete from follow2 where usuario = %s and topico = %s"
banco_select_posts = "select usuario,topico,texto from posts2 where datahora >= %s and topico in ( select topico from follow2 where usuario = %s)"
banco_select_postsTop = "select usuario,topico,texto from posts2 where datahora >= %s and topico in ( select topico from follow2 where usuario = %s) and topico = %s"
porta = 12346

#Apresentacao, mostra que a conexao foi feita
def apresentar():
	#Strings para ajudar o usuario
	help1 = " post(@username,#topic,text)     |  follow(@username,#topic)\n"
	help4 = " ----------------------------------------------------------------\n"
	help5 = "\n                          Formato:                     \n"
	help2 = " unsubscribe(@username,#topic)   |  retrievetime(@username,date)\n"
	help3 = " retrievetopic(@username,#topic,date)\n"

	apresenta = "\n        Bem vindo ao Blog RPC, digite quit para sair,\n"
	apresenta2 = "       caso tenha duvidas digite help para saber mais.\n"

	return (apresenta+apresenta2+help5+help4+help1+help2+help3+help4)

#Insere no banco de dados o post do usuario.
def postar(usuario, topico, texto):	
	cursor.execute(banco_inserir_post, (usuario,topico,texto))
	conectarBd.commit()
	return "Postado com sucesso !"

#Insere no banco de dados que tal usuario segue tal topico
def seguir(usuario,topico):
	cursor.execute(banco_inserir_follow,(usuario,topico)) #Faz a insercao
	conectarBd.commit()									  #Valida a operacao
	return "Voce esta seguindo o topico " + topico

#Remove do banco de dados um topico que o usuario segue
def parardeSeguir(usuario,topico):
	cursor.execute(banco_deletar_follow, (usuario,topico))
	conectarBd.commit()
	return "Voce parou de seguir o topico "  + topico

#Retorna do banco de dados todos posts feitos a partir de tal data
#Lembrar que sao topico que o usuario segue
def mostrarPost(usuario,datahora):
	cursor.execute(banco_select_posts,(datahora,usuario))
	tuplas = cursor.fetchall()	
	return tuplas

#Retorna do banco de dados todos posts feitos a partir de tal data
#O usuario informa o tipo de topico e ele deve segui-lo
def mostrarPostTop(usuario,topico,datahora):
	cursor.execute(banco_select_postsTop,(datahora,usuario,topico))
	tuplas = cursor.fetchall()
	return tuplas

#Conecta ao Banco de Dados
conectarBd = psycopg2.connect("dbname=teste user=vitor")
#Cursor para operar no Banco
cursor = conectarBd.cursor()

#Cria o servidor RPC
servidor = SimpleXMLRPCServer(("191.52.64.212",porta))
print ("Servidor RPC criado na porta", porta)

#Registra as funcoes que os cliente podem usar
servidor.register_function(postar,"postar")
servidor.register_function(seguir,"seguir")
servidor.register_function(parardeSeguir,"parardeSeguir")
servidor.register_function(mostrarPost,"mostrarPost")
servidor.register_function(mostrarPostTop,"mostrarPostTop")
servidor.register_function(apresentar,"apresentar")

#Para o servidor ficar de pe para sempre
servidor.serve_forever()
