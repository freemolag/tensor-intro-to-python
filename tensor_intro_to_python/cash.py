def cash(deposit, interest, years):
    return int(deposit * ((1 + interest / 100) ** years))
