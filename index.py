import json
import random
from time import sleep

try:
    with open("produtos.json", "r", encoding="utf-8") as dados:
        produtos = json.load(dados)

except FileNotFoundError:
    produtos = []

print("\033[33mSistema de Caixa\033[0m")
print()
sleep(0.6)

print("[1] Adicionar produtos ao carrinho")
print()

while True:

    escolha = input("Digite sua escolha: ")
    print()

    if escolha.isnumeric():
        break
    else:
        print("\033[31mIsso não é um número !\033[0m")
        print()

if escolha == 1:

    carrinho = []

    while True:

        while True:

            while True:

                co_prodto =input("Digite o código do produto: ")
                print()

                if co_prodto.isnumeric():
                    break
                else:
                    print("\033[31mIsso não é um número !\033[0m")
                    print()

            produto_enco = None

            for produto in produtos:
                if produto['codigo'] == co_prodto:
                    produto_enco = produto
                    break

            if produto_enco is not None:
                break

        print(f"Nome: {produto_enco['nome']}")
        print(f"Preço: {produto_enco['preço']}")
        print(f"Estoque: {produto_enco['estoque']}")
        print(f"Código: {produto_enco['codigo']}")
        print()

        opção = input("O produto está correto : ").lower().strip()
        if opção in ['sim', 's', 'positivo', 'correto', 'certo', 'ss']:

            carrinho.append(produto_enco)

            print("\033[32mProduto adicionado !\033[0m")
            print()