from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import math


#  retorna o valor da soma entre os dois parâmetros
def summ(v1, v2):
    return print("Teste Summ")


#  retorna o valor da subtração entre os dois parâmetros
def sub(v1, v2):
    return print("Teste Sub")


#  retorna o valor da divisão entre os dois parâmetros
def div(v1, v2):
    return print("Teste Div")


#  retorna o valor da multiplicação entre os dois parâmetros
def mult(v1, v2):
    return print("Teste Mult")


#  retorna o valor da raiz quadrada do valor recebido por parâmetro
def square(v1):
    return print(math.sqrt(v1))


valueInitial = float(input("Insira o Primeiro Valor: "))

choiseCalculate = inquirer.select(
    message="Como deseja fazer Calular ?",
    choices=[
        Choice(value=1, name="Soma"),
        Choice(value=2, name="Subtração"),
        Choice(value=3, name="Divisão"),
        Choice(value=4, name="Multiplicação"),
        Choice(value=5, name="Raiz Quadrada"),
    ],
    default=None,
).execute()

match choiseCalculate:
    case 1:
        valueSegundary = float(input("Insira o Segundo Valor: "))
        summ(v1=valueInitial, v2=valueSegundary)
    case 2:
        valueSegundary = float(input("Insira o Segundo Valor: "))
        sub(v1=valueInitial, v2=valueSegundary)
    case 3:
        valueSegundary = float(input("Insira o Segundo Valor: "))
        div(v1=valueInitial, v2=valueSegundary)
    case 4:
        valueSegundary = float(input("Insira o Segundo Valor: "))
        mult(v1=valueInitial, v2=valueSegundary)
    case 5:
        square(v1=valueInitial)
