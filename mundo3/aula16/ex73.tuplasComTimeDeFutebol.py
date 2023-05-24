times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", 
"Cruzeiro", "Flamengo", "Vasco", "Chapecoence", "Atlético", 
"Botafogo", "Atlético-PR", "Bahia", "São Paulo", "Fluminense", 
"Sport Recife", "EC Vitória", "Coritiba", "Avaí", "Ponte Preta", 
"Atlético-GO")
print("-=" * 15)
print(f"Lista de times do Brasileirão: {times}")
print("-=" * 15)
print(f"Os cinco primeiros são: {times[0:5]}")
print("-=" * 15)
print(f"Os quatro últimos são: {times[-4:]}")
print("-=" * 15)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 15)
print(f"O Chapecoence está na {times.index('Chapecoence')+1} posição.")