class Usuario:
    def __init__(self, nome, idade, email):
        if not nome:
            raise ValueError("Erro: O nome não pode ser vazio.")
        if not isinstance(idade, int):
            raise TypeError("Erro: A idade deve ser um número inteiro.")
        if "@" not in email:
            raise ValueError("Erro: O email deve conter um '@'.")
        
        self.nome = nome
        self.idade = idade
        self.email = email

# Testando o funcionamento e captura de exceções
try:
    usuario1 = Usuario("", 25, "teste@example.com")  # Deve lançar ValueError para o nome vazio
except ValueError as e:
    print(e)

try:
    usuario2 = Usuario("João", "vinte e cinco", "teste@example.com")  # Deve lançar TypeError para idade
except TypeError as e:
    print(e)

try:
    usuario3 = Usuario("Maria", 30, "testeexample.com")  # Deve lançar ValueError para email inválido
except ValueError as e:
    print(e)

try:
    usuario4 = Usuario("Lucas", 28, "lucas@example.com")  # Dados válidos
    print(f"Usuário criado: {usuario4.nome}, {usuario4.idade} anos, email: {usuario4.email}")
except (ValueError, TypeError) as e:
    print(e)

