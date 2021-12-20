from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print(20 * '=-')
    print(10 * '=-', 'LOJA AQUI', 10 * '=-')
    print(20 * '=-')

    print('''Selecione uma das opções abaixo
    1 - Cadastrar Produtos
    2 - Listar Produtos
    3 - Comprar Produtos
    4 - Visualizar Carrinho
    5 - Fechar Pedido
    6 - Sair do Sistema''')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Obrigado por usar nosso sistema ^^')
        sleep(2)
        exit(1)
    else:
        print('Função invalida...')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    print(20 * '=-')
    print('Cadastro de Produtos'.center(20))

    nome: str = str(input('Informe o Nome do Produto: '))
    preco: float = float(input('Informe o Preço do Produto'))

    produto: Produto = Produto(nome, preco)

    if produto.nome in produtos:
        print('Produto com nome ja cadastrado tente novamente')
        sleep(2)
        menu()

    else:
        produtos.append(produto)
        print(f'O produto {produto.nome} foi cadastrado com sucesso!')
        sleep(2)
        menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print(20 * '=-')
        print('Lista de Produtos'.center(20))
        for produto in produtos:
            print(20 * '=-')
            print(produto)

    else:
        print('Produtos ainda não cadastrados')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print(20 * '=-')
        print('Informe o codigo do produto para adicionar no carrinho: '.center(20))
        for produto in produtos:
            print(produto)
            print(20 * '=-')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidade no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()

        else:
            print('Produto Invalido...')
            sleep(2)
            menu()

    else:
        print('Ainda não possuem produtos Cadastrados')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print(20 * '=-')
        print('Produtos no carrinho'.center(20))

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print(20 * '=-')
                sleep(2)
    else:
        print('Carrinho vazio')
        sleep(2)
        menu()
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        print(20 * '=-')
        print('Produtos no carrinho'.center(20))
        print(20 * '=-')

        valor_total: float = 0

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade de produtos: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print(20 * '=-')

        print(f'Sua fatura final é de {formata_float_str_moeda(valor_total)}')
        print(f'Volte sempre')
        print(carrinho.clear())

    else:
        print('Carrinho vazio')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:

    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
