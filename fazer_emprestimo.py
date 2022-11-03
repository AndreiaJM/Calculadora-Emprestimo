import emprestimo_calc as validador
import valida_cnpj as vc
import os

#-----------------------Fazer Emprestimo----------------------------------------#

os.system('cls')

#capturando nome da empresa
nome_empresa = input("Digite o nome da empresa: ")
n
#capturando cnpj
cnpj = str(input("Digite o CPNJ: "))
validador.confirma_cnpj(cnpj) #confirmando validade do cnpj digitado

#verificando erro caso seja digitado letra no valor do emprestimo
valor_emprestimo = input("Digite o valor do emprestimo: ")
valor_emprestimo=validador.verifica_emprestimo(valor_emprestimo)

#verificando erro caso seja digitado letra no valor no numero de parcelas
qtd_parcelas = input("Digite a quantidade de parcelas: ")
qtd_parcelas = validador.verifica_parcela(qtd_parcelas)
    
#calculando o emprestimo apos a validação dos dados
validador.calcular_emprestimo(valor_emprestimo,qtd_parcelas,cnpj,nome_empresa)






