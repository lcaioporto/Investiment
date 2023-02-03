# Investimento
Repositório em Python que permite o usuário avaliar quanto tempo demoraria para ficar milionário investindo determinada quantia de dinheiro por mês.
Além disso, o programa pergunta ao usuário por quanto tempo manteria esse ritimo de investimento mensal, e printa no final o resultado.

Por padrão, considera-se um desconto do imposto de renda (IR) da CDB:
<p>
    Até 180 dias: 22,5%;
</p>
<p>
    De 181 até 360 dias: 20%;
</p>
<p>
    De 361 até 720 dias: 17,5%;
</p>
<p>
    Mais do que 721 dias: 15%.
</p>
Obs.: IR é aplicado apenas sobre o lucro.

IOF é desconsiderada porque os períodos de tempo tendem a ser longos.
Assume-se que não há taxa de administração.
Considera-se um rendimento de liquidez diária que ocorre apenas em dias úteis (desconsidera-se finais de semana).

# Exemplo de aplicação

O programa deve ser rodado no terminal:
<p>
<img width="710" alt="image" src="https://user-images.githubusercontent.com/115668120/216605133-e0ead84b-5f28-4c15-b7be-6fcb91aa29ef.png">
</p>
