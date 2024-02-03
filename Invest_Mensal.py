'''
The program calculates how long it takes for a person to become a millionaire by investing a certain amount every month.
Furthermore, it gives her the option to say how long she would maintain this monthly investment rhythm and what her results would be.
By default, a CDB income tax (IR) discount is considered:
    Up to 180 days: 22.5%
    From 181 to 360 days: 20%
    From 361 to 720 days: 17.5%
    More than 721 days: 15%
Note: IR is only applied to profit.
IOF is disregarded because time periods tend to be long.
It is assumed that there is no administration fee.
Daily liquidity income is considered to occur only on business days (weekends are not considered).
'''

def tempo_para_1M (valor_mensal, taxa):
    '''
    Calculate the time, in days, to reach 1 million reais
    Note that the calculated time only takes into account working days,
    that is, the real time tends to be longer (adjusted in the code below).
    '''
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
    '''
    Calculates and returns the amount resulting from the monthly investment
    during the time period entered by the user.
    '''
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

valor_mensal = input("Enter how much you intend to invest monthly: ")
taxa = input("Enter the annual rate of return on the investment (in decimal): ")
anos = input("Enter how many years you plan to continue with this: ")

valor_mensal = float(valor_mensal)
taxa = float(taxa)/365 # daily yield rate
dias = int(anos)*365   # number of total days

montante = invest_mensal(valor_mensal, dias, taxa) # accumulated value in the time provided with the monthly input accumulation.
dias_uteis = tempo_para_1M (valor_mensal, taxa)    # time in days that it would take to reach 1 million.
dias_totais = dias_uteis*365/251                   # dias_uteis only counts the days used for income

print("--------------------------------------------------------------------------------------------------------------------------------")
print("INVESTMENT REPORT\n")
print("Final value:", f'{montante:.2f}')
print("You won", f'{(montante - valor_mensal*(int(anos)*12)):.2f}', "dolars with the investment.")
print("Accumulating", valor_mensal, "dollars per month, it would take you", f'{(dias_totais/12):.2f}', "months to reach 1 million reais, which would give", f'{(dias_totais/365):.2f}', "years.")
print("--------------------------------------------------------------------------------------------------------------------------------")
