bateria_atual = float(input("Digite a porcentagem de bateria atual (0 a 100%):"))
duracao = float(input("Digite a duração da missão em minutos:"))
consumo_minuto = float(input("Qual consumo por minuto?:"))

if bateria_atual < 0 or bateria_atual > 100 or duracao <= 0 or consumo_minuto <= 0:
    print("Valor inválido!")

else: 

    consumo_total = duracao * consumo_minuto


    if bateria_atual >= consumo_total:
        bateria_restante = bateria_atual - consumo_total
        print("A missão pode ser concluída! Percentual de bateria restante:", bateria_restante,"%." )

    else:
        pontos_faltandos = consumo_total -  bateria_atual
        print("A missão não pode ser concluída. Faltam:", pontos_faltandos, "%.")
