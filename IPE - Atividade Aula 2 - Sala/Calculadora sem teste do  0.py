op=input("Qual Operação Matemática Deseja Utilizar +/*///-? ")
n1=float(input("Entre com n1 "))
n2=float(input("Entre com n2 "))
if op=="+":
    resultado=n1+n2
    print("Resultado Soma:",resultado)
elif op=="*":
    resultado=n1*n2
    print("Resultado Multiplicação:",resultado)
elif op=="/":
    resultado=n1/n2
    print("Resultado Divisão:", resultado  )
elif op=="-":
    resultado=n1-n2
    print("Resultado Subtração: ", resultado)
else:
    print("Opção inválida")
print("Programa Encerrado")