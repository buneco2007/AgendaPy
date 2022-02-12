"""
[Projeto de agenda para reelembrar Python]
"""

import sys
import cores

AGENDA: dict[str, dict] = {}


def mostrar_todos_contatos() -> tuple:
    """[Funcao para mostrar todos os contatos]

    Returns:
        tuple: [Retorna a tupla com todos os contatos]
    """
    contador: int = 0
    lista_todos_contatos: list = []
    for contact in AGENDA.items():
        lista_todos_contatos.append(contact)
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
        for contacts in AGENDA.items():
            if nome.upper() in contacts[0].upper():
                lista_de_nomes.append(contacts)
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
        AGENDA[nome.strip().upper()] = {
            'telefone': telefone.upper(),
            'email': email.upper(),
            'endereco': endereco.upper()
        }
        salvar_agenda()
        return buscar_contato(nome)
    except KeyError:
        return ()


def apagar_contato(name: str) -> tuple:
    """[Funcao para apagar um contato]

    Args:
        contato (str): [Nome do contato que deseja buscar]

    Returns:
        [type]: [Retorna o contato apagado]
    """
    try:
        res = AGENDA.pop(name.upper())
        salvar_agenda()
        return tuple(res)
    except KeyError:
        return ()


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
    print(f'{cores.Contorno.green}6 - '
          f'{cores.Contorno.yellow}Exportar contatos para CSV!{cores.Estilos.reset}')
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
                f'{cores.Contorno.green}{nome}{cores.Estilos.reset}'
                f'\n{cores.Contorno.green}Telefone: '
                f'{cores.Contorno.green}{telefone}{cores.Estilos.reset}'
                f'\n{cores.Contorno.green}Endereco: '
                f'{cores.Contorno.green}{endereco}{cores.Estilos.reset}'
                f'\n{cores.Contorno.green}E-mail: '
                f'{cores.Contorno.green}{email}{cores.Estilos.reset}')
    return _contato


def carregar_agenda() -> bool:
    """[Funcao que carrega a agenda no inicio do programa]"""
    try:
        with open('agenda.csv', 'r', encoding='utf-8') as file_init:
            data = file_init.readlines()
            for strings in data:
                new_contact = strings.strip().split(';')
                incluir_editar_contato(new_contact[0], new_contact[1], new_contact[2],
                                       new_contact[3])
            return True
    except IOError:
        return False


def salvar_agenda() -> bool:
    """[Funcao para salvar agenda em csv]
    """
    try:
        with open('agenda.csv', 'w', encoding='utf-8') as file:
            for contato_salvar in AGENDA.items():
                export: str = (f'{contato_salvar[0]};{contato_salvar[1]["telefone"]};'
                               f'{contato_salvar[1]["email"]};{contato_salvar[1]["endereco"]}\n')
                file.write(export)
            return True
    except IOError:
        print(f'{cores.Contorno.red}Houve um erro ao salvar a sua agenda!!!')
        return False


load_agenda_status: bool = carregar_agenda()
if not load_agenda_status:
    print(f'{cores.Contorno.red}Falha ao carregar os contatos da agenda!!!{cores.Estilos.reset}')
while True:
    imprimir_menu()
    opcao: str = input(
        f'{cores.Contorno.green}Digite a opcao desejada: {cores.Estilos.reset}')
    if opcao == '1':
        contatos: tuple = mostrar_todos_contatos()
        for dados in contatos[0]:
            print(imprimir_contato(dados[0].upper(), dados[1]["telefone"].upper(),
                                   dados[1]["endereco"].upper(), dados[1]["email"].upper()))
        print(contatos_encontrados(contatos[1]))
    elif opcao == '2':
        busca: str = input(
            f'{cores.Contorno.green}Digite o nome do contato que deseja buscar: '
            f'{cores.Estilos.reset}')
        resultado: tuple = buscar_contato(busca)
        if resultado:
            for contato in resultado[0]:
                if busca.upper() in contato[0].upper():
                    nome_vermelho = f'{cores.Contorno.red}{busca.upper()}{cores.Contorno.green}'
                    novo_nome = contato[0].upper().replace(
                        busca.upper(), nome_vermelho)
                    print(imprimir_contato(novo_nome, contato[1]["telefone"],
                                           contato[1]["endereco"], contato[1]["email"]))
            print(contatos_encontrados(resultado[1]))
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
    elif opcao == '6':
        if AGENDA:
            exporting_status: bool = salvar_agenda()
            if exporting_status:
                print(
                    f'{cores.Contorno.green}Agenda salva com sucesso!!!{cores.Estilos.reset}')
        else:
            print(
                f'{cores.Contorno.red}Nao ha nada para se salvar!!!{cores.Estilos.reset}')
    else:
        print(f'{cores.Contorno.red}Saindo...!!!')
        sys.exit()
