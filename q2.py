contador = 0
produtos = int(input("informe a quantidade de produtos: "))
for i in range (produtos):
    preço = float(input("informe o preço dos produtos: "))
    contador += preço
    print(f"o valor total é {contador}")
