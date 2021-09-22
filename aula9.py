import shutil
# #arquivo = open('teste.txt', 'w') #apenas escreve
# arquivo = open('teste.txt', 'a')   #atualiza a escrita ou adiciona
# #arquivo.write('Minha primeira escrita\n')
# arquivo.write('\nSegunda linha')
# arquivo.close()

#EXEMPLO CRIAR AQUIVO COM CAMINHO ESPECIFICADO
# def escrever_arquivo(texto):
#     diretorio = 'C:/Projetos/Python/teste.txt'
#     arquivo = open(diretorio, 'w')
#     arquivo.write(texto)
#     arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_aquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media =  []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas [0]
        lista_notas.pop(0)
        print(aluno)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/')

if __name__ == '__main__':
    move_arquivo('teste.txt')
    #copia_arquivo('notas.txt')
    #media_notas('notas.txt')

    #escrever_arquivo('Primeira linha.\n')
    #aluno = 'Cezar: 7, 9, 6, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_aquivo('teste.txt')