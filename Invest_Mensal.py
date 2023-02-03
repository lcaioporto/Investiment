'''
O programa calcula quanto tempo demora para uma pessoa ficar milionária investindo uma certa quantia todo mês.
Além disso, dá a opção dela dizer por quanto tempo manteria esse ritimo de investimento mensal e qual seria seu resultado.
Por padrão, considera-se um desconto do imposto de renda (IR) da CDB:
    Até 180 dias: 22,5%
    De 181 até 360 dias: 20%
    De 361 até 720 dias: 17,5%
    Mais do que 721 dias: 15%
Obs.: IR é aplicado apenas sobre o lucro.
IOF é desconsiderada porque os períodos de tempo tendem a ser longos.
Assume-se que não há taxa de administração.
Considera-se um rendimento de liquidez diária que ocorre apenas em dias úteis (desconsidera-se finais de semana).
'''

def tempo_para_1M (valor_mensal, taxa):
    '''Calcula o tempo para alcançar 1 milhão de reais'''
    i = 0
    valor_atual = valor_mensal
    while valor_atual < 1000000:
        lucro_diario_total = valor_atual*taxa
        if i <= 180:
            lucro_real = lucro_diario_total * 0.775
        elif 180 < i <= 360:
            lucro_real = lucro_diario_total * 0.8
        elif 360 < i <= 720:
            lucro_real = lucro_diario_total * 0.825
        elif i > 720:
            lucro_real = lucro_diario_total * 0.85
        
        valor_atual += lucro_real

        if i % 30 == 0 and i!=0:
            valor_atual+=valor_mensal
        i+=1
    return i

def invest_mensal(valor_mensal, tempo, taxa):
    valor_atual = valor_mensal
    for i in range(tempo):
        if (i % 6 != 0 and i % 6 != 1) or i < 6 or i % 30 == 0: #seleciona o dia para garantir que é um dia útil.
            lucro_diario_total = valor_atual*taxa

            if i <= 180:
                lucro_real = lucro_diario_total * 0.775
            elif 180 < i <= 360:
                lucro_real = lucro_diario_total * 0.8
            elif 360 < i <= 720:
                lucro_real = lucro_diario_total * 0.825
            elif i > 720:
                lucro_real = lucro_diario_total * 0.85

            valor_atual += lucro_real
            if i % 30 == 0 and i!=0:
                valor_atual+=valor_mensal
    
    return valor_atual

valor_mensal = input("Insira quanto pretende investir mensalmente: ")
taxa = input("Insira qual a taxa de rendimento anual do investimento (em decimal): ")
anos = input("Insira por quantos anos pretende prosseguir com isso: ")

valor_mensal = float(valor_mensal)
taxa = float(taxa)/365 #taxa de rendimento diário
dias = int(anos)*365 #número de dias totais

montante = invest_mensal(valor_mensal, dias, taxa) #valor acumulado no tempo fornecido com o acúmulo mensal do input.
dias_uteis = tempo_para_1M (valor_mensal, taxa) #tempo em dias que demoraria para atingir 1 milhão de reais.
dias_totais = dias_uteis*365/251 #dias_uteis contam apenas os dias usados para o rendimento... para um tempo total deve-se ter um número maior

print("--------------------------------------------------------------------------------------------------------------------------------")
print("RELATÓRIO DE INVESTIMENTO\n")
print("Valor final:", f'{montante:.2f}', "reais.")
print("Você ganhou", f'{(montante - valor_mensal*(int(anos)*12)):.2f}', "reais com o investimento.")
print("Acumulando", valor_mensal, "reais por mês, você demoraria", f'{(dias_totais/12):.2f}', "meses para atingir 1 milhão de reais, o que daria", f'{(dias_totais/365):.2f}', "anos.")
print("--------------------------------------------------------------------------------------------------------------------------------")
