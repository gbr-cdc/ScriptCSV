import csv
import re

def separar_elementos(nome):
    # Inicializa a lista para armazenar os elementos separados
    elementos_separados = []
    
    # Divide a string usando o espaço como separador
    partes = nome.split(' ')
    for parte in partes:
        # Divide cada parte usando o hífen como separador
        elementos_hifen = parte.split('-')
        for elemento_hifen in elementos_hifen:
            # Divide cada elemento usando a barra como separador
            elementos_barra = elemento_hifen.split('/')
            # Adiciona cada elemento separado à lista final
            elementos_separados.extend(elementos_barra)
    
    return elementos_separados

cores_abreviacoes = {
    "vermelho": ["vermelho", "vermelha", "vmo", "vm", "verm", "vml"],
    "verde": ["verde", "vd", "vrd", "vde", "green"],
    "azul": ["azul", "az", "azu", "azl", "azm", "blue"],
    "amarelo": ["amarelo", "amarela", "am", "amr", "yellow"],
    "laranja": ["laranja", "lr", "lja", "lrj", "orange"],
    "roxo": ["roxo", "rxo", "rx", "purple"],
    "rosa": ["rosa", "rs", "ros"],
    "pink": ["pink", "pk"],
    "dark": ["dark", "da"],
    "ciano": ["ciano", "cn", "cia"],
    "magenta": ["magenta", "mg", "mgt", "mgn"],
    "branco": ["branco", "branca", "br", "bc", "bco", "white"],
    "preto": ["preto", "preta", "pt", "pto", "black"],
    "cinza": ["cinza", "cz", "cza", "cnz", "gray"],
    "polido": ["polido", "polida"],
    "transparente": ["transparente", "transp"],
    "prata": ["prata", "prt", "pta"]
}

tamanhos = ['P', 'PP', 'M', 'G', 'GG']
padrao = r'\b\d+(?:,\d+)?(?:ML|L)\b'
adjetivos = ["fosco", "neon", "brilhante"]

def is_cor(palavra):
    palavra = palavra.lower()
    for cor in cores_abreviacoes:
        if palavra in cores_abreviacoes[cor]:
            return cor
    return "none"

def is_tamanho(palavra):
    if palavra.upper() in tamanhos:
        return palavra
    return "none"

def is_volume(palavra):
    if re.match(padrao, palavra.upper()):
        return palavra
    return "none"

