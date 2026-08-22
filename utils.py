def validar_valor(valor_str):
    try:
        valor = float(valor_str)
        if valor < 0:
            print("Erro: o valor não pode ser negativo.")
            return None
        return valor
    except ValueError:
        print("Erro: digite um número válido.")
        return None

def validar_id(id_str):
    if id_str.isdigit():
        return int(id_str)
    else:
        print("Erro: o ID deve ser um número inteiro.")
        return None

def formatar_moeda(valor):
    return f"R$ {valor:.2f}"

def separador():
    print("-" * 40)
    
    