global = "Esta variável é global e pode ser acessada em qualquer lugar do código."
def minha_funcao(): 
    print("Olá, esta é a minha função!")
    local = "Esta variável é local à função." 

#chamando a função
minha_funcao()
#print(local)  
# Isso causará um erro, pois 'local' não é acessível fora da função.
print(global)


