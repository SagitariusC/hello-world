produto = input("Digite o nome do produto: ")
preco = float(input(f"Digite o preço do produto {produto} R$"))
valida = int(input("Vai a pagar a vista? Se sim digite 1 se for a prazo, digite 2: \n"))
if valida == 1:
   desc = preco*0.95
   print(f"Recebeu um desconto de %5 e a preço final do produto {produto} é de R${desc:.2f}, lindão")
elif valida == 2:
  acre = preco*1.10
  print(f"Recebeu um acrescimo de %10 e a preço final do produto {produto} é de R${acre:.2f}")
else:
  print("Fiado só quando o palmeiras ganhar mundial.")