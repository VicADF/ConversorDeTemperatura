resposta = input(" Pressione C para converter Celsius em Fahrenheit ou F para converter Fahrenheit em Celsius ")
valor_temperatura = input(" Qual o valor da temperatura? ")

if resposta == 'C':
  F = (float (valor_temperatura) * 1.8) + 32
  print(valor_temperatura + " convertido em Fahrenheit é " + str(F))
      
if resposta == 'F':
  C = (float(valor_temperatura) - 32) / 1.8
  print(valor_temperatura + " convertido em Celsius é " + str(C))