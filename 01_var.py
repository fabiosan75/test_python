import random

options = ('piedra','papel','tijera')
num_games = 0
max_games = 3
primos = [2,3,5,7,11,13,17,19,23,29,31,37,41]
print(primos[3:10:2])

while num_games <= max_games:
  user_option = input('Digite su opcion : ')

  if not user_option in options:
    print('Opcion errada')
    continue
  else:
    game_option = random.choice(options)
    if(user_option == game_option):
      print("Hay Empate !!")
      num_games -= 1
    elif user_option == 'piedra':
      if game_option == 'papel':
        print('GANA GAME papel a piedra!!')
      else:
        print(f"GANA GAME {game_option} a {user_option} !!")
    else:
      if user_option == 'papel':
        if game_option == 'tijera':
          print('GANA GAME tijera a papel !!')
        elif game_option == 'piedra':
          print('GANA JUGADOR papel a piedra !!')
          print(f"GANA GAME {game_option} a {user_option} !!")
      else:
        if game_option == 'papel':
          print('GANA JUGADOR tijera a papel !!')
        else:
          print(f"GANA GAME {game_option} a {user_option} !!")
          
  num_games += 1
      
     
        

