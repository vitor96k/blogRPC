import xmlrpclib
from datetime import datetime

#Funcao para ajudar o usuario, printa na tela oque cada comando faz
def ajudar():
	#Strings para ajudar o usuario
	help1 = " post(@username,#topic,text)     |  follow(@username,#topic)\n"
	help4 = " ----------------------------------------------------------------\n"
	help5 = "\n                          Formato:                     \n"
	help2 = " unsubscribe(@username,#topic)   |  retrievetime(@username,date)\n"
	help3 = " retrievetopic(@username,#topic,date)\n"

	posta = "\n Post: Voce postar sobre um determinado topico e os\n outros usuarios que seguem esse topico podem ver"
	segui = "\n Follow: Ao seguir um determinado topico voce podera\n ver todos os posts relacionada a esse topico\n"
	unsegui = "\n Unsubscribe: Voce para de seguir determinado topico\n"
	retri = "\n Retrieve Time: Voce pode ver todos os posts feitos\n a partir da data informada dos topicos que segue\n"
	retrit = "\n Retrieve Topic: Voce pode ver todos os posts feitos de\n determinado topico a partir da data informada\n"

	return (help5+help4+help1+help2+help3+help4+posta+"\n"+segui+unsegui+retri+retrit)

#Usado para printar os posts dos usarios nas consultas retrieves
def printarTuplas(tuplas):	
    tam = len(tuplas)
    i = 0
    while i < tam:
        texto = tuplas[i]
        print("Usuario: %s  Topico: %s  Texto: %s" % (texto[0],texto[1],texto[2]))
        i+=1

#Usado para saber qual opcao o usuario digitou
def achar(ent):
	if ent.find("post(@") != -1:
		return 1
	if ent.find("follow(@") != -1:
		return 2
	if ent.find("unsubscribe(@") != -1:
		return 3
	if ent.find("retrievetime(@") != -1:
		return 4
	if ent.find("retrievetopic(@") != -1:
		return 5
	if ent.find("help") != -1:
		return 6
	else: return 0

#Retorna o usuario de uma string do tipo comando(@user,....)
def getUser(ent):
	x = ent.find("@")
	y = ent.find(",")
	return ent[x:y]

#Retorna o topico de uma string do tipo comando(@user,#topico,....)
def getTopic(ent):
	x = entrada.find(",")
	x = x + 1
	aux = entrada[x:]
	y = aux.find(",")
	return (aux[0:y])

#Retorna a data de uma string do tipo retrievetime(@user,2015-05-05)
def getDataHora(ent):
	x = entrada.find(",")
	x = x + 1
	aux = entrada[x:]
	y = aux.find(")")
	return aux[0:y]

#Retorna o texto string do tipo comando(@user,#topic,texto)
#Tambem e usado para pegar a data do retrievetopic
def getText(ent):
	x = entrada.find(",")
	x = x + 1
	aux = entrada[x:]
	y = aux.find(",")
	y = y + 1
	z = aux.find(")")
	return (aux[y:z])

#Definicoes de porta e IP do servidor
porta = "12346";
url = "http://191.52.64.212:" + porta + "/"

#Faz a conexao com o servidor RPC
servidor =  xmlrpclib.ServerProxy(url)

#Chama a funcao do servidor Apresentar que retorna a mensagem de bem vindo.
print(servidor.apresentar())


#A partir daqui o codigo le o que o usuario digitou e analisa o comando para chamar alguma funcao do servidor
entrada = raw_input("-> ")

while entrada != 'quit':	

	teste = achar(entrada)

	if teste == 1: 
		usr = getUser(entrada)
		top = getTopic(entrada)		
		txt = getText(entrada)
		print(servidor.postar(usr,top,txt))
	if teste == 2:
		usr = getUser(entrada)
		top = getTopic(entrada)
		print(servidor.seguir(usr,top))
	if teste == 3: 
		usr = getUser(entrada)
		top = getTopic(entrada)
		print(servidor.parardeSeguir(usr,top))
	if teste == 4:
		usr = getUser(entrada)
		dh = getDataHora(entrada)
		rec = servidor.mostrarPost(usr,dh)
		printarTuplas(rec)
	if teste == 5:
		usr = getUser(entrada)
		top = getTopic(entrada)
		dh = getText(entrada) #getText pega o terceiro parametro
		rec = servidor.mostrarPostTop(usr,top,dh)
		printarTuplas(rec)
	if teste == 6:
		print(ajudar())
	if teste == 0: 
		print("Comando nao encontrado")
	

	entrada = raw_input("-> ")
