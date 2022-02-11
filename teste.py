try:
    with open('emails.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        for linha in data:
            print(linha.strip())
except FileNotFoundError:
    print('Arquivo nao existe!!')