output = []
with open("csv.csv", newline='') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    i = 0
    for linha in leitor_csv:
        i = i + 1;
        nome = linha['Nome']
        for pos, char in enumerate(nome):
            if not char.isalnum():
                nome = nome[:pos] + ' ' + nome[pos+1:]
        result = {
            "Identificador URL": linha['Identificador URL'],
            "Nome": linha['Nome'],
            "Categoria": linha['Categoria'],
            "Nome da variação 1": linha['Nome da variação 1'],
            "Valor da variação 1": linha['Valor da variação 1'],
            "Nome da variação 2": linha['Nome da variação 2'],
            "Valor da variação 2": linha['Valor da variação 2'],
            "Nome da variação 3": linha['Nome da variação 3'],
            "Valor da variação 3": linha['Valor da variação 3'],
            "Preço": linha['Preço'],
            "Preço promocional": linha['Preço promocional'],
            "Peso (kg)": linha['Peso (kg)'],
            "Altura (cm)": linha['Altura (cm)'],
            "Largura (cm)": linha['Largura (cm)'],
            "Comprimento (cm)": linha['Comprimento (cm)'],
            "Estoque": linha['Estoque'],
            "SKU": linha['SKU'],
            "Código de barras": linha['Código de barras'],
            "Exibir na loja": linha['Exibir na loja'],
            "Frete gratis": linha['Frete gratis'],
            "Descrição": linha['Descrição'],
            "Tags": linha['Tags'],
            "Título para SEO": linha['Título para SEO'],
            "Descrição para SEO": linha['Descrição para SEO'],
            "Marca": linha['Marca'],
            "Produto Físico": linha['Produto Físico'],
            "MPN (Cód. Exclusivo, Modelo Fabricante)": linha['MPN (Cód. Exclusivo, Modelo Fabricante)'],
            "Sexo": linha['Sexo'],
            "Faixa etária": linha['Faixa etária'],
            "Custo": linha['Custo']
        }
        elemento_trocado = ''
        remover = []
        elementos = nome.split(' ')
        for index, elemento in enumerate(elementos):
            elemento_trocado = elemento.replace(".", "")
            cor = is_cor(elemento_trocado)
            if cor != "none":
                remover.append(elemento)
                if (index + 1) < len(elementos) and elementos[index + 1] in adjetivos:
                    cor = cor + " " + elementos_separados[index + 1]
                if result['Nome da variação 1'] == '':
                    result['Nome da variação 1'] = "Cor"
                    result['Valor da variação 1'] = cor.capitalize()
                elif result['Nome da variação 2'] == '':
                    result['Nome da variação 2'] = "Cor"
                    result['Valor da variação 2'] = cor.capitalize()
                elif result['Nome da variação 3'] == '':
                    result['Nome da variação 3'] = "Cor"
                    result['Valor da variação 3'] = cor.capitalize()
        elementos = nome.split(' ')
        if i == 475:
            print(nome)
            print(elementos)

        for elemento in elementos:
            tamanho = is_tamanho(elemento)
            if i == 475:
                    print("t:" + str(tamanho))
            if tamanho != "none":
                if i == 475:
                    print("e:" + str(elemento))
                remover.append(elemento)
                if result['Nome da variação 1'] == '':
                    result['Nome da variação 1'] = "Tamanho"
                    result['Valor da variação 1'] = tamanho
                elif result['Nome da variação 2'] == '':
                    result['Nome da variação 2'] = "Tamanho"
                    result['Valor da variação 2'] = tamanho
                elif result['Nome da variação 3'] == '':
                    result['Nome da variação 3'] = "Tamanho"
                    result['Valor da variação 3'] = tamanho
                elif result['Nome da variação 3'] == "Cor":
                    result['Nome da variação 3'] = "Tamanho"
                    result['Valor da variação 3'] = tamanho
                elif result['Nome da variação 2'] == "Cor":
                    result['Nome da variação 2'] = "Tamanho"
                    result['Valor da variação 2'] = tamanho
            volume = is_volume(elemento)
            if volume != "none":
                remover.append(elemento)
                if result['Nome da variação 1'] == '':
                    result['Nome da variação 1'] = "Volume"
                    result['Valor da variação 1'] = volume
                elif result['Nome da variação 2'] == '':
                    result['Nome da variação 2'] = "Volume"
                    result['Valor da variação 2'] = volume
                elif result['Nome da variação 3'] == '':
                    result['Nome da variação 3'] = "Volume"
                    result['Valor da variação 3'] = volume
                elif result['Nome da variação 3'] == "Cor":
                    result['Nome da variação 3'] = "Volume"
                    result['Valor da variação 3'] = volume
                elif result['Nome da variação 2'] == "Cor":
                    result['Nome da variação 2'] = "Volume"
                    result['Valor da variação 2'] = volume

        for elemento in remover:
            elementos.remove(elemento)  

        result['Nome'] = ' '.join(elementos)
        output.append(result)

cabeçalho = ("Identificador URL", "Nome", "Categoria", "Nome da variação 1", "Valor da variação 1", "Nome da variação 2", "Valor da variação 2", "Nome da variação 3", "Valor da variação 3", "Preço", "Preço promocional", "Peso (kg)", "Altura (cm)", "Largura (cm)", "Comprimento (cm)", "Estoque", "SKU", "Código de barras", "Exibir na loja", "Frete gratis", "Descrição", "Tags", "Título para SEO", "Descrição para SEO", "Marca", "Produto Físico", "MPN (Cód. Exclusivo, Modelo Fabricante)", "Sexo", "Faixa etária", "Custo")

# Escrever os dados em um novo arquivo CSV
with open('out.csv', mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.DictWriter(arquivo_csv, cabeçalho)
    escritor_csv.writeheader()
    # Escrever linhas de dados
    for result in output:
        escritor_csv.writerow(result)
