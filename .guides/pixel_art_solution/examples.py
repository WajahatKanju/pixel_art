import pixel_art.pixels as p

def colors():
  print(f"{p.black}{p.Back.RESET} - 'black'")
  print(f"{p.red}{p.Back.RESET} - 'red'")
  print(f"{p.green}{p.Back.RESET} - 'green'")
  print(f"{p.yellow}{p.Back.RESET} - 'yellow'")
  print(f"{p.blue}{p.Back.RESET} - 'blue'")
  print(f"{p.magenta}{p.Back.RESET} - 'magenta'")
  print(f"{p.cyan}{p.Back.RESET} - 'cyan'")
  print(f"{p.white}{p.Back.RESET} - 'white'")

def house():
  img = p.Image()
  img.add_row(0, 'cyan')
  img.add_row(1, 'cyan', 'yellow', 'cyan', 'red', 'cyan', 'cyan', 'cyan')
  img.add_row(2, 'cyan', 'cyan', 'red', 'red', 'red', 'cyan', 'cyan')
  img.add_row(3, 'cyan', 'red', 'red', 'red', 'red', 'red', 'cyan')
  img.add_row(4, 'cyan', 'white', 'white', 'white', 'white', 'white', 'cyan')
  img.add_row(5, 'cyan', 'white', 'white', 'black', 'white', 'white', 'cyan')
  img.add_row(6, 'green')
  img.display()

def notes():
  img = p.Image(16, 14)
  img.add_row(0, 'magenta')
  img.add_row(1, 'magenta', 'magenta', 'magenta', 'magenta',
                 'magenta', 'magenta', 'black', 'black',
                 'black', 'black', 'black', 'black',
                 'black', 'black', 'black', 'magenta')
  img.add_row(2, 'magenta', 'magenta', 'magenta', 'magenta',
                 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(3, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'white', 'white',
                 'white', 'white', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(4, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'black',
                 'black', 'black', 'black', 'black',
                 'black', 'white', 'black', 'magenta')
  img.add_row(5, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(6, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(7, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(8, 'magenta', 'magenta', 'black', 'black',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'black', 'black',
                 'black', 'white', 'black', 'magenta')
  img.add_row(9, 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'black', 'magenta',
                 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(10, 'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta',
                  'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta')
  img.add_row(11, 'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta',
                  'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta')
  img.add_row(12, 'magenta', 'magenta', 'black', 'black',
                  'black', 'black', 'magenta', 'magenta',
                  'magenta', 'magenta', 'black', 'black',
                  'black', 'black', 'magenta', 'magenta')
  img.add_row(13, 'magenta')
  img.display()