"""
[Projeto de agenda para reelembrar Python]
"""
import sys
import cores

AGENDA: dict[str, dict] = {}

AGENDA['Fernando Moraes Brasil Santos'] = {
    'telefone': '11952463014',
    'email': 'buneco2007@gmail.com',
    'endereco': 'Rua joao Simao n80',

}

AGENDA['Jacqueline Cristina Augusto Moraes'] = {
    'telefone': '11958371290',
    'email': 'jacquelineaugusto28@hotmail.com',
    'endereco': 'Rua joao Simao n80',

}


def mostrar_todos_contatos() -> tuple:
    """[Funcao para mostrar todos os contatos]

    Returns:
        tuple: [Retorna a tupla com todos os contatos]
    """
    contador: int = 0
    lista_todos_contatos: list = []
    for contato in AGENDA.items():
        lista_todos_contatos.append(contato)
        contador += 1
    return (lista_todos_contatos, contador)


def buscar_contato(nome: str) -> tuple:
    """[Funcao para buscar um contato]

    Args:
        nome (str): [Nome do contato que deseja buscar]

    Returns:
        tuple: [Retorna a tupla com todos os contatos]
    """
    try:
        contador: int = 0
        lista_de_nomes: list = []
        for contato in AGENDA.items():
            if nome.upper() in contato[0].upper():
                lista_de_nomes.append(contato)
                contador += 1
        if contador == 0:
            return ()
        return lista_de_nomes, contador
    except KeyError as erro_keyerror:
        return tuple(f'Contato nao encontrado: {erro_keyerror}')


def incluir_editar_contato(nome: str, telefone: str,
                           email: str, endereco: str) -> tuple:
    """[Funcao para criar um novo contato]

    Args:
        nome (str): [Nome do contato]
        telefone (str): [Telefone do contato]
        email (str): [Email do contato]
        endereco (str): [Endereco do contato]

    Returns:
        tuple: [Retorna o contato incluido]
    """
    try:
        AGENDA[nome.strip()] = {
            'telefone': telefone,
            'email': email,
            'endereco': endereco
        }
        return buscar_contato(nome)
    except KeyError:
        return ()


def apagar_contato(contato: str) -> tuple:
    """[Funcao para apagar um contato]

    Args:
        contato (str): [Nome do contato que deseja buscar]

    Returns:
        [type]: [Retorna o contato apagado]
    """
    try:
        resultado = AGENDA.pop(contato)
        return tuple(resultado)
    except KeyError:
        return tuple()


def imprimir_menu():
    """[Funcao que imprime o menu]
    """
    print('#' * 10)
    print(f'{cores.Contorno.green}1 - '
          f'{cores.Contorno.yellow}Mostrar todos os contatos da agenda!{cores.Estilos.reset}')
    print(f'{cores.Contorno.green}2 - '
          f'{cores.Contorno.yellow}Buscar contato!{cores.Estilos.reset}')
    print(f'{cores.Contorno.green}3 - '
          f'{cores.Contorno.yellow}Incluir contato!{cores.Estilos.reset}')
    print(f'{cores.Contorno.green}4 - '
          f'{cores.Contorno.yellow}Editar contato!{cores.Estilos.reset}')
    print(f'{cores.Contorno.green}5 - '
          f'{cores.Contorno.yellow}Excluir contato!{cores.Estilos.reset}')
    print(f'{cores.Contorno.green}0 - '
          f'{cores.Contorno.yellow}Fechar agenda!{cores.Estilos.reset}')


def contatos_encontrados(quantidade: int) -> str:
    """[Funcao que retorna a quantidade encontrada de contatos]

    Args:
        quantidade (int): [Quantidade de contatos encontrados]

    Returns:
        int: [Lireralmente a quantidade encontrada]
    """
    contatos_total = (
        '#' * 10) + (f'{cores.Contorno.green}\nContatos encontrados: '
                     f'{cores.Contorno.yellow}{quantidade}{cores.Estilos.reset}')
    return contatos_total


def imprimir_contato(nome: str, telefone: str, endereco: str, email: str) -> str:
    """[Funcao para retornar o contato imprimido]

    Args:
        nome (str): [Nome do contato]
        telefone (str): [Telefone do contato]
        endereco (str): [Enderco do contato]
        email (str): [Email do contato]

    Returns:
        str: [Retorna o contato formado para impressao]
    """
    _contato = ('#' * 10 +
                f'\n{cores.Contorno.green}Nome: '
                f'{cores.Contorno.yellow}{nome}{cores.Estilos.reset}'
                f'\n{cores.Contorno.green}Telefone: '
                f'{cores.Contorno.yellow}{telefone}{cores.Estilos.reset}'
                f'\n{cores.Contorno.green}Endereco: '
                f'{cores.Contorno.yellow}{endereco}{cores.Estilos.reset}'
                f'\n{cores.Contorno.green}E-mail: '
                f'{cores.Contorno.yellow}{email}{cores.Estilos.reset}')
    return _contato


while True:
    imprimir_menu()
    opcao: str = input(
        f'{cores.Contorno.green}Digite a opcao desejada: {cores.Estilos.reset}')
    if opcao == '1':
        contatos: tuple = mostrar_todos_contatos()
        for dados in contatos[0]:
            print(imprimir_contato(dados[0], dados[1]["telefone"],
                                   dados[1]["endereco"], dados[1]["email"]))
        print(contatos_encontrados(contatos[1]))
    elif opcao == '2':
        _busca: str = input(
            f'{cores.Contorno.green}Digite o nome do contato que deseja buscar: '
            f'{cores.Estilos.reset}')
        _resultado: tuple = buscar_contato(_busca)
        if _resultado:
            for _contato in _resultado[0]:
                print(imprimir_contato(_contato[0], _contato[1]["telefone"],
                                       _contato[1]["endereco"], _contato[1]["email"]))
            print(contatos_encontrados(_resultado[1]))
        else:
            print(
                f'{cores.Contorno.red}Nenhum contato encontrado com esse nome!!!'
                f'{cores.Estilos.reset}')
    elif opcao in ('3', '4'):
        _nome: str = input(
            f'{cores.Contorno.green}Digite o nome do contato: {cores.Estilos.reset}')
        _telefone: str = input(
            f'{cores.Contorno.green}Digite o telefone: {cores.Estilos.reset}')
        _endereco: str = input(
            f'{cores.Contorno.green}Digite o endereco: {cores.Estilos.reset}')
        _email: str = input(
            f'{cores.Contorno.green}Digite o email: {cores.Estilos.reset}')
        _contato_incluir: tuple = incluir_editar_contato(
            _nome, _telefone, _email, _endereco)
        print(imprimir_contato(_contato_incluir[0][0][0], _contato_incluir[0][0][1]['telefone'],
                               _contato_incluir[0][0][1]['endereco'],
                               _contato_incluir[0][0][1]['email']))
        print(
            f'{cores.Contorno.red}Contato incluido com sucesso!!!{cores.Estilos.reset}')
    elif opcao == '5':
        nome_contato_excluir = input(
            f'{cores.Contorno.green}Digite o nome do contato que deseja excluir: '
            f'{cores.Estilos.reset}')
        contato_excluir = apagar_contato(nome_contato_excluir)
        if contato_excluir:
            print(
                f'{cores.Contorno.red}Contato apagado com sucesso!!!{cores.Estilos.reset}')
        else:
            print(
                f'{cores.Contorno.red}Contato nao encontrado!!!{cores.Estilos.reset}')
    else:
        sys.exit()
