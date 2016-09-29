#ESSA VERSAO DO CLIENTE FUNCIONA IGUAL A OUTRA, POREM FOI TIRADO OS PRINTS PARA TER UMA MELHOR IDEIA DO TEMPO DE EXECUCAO
#ESSA VERSAO JA INCLUI 1000 INSERCOES

import xmlrpclib
import time
from datetime import datetime

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
	else: return 0

#Retorna so o usario de uma string do tipo comando(@user,....)
def getUser(ent):
	x = ent.find("@")
	y = ent.find(",")
	return ent[x:y]

#Retorna so o topico de uma string do tipo comando(@user,#topico,....)
def getTopic(ent):
	x = entrada.find(",")
	x = x + 1
	aux = entrada[x:]
	y = aux.find(",")
	return (aux[0:y])

#Retorna so a data de uma string do tipo retrievetime(@user,2015-05-05)
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
url = "http://localhost:" + porta + "/"
servidor =  xmlrpclib.ServerProxy(url)

#print(servidor.apresentar())

quantidade = 1000
media = 0;
i = 0

usr = "@nego"
top = "#sod"
data = "2016-09-01"
# mostrarPostTop(usuario,topico,datahora):
while i < quantidade:	

	comeco = time.time()
	
	rec = servidor.mostrarPostTop(usr,top,data)
	printarTuplas(rec)
	
	fim = time.time()

	i = i + 1

	media = media + (fim-comeco)


print(media/quantidade)
	

	
