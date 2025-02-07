# 01_ Implementem uma estrutura de condicional
    # if - elif
    # math - case
    # função - elevar a potencia
    # raiz quadrado
    # resto de divisão

calc = input("Qual operação você quer fazer? Digite: \n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - porcentagem\n6 - potencialização")
a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))

if calc == 1:
    def soma(a, b):
        return [a+b,"soma"]
elif calc == 2:
    def sub(a, b):
        return [a-b, "subtração"]
elif calc == 3:
    def mult(a, b):
        return [a*b, "multiplicação"]
elif calc == 4:
    def div(a, b):
        return [a/b, "divisão"]
elif calc == 5:
    def porc(a, b):
        return [(a/100)*b, "porcetagem"]
else:
    def poten(a, b):
        return [a**b, "potencialização"]
    


print(f'O resultado da operação de {calc[1]} de {a} e {b} é {calc[0]}')
