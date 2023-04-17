n = int(input("Qual o termo desejar verificar:"))
t1 = 0
t2 = 1
t3 = 0
print(f"{t1} -> {t2}",end='')
cont = 3 
while cont <= n:
    t3 = t1 + t2
    print(f" -> {t3}",end='')
    t1 = t2
    t2 = t3
    cont += 1 
print(" -> FIM")
if n == 0 or n == 1:
        print("O número informado pertence a sequência")
elif n == t3:
        print("O número informado pertence a sequência")
else:
        print("O número informado não pertence a sequência")