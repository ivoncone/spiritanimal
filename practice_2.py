
def suma(gatos):
	suma=0
	for i in gatos:
		suma = suma + i
		
	return(suma)

gatos=[]
gatos = [732, 75, 540]

n = len(gatos)

resultado = suma(gatos)

print ('Gaste un total de ', resultado)


