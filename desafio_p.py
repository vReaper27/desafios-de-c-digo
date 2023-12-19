def calcular_operacoes(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            expressao = linha.strip()
            
            try:
                resultado = eval(expressao)
                print(f"{resultado}")

            except TypeError as erro:
                #corrigindo expressão 
                #print(expressao)
                expressao_corrigida = expressao.replace("^", "**")
                #print(expressao_corrigida)
                resultado = eval(expressao_corrigida)
                print(f"{resultado}")
            
            except SyntaxError as erro:
                print("ERR SYNTAX")

            except ZeroDivisionError as erro:
                print("ERR DIVBYZERO")

# Nome do arquivo de operações
arquivo_operacoes = 'C:/Users/Projeto 2/Desktop/d14.txt'

# Calcular operações do arquivo
calcular_operacoes(arquivo_operacoes)