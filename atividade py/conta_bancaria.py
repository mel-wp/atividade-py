class SaldoInsuficienteException(Exception):
    pass


class ContaBancaria:

    def __init__(self, numero, titular):
        if numero is None or not str(numero).strip():
            raise ValueError("Número obrigatório.")

        if titular is None or len(titular.strip()) < 3:
            raise ValueError(
                "Titular deve ter pelo menos 3 caracteres."
            )

        self.numero = str(numero).strip()
        self.titular = titular.strip()
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo

    # Mantém compatibilidade com o nome do método original.
    def getSaldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError(
                "O depósito deve ser positivo."
            )

        self.__saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError(
                "O saque deve ser positivo."
            )

        if valor > self.__saldo:
            raise SaldoInsuficienteException(
                "Saldo insuficiente."
            )

        self.__saldo -= valor

    def transferir(self, destino, valor):
        if destino is None:
            raise ValueError(
                "A conta de destino não pode ser nula."
            )

        if destino is self:
            raise ValueError(
                "Não é possível transferir para a mesma conta."
            )

        if not isinstance(destino, ContaBancaria):
            raise ValueError("Conta de destino inválida.")

        if valor <= 0:
            raise ValueError(
                "O valor deve ser positivo."
            )

        if valor > self.__saldo:
            raise SaldoInsuficienteException(
                "Saldo insuficiente."
            )

        # Os saldos só mudam depois de validar a operação.
        self.__saldo -= valor
        destino.__saldo += valor