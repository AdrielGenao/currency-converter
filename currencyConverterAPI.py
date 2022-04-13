import requests
s=requests.session()
Key="f659c4c8c560e07d702022354112b198"
parameters={"access_key":Key,"source":"USD","currencies":"EUR,GBP,MXN,JPY"}
r=s.get("http://api.currencylayer.com/live",params=parameters)
response=r.json()
# Currency Converter for US Dollar to Euro, Pound, Peso, or Yen
change = input("What kind of currency do you want to convert to? (Euro, Pound, Peso, or Yen)\n")
amount = input("What amount of dollars do you want to convert?\n$")
if change == 'Euro' or change == 'euro' or change == 'euros' or change == 'Euros':
    final = float(amount) * response['quotes']['USDEUR']
    print("$" + str(amount) + " would convert to €" + str(final))
elif change == 'Pound' or change == 'pound' or change == 'pounds' or change == 'Pounds':
    final = float(amount) * response['quotes']['USDGBP']
    print("$" + str(amount) + " would convert to £" + str(final))
elif change == 'yen' or change == 'Yen':
    final = float(amount)  * response['quotes']['USDJPY']
    print("$" + str(amount) + " would convert to ¥" + str(final))
elif change == 'peso' or change == 'Peso' or change == 'pesos' or change == 'Pesos':
    final = float(amount) * response['quotes']['USDMXN']
    print("$" + str(amount) + " would convert to Mex$" + str(final))
else:
  print("Error. Currency name given does not match.")    
