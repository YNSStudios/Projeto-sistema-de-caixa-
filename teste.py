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
    print("[3] Visualizar o carrinho ")
    print()
    print("[4] Remover item do carrinho ")
    print()


    escolha = input("Digite sua escolha: ")
    print()

    if escolha == 1:

        while True:

            while True:

                while True:

                    print("Para terminar a adição digite \033[31mSair\033[0m")

                    co_produto = input("Digite o código do produto: ")
                    print()

                    produto_enco = None

                    for produto in produtos:
                        if produto["codigo"] == co_produto:
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

                while True:

                    opçao = input("O produto está correto : ").lower().strip()
                    print()

                    if opçao in ["sim", "s", "positivo", "correto", "certo", "ss"]:

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

                        print("\033[32mProduto adicionado !\033[0m")
                        print()
                        break
                    else:
                        print("Está correto ? Não entendi sua ultima mensaguem ): ")

                    break
                break    

            if co_produto or opçao or qua_produto in ['Sair', 'sair']:
                break

    elif escolha == 2:

        agora = datetime.now()

        data_hora = agora.strftime("%d/%m/%Y/-/%H:%M")

        total = sum(produto["preço"] for produto in carrinho)
        total_itens = 0

        for produto in carrinho:
            total_itens += 1

        for item_carrinho in carrinho:
            for produto in produtos:
                if produto["codigo"] == item_carrinho["codigo"]:
                    produto["estoque"] = produto["estoque"] - 1
                    break

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

        with open("produtos.json", "w", encoding="utf-8") as dados:
            json.dump(produtos, dados, ensure_ascii=False, indent=4)

        break

    elif escolha == 3:

        print("\033[33mProdutos no Carrinho\033[0m")
        print("==========================")
        print()

        itens_exibidos = []

        for produto in carrinho:
            
            if produto['codigo'] not in itens_exibidos:
                
                qtd = sum(1 for p in carrinho if p['codigo'] == produto['codigo'])
                
                print(f"Nome: {produto['nome']}")
                print(f"Preço: {produto['preço']:.2f}")
                print(f"Quantidade: {qtd}")
                print("==========================")
                print()
                itens_exibidos.append(produto['codigo'])

        total = sum(produto['preço'] for produto in carrinho)

        print(f"O total a pagar é de: \033[32mR${total:.2f}\033[0m.")
        print()

    elif escolha == 4:

        print("Digite o código do item que deseja remover. ")
        print()

        while True:

            re_produto = input("Digite o código: ")
            print()

            remover_produto = None

            for produto in carrinho:
                if produto["codigo"] == re_produto:
                    remover_produto = produto
                    break

            if remover_produto is not None:
                break
            else:
                print("\033[31mCódigo não encontrado !\033[0m")
                print()

        quantidade_carrinho = sum(
            1 for produto in carrinho
            if produto["codigo"] == re_produto
        )

        print(
            f"Você possui {quantidade_carrinho} unidade(s) "
            f"de {remover_produto['nome']} no carrinho."
        )
        print()

        while True:

            quantidade_remover1 = input("Quantas unidades deseja remover: ")
            print()

            if quantidade_remover1.isnumeric():

                quantidade_remover = int(quantidade_remover1)

                if quantidade_remover == 0:
                    print("\033[31mA quantidade deve ser maior que 0 !\033[0m")
                    print()

                elif quantidade_remover > quantidade_carrinho:
                    print(
                        f"\033[31mVocê possui apenas "
                        f"{quantidade_carrinho} unidade(s) no carrinho !\033[0m"
                    )
                    print()

                else:
                    break

            else:
                print("\033[31mIsso não é um número !\033[0m")
                print()

        for i in range(quantidade_remover):
            carrinho.remove(remover_produto)

        print(
            f"\033[32m{quantidade_remover} unidade(s) "
            f"removida(s) com sucesso !\033[0m"
        )
        print()
