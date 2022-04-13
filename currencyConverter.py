# Currency Converter for US Dollar, Euro, Pound, Peso, and Yen
original = input("What kind of currency do you want to convert? (Dollar, Euro, Pound, Peso, or Yen)\n")

# Dollars
if original == 'Dollar' or original == 'dollar' or original == 'Dollars' or original == 'dollars':
    amount = input("What amount of dollars do you want to convert?\n$")
    change = input("To what currency type would you like to convert to? (Euro, Pound, Peso, or Yen)\n")
    if change == 'Euro' or change == 'euro' or change == 'euros' or change == 'Euros':
        final = float(amount) * 0.83144
        print("$" + str(amount) + " would convert to €" + str(final))
    if change == 'Pound' or change == 'pound' or change == 'pounds' or change == 'Pounds':
        final = float(amount) * 0.72
        print("$" + str(amount) + " would convert to £" + str(final))
    if change == 'yen' or change == 'Yen':
        final = float(amount) * 108.40
        print("$" + str(amount) + " would convert to ¥" + str(final))
    if change == 'peso' or change == 'Peso' or change == 'pesos' or change == 'Pesos':
        final = float(amount) * 21.32
        print("$" + str(amount) + " would convert to Mex$" + str(final))

# Yen
if original == 'yen' or original == 'Yen':
    amount = input("What amount of yen do you want to convert?\n¥")
    change = input("To what currency type would you like to convert to? (Dollar, Euro, Pound, or Peso)\n")
    if change == 'Dollar' or change == 'dollar' or change == 'dollars' or change == 'Dollars':
        final = float(amount) * 0.0092
        print("¥" + str(amount) + " would convert to $" + str(final))
    if change == 'Euro' or change == 'euro' or change == 'euros' or change == 'Euros':
        final = float(amount) * 0.0077
        print("¥" + str(amount) + " would convert to €" + str(final))
    if change == 'pound' or change == 'pound' or change == 'pounds' or change == 'Pounds':
        final = float(amount) * 0.0067
        print("¥" + str(amount) + " would convert to £" + str(final))
    if change == 'peso' or change == 'Peso' or change == 'pesos' or change == 'Pesos':
        final = float(amount) * 0.20
        print("¥" + str(amount) + " would convert to Mex$" + str(final))  

# Pound
if original == 'Pound' or original == 'pound' or original == 'Pounds' or original == 'pounds':
    amount = input("What amount of pounds do you want to convert?\n£")
    change = input("To what currency type would you like to convert to? (Dollar, Euro, Peso, or Yen)\n")
    if change == 'Dollar' or change == 'dollar' or change == 'dollars' or change == 'Dollars':
        final = float(amount) * 1.38
        print("£" + str(amount) + " would convert to $" + str(final))
    if change == 'Euro' or change == 'euro' or change == 'euros' or change == 'Euros':
        final = float(amount) * 1.16
        print("£" + str(amount) + " would convert to €" + str(final))
    if change == 'yen' or change == 'Yen':
        final = float(amount) * 149.89
        print("£" + str(amount) + " would convert to ¥" + str(final))
    if change == 'peso' or change == 'Peso' or change == 'pesos' or change == 'Pesos':
        final = float(amount) * 29.50
        print("£" + str(amount) + " would convert to Mex$" + str(final))

# Euro
if original == 'Euro' or original == 'euro' or original == 'Euros' or original == 'euros':
    amount = input("What amount of euros do you want to convert?\n€")
    change = input("To what currency type would you like to convert to? (Dollar, Pound, Peso, or Yen)\n")
    if change == 'Dollar' or change == 'dollar' or change == 'dollars' or change == 'Dollars':
        final = float(amount) * 1.19
        print("€" + str(amount) + " would convert to $" + str(final))
    if change == 'Pound' or change == 'pound' or change == 'pounds' or change == 'Pounds':
        final = float(amount) * 0.86
        print("€" + str(amount) + " would convert to £" + str(final))
    if change == 'yen' or change == 'Yen':
        final = float(amount) * 129.18
        print("€" + str(amount) + " would convert to ¥" + str(final))
    if change == 'peso' or change == 'Peso' or change == 'Pesos' or change == 'peso':
        final = float(amount) * 25.40
        print("€" + str(amount) + " would convert to Mex$" + str(final))

# Peso
if original == 'Peso' or original == 'pesos' or original == 'Pesos' or original == 'pesos':
    amount = input("What amount of pesos do you want to convert?\nMex$")
    change = input("To what currency type would you like to convert to? (Dollar, Pound, Peso, or Yen)\n")
    if change == 'Dollar' or change == 'dollar' or change == 'dollars' or change == 'Dollars':
        final = float(amount) * 0.048
        print("Mex$" + str(amount) + " would convert to $" + str(final))
    if change == 'Pound' or change == 'pound' or change == 'pounds' or change == 'Pounds':
        final = float(amount) * 0.035
        print("Mex$" + str(amount) + " would convert to £" + str(final))
    if change == 'yen' or change == 'Yen':
        final = float(amount) * 5.27
        print("Mex$" + str(amount) + " would convert to ¥" + str(final))
    if change == 'euro' or change == 'Euro' or change == 'euros' or change == 'Euros':
        final = float(amount) * 0.040
        print("Mex$" + str(amount) + " would convert to €" + str(final))
