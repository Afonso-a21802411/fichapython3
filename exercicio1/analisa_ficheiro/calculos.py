def calculo_linhas(nome):
    f= open(nome,'r')
    count=0
    for line in f:
        if line != "\n":
            count += 1
    f.close()
    return count

def calcula_carateres(nome):
    f = open(nome,'r')
    data = f.read().replace(" ","").replace("\n","")
    count = 0
    for line in data:
        print(line)
        count += len(line)
        print(count)
    f.close()
    return count

def calcula_palavra_comprida(nome):
    f = open(nome,'r')
    palavraM='a'
    for line in f:
        line= list(line.split(" "))
        for i in line:
            if len(i) > len(palavraM):
                palavraM=i
    f.close()
    return palavraM

def calcula_ocorrencia_de_letras(nome):
    f = open(nome, 'r')
    my_dict = {}
    for line in f:
        line= list(line.split(" "))
        for i in line:
            for caract in i:
                if caract in my_dict and caract !="\n":
                    my_dict[caract] += 1
                elif caract!="\n":
                    my_dict[caract] = 1
    return my_dict


