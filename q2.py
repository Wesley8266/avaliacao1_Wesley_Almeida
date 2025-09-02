produtos = int(input("informe a quantidade de produtos: "))
for i in range (produtos):
    preco = float(input("informe o preço dos produtos: "))
if preco >= 50:
    print(f"o numero de produtos maior que 50 é {i}")

