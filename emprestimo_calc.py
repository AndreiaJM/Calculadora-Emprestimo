import os
import valida_cnpj as vc

#capturando erro caso seja digitado letra na quantidade de parcelas
def verifica_parcela(qtd_parcelas):

    try:
        qtd_parcelas=int(qtd_parcelas)
        return qtd_parcelas
    except ValueError: #tratando erro e encerrando programa
        print('Valor invalido, verifique os dados e tente novamente')
        exit()

#capturando erro caso seja digitado letra no valor do emprestimo
def verifica_emprestimo(valor_emprestimo):

    
    try:
        valor_emprestimo=float(valor_emprestimo)
        return valor_emprestimo 
    except ValueError: #tratando erro e encerrando programa
        print('Valor invalido, verifique os dados e tente novamente')
        exit()

def confirma_cnpj(cnpj):

    Sair_cnpj=False

    #looping para digitar o cpf novamente sem encerrar o programa caso haja erro
    while Sair_cnpj == False:
        if vc.validar_cnpj(cnpj) == False:
            cnpj = input("CPNJ inválido, tente novamente: ")
        else:
            Sair_cnpj=True


#-------------------------------------------------------------------------------

#função para calcular o emprestimo
def calcular_emprestimo(valor_emprestimo, qtd_parcelas,cnpj,nome_empresa):

    juros=3 #definindo juros
    cont_mes=1 #contagem de meses para o looping whilw

    #enquanto o contador de mês for menor que a quantidade de parcelas digitadas
    #a variavel valor_emprestimo ira acumular o valor de juros definido
    #de acordo com a quantidade de meses digitados e guarda o total

    os.system('cls') #limpando tela

    #dados que seram impressos em tela
    print('-----------------------------------------')
    print('-------Bem vindo ao AJMS Bank------------')
    print('-----------------------------------------')
    print('-----------CAPITAL + JUROS---------------')
    while cont_mes<=qtd_parcelas:
        valor_emprestimo+=((valor_emprestimo/100)*juros)
        print('Montante (Juros de '+str(juros)+'%'+' ao mês): %.2f '%(valor_emprestimo))
            
        cont_mes+=1
    print('-------------------------------------------')
    print('---------------RESUMO----------------------')

    valor_parcela = (valor_emprestimo/qtd_parcelas) 
    #acima o total dividido pela quantidade de meses

    #dados impressos em tela
    print('Empresa: '+nome_empresa)
    print('CNPJ: '+cnpj)
    print('Valor total: %.2f' %(valor_emprestimo))
    print('Valor de cada parcela: %.2f' %(valor_parcela)+' X '+str(qtd_parcelas))
    print('-------------------------------------------')
    print('\n')
