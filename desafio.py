nome_usuario = input("Digite seu nome: ")

salario_usuario = float(input("Digite o seu salário: "))

bonus_usuario = float(input("Digite o seu bônus: "))

CONSTANTE_BONUS = 1000

valor_do_bonus = 1000 + salario_usuario * bonus_usuario

print(f"O usuário {nome_usuario} recebeu um bônus de R$ {valor_do_bonus:.2f}")