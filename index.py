import json
import random
from time import sleep
from datetime import datetime

try:
    with open("produtos.json", "r", encoding="utf-8") as dados:
        produtos = json.load(dados)

except FileNotFoundError:
    produtos = []

carrinho = []

print("\033[33mSistema de Caixa\033[0m")
print()
sleep(0.6)

while True:

    print("[1] Adicionar produtos ao carrinho")
    print()
    print("[2] Comfirmar a compra ")
    print()
    print("[3] Remover item do carrinho ")
    print()

    while True:

        escolha1 = input("Digite sua escolha: ")
        print()

        if escolha1.isnumeric() == True:
            break
        else:
            print("\033[31mIsso não é um número !\033[0m")
            print()

    escolha = float(escolha1)

    if escolha == 1:

        

        while True:

            while True:

                while True:

                    co_produto =input("Digite o código do produto: ")
                    print()

                    produto_enco = None

                    for produto in produtos:
                        if produto['codigo'] == co_produto:
                            produto_enco = produto
                            break

                    if produto_enco is not None:
                        break
                    else:
                        print("\033[31mProduto não encontrado !\033[0m")
                        print()

                print(f"Nome: {produto_enco['nome']}")
                print(f"Preço: {produto_enco['preço']}")
                print(f"Estoque: {produto_enco['estoque']}")
                print(f"Código: {produto_enco['codigo']}")
                print()

                opção = input("O produto está correto : ").lower().strip()
                print()

                if opção in ['sim', 's', 'positivo', 'correto', 'certo', 'ss']:

                    while True:

                        qua_produto1 = input("Digite quantos vão ser adicionados: ")
                        print()

                        if qua_produto1.isnumeric():
                            
                            break
                        else:
                            print("\033[31mIsso não é um número !\033[0m")
                            print()

                    qua_produto = int(qua_produto1)

                    for i in range(qua_produto):

                        carrinho.append(produto_enco)
                        produto_enco['estoque'] = produto_enco['estoque'] - 1

                    print("\033[32mProduto adicionado !\033[0m")
                    print() 
                    break

            print("Ainda vai adicionar produtos? ") 
            print()     

            continuar = input("Sim ou Não: ").lower().strip()
            print()

            if continuar in ['não', 'n']:
                break
            elif continuar in ['sim', 's', 'positivo', 'correto']:
                print() 
            else:
                print("\033[31mOpção inválida !\033[0m")
                print()

    elif escolha == 2:

        agora = datetime.now()

        data_hora = agora.strftime("%d/%m/%Y/-/%H:%M")

        total = sum(produto['preço'] for produto in carrinho)
        total_itens = 0
        for produto in carrinho:
            total_itens += 1

        print("\033[33mNota fiscal\033[0m")
        print("==========================")
        print()
        print("Mercado Bom Preço")
        print(f"Data: {data_hora}")
        print(f"Quantidade de itens: {total_itens}")
        print(f"O total a pagar é de \033[32mR${total:.2f}\033[0m.")
        print()
        print("==========================")
        print()

        with open('produtos.json', 'w', encoding="utf-8") as dados:
            json.dump(produtos, dados, ensure_ascii= False, indent= 4)

    elif escolha == 3:

        print("Digite o código do item que deseja remover: ")

        