from colorama import init, Back, Style

init(autoreset=True)

black = Back.BLACK + '  '
red = Back.RED + '  '
green = Back.GREEN + '  '
yellow = Back.YELLOW + '  '
blue = Back.BLUE + '  '
magenta = Back.MAGENTA + '  '
cyan = Back.CYAN + '  '
white = Back.WHITE + '  '

colors_dict = {
  'black' : black,
  'red' : red,
  'green' : green,
  'yellow' : yellow,
  'blue' : blue,
  'magenta' : magenta, 
  'cyan' : cyan,
  'white' : white
}

class Image():
  def __init__(self, w=7, h=7):
    self.width = w
    self.height = h
    self.img = self.init_list()

  def init_list(self):
    lst = []
    for row in range(self.height):
      lst.append([])
    return lst

  def display_row(self, row):
    for pixel in row:
      print(pixel, end='')
    print()

  def display(self):
    for row in self.img:
      self.display_row(row)

  def convert_color(self, str_clr):
    if str_clr in colors_dict:
      return colors_dict[str_clr]
    else:
      return black

  def add_row(self, *args):
    if len(args) == 2:
      colors = [self.convert_color(args[1]) for i in range(self.width)]
      self.img[args[0]] = colors
    else:
      color_params = args[1:]
      colors = [self.convert_color(arg) for arg in color_params]
      self.img[args[0]] = colors

  def clear(self):
    print(Style.RESET_ALL)
