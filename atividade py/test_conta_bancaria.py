import pytest

from conta_bancaria import (
    ContaBancaria,
    SaldoInsuficienteException
)


def test_criar_conta():
    conta = ContaBancaria("123", "Ana Lima")

    assert conta.numero == "123"
    assert conta.titular == "Ana Lima"
    assert conta.get_saldo() == 0.0


def test_numero_invalido():
    for numero in [None, "", "   "]:
        with pytest.raises(ValueError):
            ContaBancaria(numero, "Ana Lima")


def test_titular_invalido():
    with pytest.raises(ValueError):
        ContaBancaria("123", "Al")


def test_depositar():
    conta = ContaBancaria("123", "Ana Lima")
    conta.depositar(100)

    assert conta.get_saldo() == 100.0


@pytest.mark.parametrize("valor", [0, -50])
def test_deposito_invalido(valor):
    conta = ContaBancaria("123", "Ana Lima")

    with pytest.raises(ValueError):
        conta.depositar(valor)

    assert conta.get_saldo() == 0.0


def test_sacar():
    conta = ContaBancaria("123", "Ana Lima")
    conta.depositar(100)
    conta.sacar(40)

    assert conta.get_saldo() == 60.0


def test_sacar_saldo_total():
    conta = ContaBancaria("123", "Ana Lima")
    conta.depositar(100)
    conta.sacar(100)

    assert conta.get_saldo() == 0.0


def test_saque_sem_saldo():
    conta = ContaBancaria("123", "Ana Lima")
    conta.depositar(100)

    with pytest.raises(SaldoInsuficienteException):
        conta.sacar(100.01)

    assert conta.get_saldo() == 100.0


@pytest.mark.parametrize("valor", [0, -10])
def test_saque_invalido(valor):
    conta = ContaBancaria("123", "Ana Lima")
    conta.depositar(100)

    with pytest.raises(ValueError):
        conta.sacar(valor)

    assert conta.get_saldo() == 100.0


def test_transferir():
    origem = ContaBancaria("123", "Ana Lima")
    destino = ContaBancaria("456", "João Silva")
    origem.depositar(100)

    origem.transferir(destino, 30)

    assert origem.get_saldo() == 70.0
    assert destino.get_saldo() == 30.0


def test_transferir_para_propria_conta():
    conta = ContaBancaria("123", "Ana Lima")
    conta.depositar(100)

    with pytest.raises(ValueError):
        conta.transferir(conta, 30)

    assert conta.get_saldo() == 100.0


def test_transferencia_sem_saldo():
    origem = ContaBancaria("123", "Ana Lima")
    destino = ContaBancaria("456", "João Silva")
    origem.depositar(100)

    with pytest.raises(SaldoInsuficienteException):
        origem.transferir(destino, 150)

    assert origem.get_saldo() == 100.0
    assert destino.get_saldo() == 0.0


def test_transferir_para_destino_nulo():
    origem = ContaBancaria("123", "Ana Lima")
    origem.depositar(100)

    with pytest.raises(ValueError):
        origem.transferir(None, 30)

    assert origem.get_saldo() == 100.0


def test_transferencia_invalida_nao_altera_saldos():
    origem = ContaBancaria("123", "Ana Lima")
    destino = ContaBancaria("456", "João Silva")
    origem.depositar(100)
    destino.depositar(20)

    with pytest.raises(ValueError):
        origem.transferir(destino, 0)

    assert origem.get_saldo() == 100.0
    assert destino.get_saldo() == 20.0


def test_consultar_saldo():
    conta = ContaBancaria("123", "Ana Lima")
    conta.depositar(100)

    assert conta.get_saldo() == 100.0
    assert conta.get_saldo() == 100.0
