
from conta_bancaria import ContaBancaria, SaldoInsuficienteException

# Criando as três contas
ana = ContaBancaria("123", "Ana Lima")
carlos = ContaBancaria("456", "Carlos Souza")
maria = ContaBancaria("789", "Maria Silva")

# Definindo os saldos iniciais
ana.depositar(500)
carlos.depositar(300)
maria.depositar(100)

# Primeira transferência: Ana transfere R$ 200 para Carlos
ana.transferir(carlos, 200)

# Segunda transferência: Carlos transfere R$ 150 para Maria
carlos.transferir(maria, 150)

# Terceira transferência: Maria tenta transferir R$ 500 para Ana
try:
    maria.transferir(ana, 500)
except SaldoInsuficienteException as erro:
    print(f"Erro na transferência de Maria para Ana: {erro}")

# Transferência para a própria conta
try:
    ana.transferir(ana, 50)
except ValueError as erro:
    print(f"Erro na transferência para a própria conta: {erro}")

# Exibindo os saldos finais
print("\n--- Saldos finais ---")
print(f"Ana Lima (conta 123): R$ {ana.get_saldo():.2f}")
print(f"Carlos Souza (conta 456): R$ {carlos.get_saldo():.2f}")
print(f"Maria Silva (conta 789): R$ {maria.get_saldo():.2f}")
