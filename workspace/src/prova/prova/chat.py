#! /bin/env python3
import re

def update_card(_):
    return "Para atualizar as informações do cartão, basta clicar no ícone do perfil, acessar as configurações e depois clicar em mudar informações"

def order_status(_):
    return "Seu pedido já saiu para entrega e deve chegar entre 3-5 dias"

intecoes = {
    r"\b((pagamento|cart[ãa]o|cr[ée]dito)\s?.+)?(desatualizado|atualizar|mudar)\s?.+(pagamento|cart[ãa]o|cr[ée]dito)?": "update_card",
    r"\b(([Vv]er|rastrear)\s?.+)?(([Ss]tatus|onde)\s?.+)?(pedido|entrega).+((?))?": "order_status"
}

acoes = {
        "update_card": update_card,
        "order_status": order_status
}
def main():
    
    while (input("Tem outro problema (yes|no): ") == "no"):
        command = input("Qual o sue problema")         
        for key, value in intecoes.items():
            pattern = re.compile(key)
            print(pattern)
            groups = pattern.findall(command)
            print('key:', key)
            print('value:', value)
            # print('groups: ',groups)
            # print('value: ',value)
            if groups:
                print(f"{acoes[value](groups[0])}", end=" ")
        print()