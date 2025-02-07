# 01_ Implementem uma estrutura de condicional
    # if - elif
    # math - case
    # função - elevar a potencia
    # raiz quadrado
    # resto de divisão

numero = int(input("Qual operação você quer fazer? Digite: \n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - porcentagem\n6 - potencialização\n"))
a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))

if numero == 1:
    def soma(a, b):
        return [a+b,"soma"]
    calc = soma(a,b)
elif numero == 2:
    def sub(a, b):
        return [a-b, "subtração"]
    calc = sub(a, b)
elif numero == 3:
    def mult(a, b):
        return [a*b, "multiplicação"]
    calc = mult(a, b)
elif numero == 4:
    def div(a, b):
        return [a/b, "divisão"]
    calc = div(a, b)
elif numero == 5:
    def porc(a, b):
        return [(a/100)*b, "porcetagem"]
    calc = porc(a, b)
else:
    def poten(a, b):
        return [a**b, "potencialização"]
    calc = poten(a, b)
    


print(f'O resultado da operação de {calc[1]} de {a} e {b} é {calc[0]}')
