import pixel_art

smile = pixel_art.pixels.Image()
smile.add_row(0, 'yellow')
smile.add_row(1, 'yellow', 'yellow', 'black', 'yellow', 'black', 'yellow', 'yellow')
smile.add_row(2, 'yellow', 'yellow', 'black', 'yellow', 'black', 'yellow', 'yellow')
smile.add_row(3, 'yellow')
smile.add_row(4, 'yellow', 'black', 'yellow', 'yellow', 'yellow', 'black', 'yellow')
smile.add_row(5, 'yellow', 'yellow', 'black', 'black', 'black', 'yellow', 'yellow')
smile.add_row(6, 'yellow')
smile.display()
