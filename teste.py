# Sistema de pagamento universitário#
# Solicitaçaão de dados do aluno#

base_mensalidade = float(input("Digite o valor da mensalidade: "))
nota_aluno = float(input("Digite a nota do aluno (0.0 a 10.0): "))
mes_do_pagamento = int(input("Digite o mês do pagamento (1 a 31): "))
membro_da_comissao = input("O aluno é membro da comissão? (sim/não): ")

# Regra 1 : Validaçao de pagamento antecipado vs multa por atraso#
if mes_do_pagamento <= 5:
    base_mensalidade -= 100
    print("Pagamento antecipado. Desconto de R$100 aplicado.")
elif mes_do_pagamento <= 15:
    base_mensalidade = base_mensalidade
    print("Pagamento dentro do prazo. Valor da mensalidade mantido.")
elif mes_do_pagamento > 15:
    base_mensalidade += 50
    print("Pagamento atrasado. Multa de R$50 aplicada.")

# Regra 2 : Concessão de bolsa por desempenho acadêmico#
if nota_aluno >= 9.0:
    base_mensalidade -= base_mensalidade * 0.20
    print("Desempenho acadêmico excelente. Bolsa de 20% aplicada.")
elif 7.0 <= nota_aluno < 9.0:
    base_mensalidade -= base_mensalidade * 0.10
    print("Desempenho acadêmico bom. Bolsa de 10% aplicada.")
elif nota_aluno < 7.0:
    print("Atenção : Procure a coordenação para apoio pedagógico.")

# Regra 3 : Bônus da Monitoria#
if membro_da_comissao == "sim":
    base_mensalidade = base_mensalidade - 50
    print("Bônus de monitoria aplicado. Desconto de R$50.")
else :
    print("Sem bônus de monitoria.")

print(f"Valor final da mensalidade :) R${base_mensalidade:.2f}")
