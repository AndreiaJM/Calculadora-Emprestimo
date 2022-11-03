#----------------------------VALIDANDO CNPJ----------------------------------------#

#função para validar cnpj
def validar_cnpj(cnpj):

    #retirando dados que o usuario pode vir a digitar (traços,pontos,barra,espaços)
    cnpj = cnpj.replace(' ','').replace('-','').replace('/','').replace('.','')

    cnpj_auxiliar=0
    cont=0
    somador=0
    resto=0
    digito1=0
    digito2=0

    #Valores padrão da receita federal(RF) para calcular o cnpj
    multiplicador1=[5,4,3,2,9,8,7,6,5,4,3,2] #digito 1
    multiplicador2=[6,5,4,3,2,9,8,7,6,5,4,3,2] #digito 2

    #pegando os 12 digitos para o calculo
    cnpj_auxiliar=cnpj[0:12]

    #verificando quantidade de digitos digitados, cnpj=14
    if len(cnpj) !=14:
        return False
    else: 

        #Multiplicando as 12 posições/digitos do cnpj X o padrão da RF
        #e somando
        while cont<12:
            somador+=int(cnpj_auxiliar[cont])*int(multiplicador1[cont])
            
            cont+=1

        #calculando resto da soma dividida por 11 de acordo com a RF
        resto=somador%11

        #caso RESTO seja 0 ou 1 o PRIMEIRO digito tera valor 0, caso não
        #o valor do digito sera 11 meno o resto
        if resto<2:
            digito1=0
        else:
            digito1=11-resto

        #concatenando os 12 numeros do cnpj + PRIMEIRO digito verificado
        #e formando 13 numeros
        cnpj_auxiliar=cnpj_auxiliar+str(digito1)

        #resetando as variaveis
        somador=0
        cont=0
        resto=0

        #Multiplicando as 13 posições/digitos do cnpj X o padrão da RF
        #e somando
        while cont<13:
            somador+=int(cnpj_auxiliar[cont])*int(multiplicador2[cont])
            
            cont+=1

        #calculando resto da soma dividida por 11 de acordo com a RF
        resto=somador%11

        #caso RESTO seja 0 ou 1 o PRIMEIRO digito tera valor 0, caso não
        #o valor do digito sera 11 menos o resto
        if resto<2:
            digito1=0
        else:
            digito2=11-resto

        #concatenando os 13 numeros do cnpj + SEGUNDO digito verificado
        #e formando 13 numeros
        cnpj_auxiliar=cnpj_auxiliar+str(digito2)

        #Se o cnpj auxiliar for igual ao digitado retornara Verdadeiro
        #Caso diferente retorna falso
        if cnpj_auxiliar == cnpj:
            return True
        else:
            return False