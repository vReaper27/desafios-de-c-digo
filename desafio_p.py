
def calcular_operacoes(nome_arquivo):
    
    """
    
    Função feita para calcular as equações solicitadas.

    parametros: arquivo fornecido pelo criador do desafio.
    retorno: resultado.
    
    """
    

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:  # Passar pelas linhas do arquivo.
            expressao = linha.strip()  # "Formata-las".
            
            try: # Tentativa de realização da equação sem manipulação dos dados fornecidos.

                resultado = eval(expressao)
                print(f"{resultado}")


            except TypeError as erro:  # Captação do erro, e correção da equação.

                expressao_corrigida = expressao.replace("^", "**")
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