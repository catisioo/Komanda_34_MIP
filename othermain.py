import random


# NEMAINIT SPONGEBOB, SAVADAK VISS FAILA INDENTATION NOBRUUK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def sad():
  return (
      "⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⢀⣠⣤⣤⣄⡀⠀⠀⢀⣧⣀⣤⡤⣤⣀⠀⠀⠀⠀⡀⠀⠈⠀⠀⠀⠀⠀⠀\n⠀⠀⣠⠞⠉⠀⠈⣉⡓⠒⠚⠉⠴⢶⠀⠈⠉⠉⠢⠋⢻⠃⣤⡶⠾⣍⠙⠒⢒⣒⠋⠉⠉⠙⢷⣆⠀⠀⠀\n⠀⠀⢿⠀⢀⡀⠘⠿⠃⠀⠀⣠⡾⠛⠢⠀⠀⠀⢈⢰⣡⢠⠎⢘⣦⡠⠂⠉⠀⠀⠘⢿⡆⠀⢀⡿⠀⠀⠀\n⠀⠀⠈⢣⡈⠁⠀⢀⣠⣴⣾⣏⣈⠉⠒⢄⡀⠁⡄⠈⢂⣊⡤⠞⠛⣳⣦⣄⣀⡆⠀⠀⠀⢀⡾⠁⠀⠀⠀\n⠀⠀⠀⢠⠟⢉⣿⣿⣿⣿⣿⣿⡿⢿⣦⣈⢹⣅⡗⣮⡟⢁⣠⣾⣿⣿⣿⠿⣿⣿⣏⠛⣿⡉⡇⠀⠀⠀⠀\n⠀⠀⢠⡏⢰⣿⢋⣿⣿⣿⣿⠋⠁⢾⣿⣿⡜⠻⣽⡏⣰⣿⢻⣿⣿⣿⣿⠛⠻⣿⢻⣷⡀⠹⡇⠀⠀⠀⠀\n⠀⠀⣾⢀⣿⡇⣿⣿⣿⣿⣿⣦⣴⣿⣿⢿⡧⠘⣿⢚⣿⡏⣾⣿⣿⣿⣿⣄⣠⣿⡟⣿⡇⠀⢻⠀⠀⠀⠀\n⠀⠀⣿⠸⣿⣤⢿⣿⣿⣿⣿⣿⣿⣿⡟⣿⡗⢀⣇⠌⣿⡄⣿⣿⣿⣿⣿⣿⣿⣿⣗⣼⡏⠀⣾⠀⠀⠀⠀\n⠀⠀⢹⡄⠙⣿⣦⠿⣿⣿⣿⣿⡿⣏⣳⡟⢀⣼⣿⡀⠹⣿⣉⣿⣿⣿⣿⣿⣿⠟⣩⣿⠁⣰⠇⠀⠀⠀⠀\n⠀⠀⠀⠻⣄⡈⠛⠷⣼⣯⣭⣥⣴⠟⠋⣠⠞⣿⢹⡷⣄⡙⠻⣷⣬⣟⣏⣹⣿⡿⠟⢃⣴⠏⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣿⠙⠲⠤⣤⣤⣤⣤⣤⠴⠛⠁⠀⡟⢸⡇⠈⠛⠦⣤⣈⣉⣉⣉⣁⣤⠶⠫⣱⠃⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠸⡇⠀⠀⠀⠀⠀⠉⣉⡍⠁⠁⠀⡡⣿⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣿⠀⠀⢴⡄⠀⠀⠀⠀⠀⢀⡴⣿⡇⠀⡷⣄⠀⠀⠀⠀⡼⠙⢳⡀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣿⣄⠀⠀⣀⡀⠀⠀⠀⢠⠏⠀⢈⡇⠀⡇⠈⢧⠀⠀⡼⠁⠀⠈⡇⠹⠓⣼⠁⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⡼⢻⠀⠘⢿⡿⠆⠀⢴⠛⡄⠀⢸⡇⠠⡇⢠⣈⡼⠀⢧⡘⢾⡷⠃⢀⢸⠛⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⢸⡁⣈⡷⠖⠒⠲⠶⠤⢼⡛⠓⠶⣾⠃⠀⣷⡤⠭⢤⣶⠦⢬⣤⠤⣤⣀⡽⠀⣻⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠈⠙⡟⢻⣤⣤⣤⣤⣀⣀⣈⣓⣊⣽⠀⠀⣇⣙⣖⣋⣀⣀⣀⣀⣀⣠⣹⣿⠛⠉⠀⠀⠀⠀⠀⠠\n⠀⠀⢀⣀⣀⣇⢸⠙⠛⠛⠛⠁⠙⠿⠿⠿⣿⠀⠀⣿⠿⠿⠏⠉⠿⠿⠿⠿⡛⡟⢻⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⣼⠸⣦⢤⣄⣀⣀⣀⣀⣤⡤⣬⣿⣾⣁⣀⣀⣀⣀⣀⣀⣠⣤⣃⡇⣾⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢰⠣⡄⡇⠀⠿⢦⣄⣀⣀⣸⡆⠀⠀⠀⠀⠀⠸⣿⣿⣍⣿⣿⠈⢸⢃⢸⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠸⣧⢻⠇⠀⠀⠀⣧⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣼⠁⠀⠀⢸⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠻⠿⠀⠀⠀⠀⣿⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠀⠀⠀⠸⢿⠇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⡃⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⣷⠀⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢰⣾⣿⣦⣾⣧⣼⡇⠀⠀⠀⠀⠀⠀⠀⢀⣾⣧⣿⣇⣠⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣀⣀⣀⣀⣀⣀⣘⣻⣿⣟⢛⣻⣟⣁⣀⣀⣀⣀⣀⣀⣀⣈⣻⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀"
  )


def happi():
  return (
      "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠉⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⢀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⡇⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⠉⠀⠘⠻⠟⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        \n⡠⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠉⡈⡱⠮⠉⠙⡄⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        \n⣇⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⣾⠀⠼⣿⠃⢼⡧⠄⡄⠀⠀⡇⠀⠀⠀⠀⠀⠀⢀⣠⠖⠊⠉⣣        \n⠹⡆⠀⠀⠀⠉⠲⣄⠀⠀⠀⢸⢦⣀⡰⢧⣀⣀⡴⡁⠀⠀⣷⠀⠀⠀⢀⡠⠖⠉⠀⠀⠀⢰⠇        \n⠀⠹⡄⠀⠀⠀⠀⠀⠑⢦⣠⠏⣄⡀⠀⠀⣀⣠⣤⣿⠓⠀⠸⡀⣠⠔⠋⠀⠀⠀⠀⠀⣰⠃⠀        \n⠀⠀⠙⡄⠀⠀⠀⠀⠀⢠⠏⠀⢸⣿⣿⣿⣿⣿⣿⡏⠀⠀⡠⠟⠁⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀        \n⠀⠀⠀⠘⣆⠀⠀⠀⣠⠏⠠⣤⣿⠟⠛⠟⢋⡽⠋⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀        \n⠀⠀⠀⠀⠈⢦⠀⡴⠃⠀⠀⠈⠙⠓⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⢀⡟⠁⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⢀⡏⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠹⡄⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⢸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⢹⠿⣦⣄⠀⠀⣴⣤⣀⠀⠀⠁⠇⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⢻⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠸⡄⢹⠛⣿⣶⣬⣉⡁⠀⠀⠀⠂⠀⠀⠀⣀⣠⣴⡾⠟⠉⠀⡎⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⢳⡈⣻⠋⠀⠉⢻⡛⠛⢿⠿⠿⠿⠛⠛⠋⠉⠀⠀⣀⣀⡼⠁⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠀⣿⢯⡓⠦⠤⠼⠙⠒⠋⠀⠀⠀⠂⠀⠀⠀⡰⠋⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠸⣇⠀⠈⠓⠦⢤⣀⣀⠀⠀⣀⠀⠀⠂⠀⣠⢍⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠀⠘⡷⠢⠤⠤⢤⠼⠈⠉⠉⢻⡄⠀⠀⠂⡇⢀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⢀⡞⠀⠀⠀⠀⠀⠙⣏⠓⠚⠉⢫⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠋⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⢀⠞⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀        \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣉⣁⠀⠀⠀⠀⠀⠀⠀⠁⠂⠂⠀⠀⠀"
  )


def botvbot():
  return (
      "\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡤⠶⠒⠛⠋⠉⠉⠉⠉⠉⠉⠙⠓⠲⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⡇⢀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠁⡞⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⡃⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⣀⣤⣾⡇⠀⠏⢨⠓⢠⣄⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⣀⡀⣿⣋⣥⣤⣤⣝⣦⠀⣼⣿⣿⣯⣟⣶⡀⡾⠃⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠒⠃⢧⣀⡘⠛⣋⣴⠇⠀⠘⢯⡈⠻⢟⡻⠿⣇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⢉⣩⠽⠋⠀⠀⠀⢈⡿⠭⡍⠀⠀⠘⡇⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⢸⠃⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢦⡬⠷⣤⣀⠀⠀⠀⠀⠀⢠⡞⣁⠀⠀⠀⢸⣷⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⡇⠈⠉⠙⡆⠀⢠⠟⠖⠿⢷⡀⠀⣠⢿⡀⢸⠋⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⡇⠀⠀⠀⡇⠀⡞⠀⠀⢀⣠⣍⣩⣅⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⠏⠀⠀⠀⡇⠀⠀⠀⠀⠰⠇⢀⣴⣛⣡⣏⣱⣏⡇⠁⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠒⠛⣻⠟⠉⣱⠏⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠘⢧⣀⠀⣀⡼⠁⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢀⣠⡴⠞⠛⠉⠀⠀⠀⠀⢰⠏⠀⠀⠁⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠭⠭⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣀⣤⠾⠟⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠲⢤⡀⠀⠈⠙⡆⠀⠀⠀⠀⠀⠀⠀\n⡾⠛⣁⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣷⣄⠀⠀⠀⠀⠀⠀\n⠚⠛⠉⠉⠉⠙⠛⠶⢦⣀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⢤⣀⣀⠀⢀⣀⣤⢷⠶⠚⠋⠁⠹⡗⢦⣄⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠹⣄⠀⡴⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠉⠉⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣆⠆⠀⠀⠙⢦⣙⣣⢇⠤⡄⠀⠀⠀⠀⠀⠀⠀⠈⠉⣁⠀⠀⠀⢀⡼⣣⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣆"
  )

turn = 0
p1Points = 0
p2Points = 0

global gameNumbers
gameNumbers = 0

global game_status
game_status = 0

def update_game_status(is_game_runing):
  global game_status
  game_status = is_game_runing
  print(game_status)

def check_game_status():
  global game_status
  return  game_status

def generate_numbers():
  numbers = []
  global gameNumbers
  while len(numbers) < 5:
    number = random.randint(20000, 30000)
    if number % 2 == 0 and number % 3 == 0 and number % 4 == 0:
      numbers.append(number)
  gameNumbers = numbers   
  return numbers


def result(number):
  global p1Points, p2Points, turn
  if turn == 2:
    if number % 2 == 0:
      p1Points -= 1
      print('spēlētājam -1 punkts, kopā ' + str(p1Points))
      print('-----------------------------------')
      print(p1Points)
      return 0
    else:
      p2Points += 1
      print('datoram +1 punkts, kopā ' + str(p2Points))
      print('-----------------------------------')
      return 0
  else:
    if number % 2 == 0:
      p2Points -= 1
      print('datoram -1 punkts, kopā ' + str(p2Points))
      print('-----------------------------------')
      return 0
    else:
      p1Points += 1
      print('spēlētājam +1 punkts, kopā ' + str(p1Points))
      print('-----------------------------------')
      return 0

#minmax algoritms

def minimax(number, depth, player):
  if depth == 0 or number <= 10:
    return 1  # Default divisor and score if depth is 0 or number is small

  best_divisor = None
  best_score = float('-inf') if player == 1 else float('inf')

  for divisor in [2, 3, 4]:
    if number % divisor == 0:
        new_number = number // divisor
        eval_score = minimax(new_number, depth - 1, 2 if player == 1 else 1)

        if player == 1:
            if eval_score > best_score:
                best_score = eval_score
                best_divisor = divisor
        else:
            if eval_score < best_score:
                best_score = eval_score
                best_divisor = divisor

  return best_divisor if best_divisor is not None else 1

#alfa beta algoritms

def alpha_beta(number, depth, alpha, beta, player):
  if depth == 0 or number <= 10:
    return 2

  last_valid_divisor = None

  if player == 1:
    for divisor in [2, 3, 4]:
      if number % divisor == 0:
        newNumber = number // divisor
        eval = alpha_beta(newNumber, depth - 1, alpha, beta, 2)
        if eval > alpha:
          alpha = eval
          last_valid_divisor = divisor
        if beta <= alpha:
          break
    return last_valid_divisor if last_valid_divisor is not None else alpha
  else:
    for divisor in [2, 3, 4]:
      if number % divisor == 0:
        newNumber = number // divisor
        eval = alpha_beta(newNumber, depth - 1, alpha, beta, 1)
        if eval < beta:
          beta = eval
          last_valid_divisor = divisor
        if beta <= alpha:
          break
    return last_valid_divisor if last_valid_divisor is not None else beta

global number 
number = 0

global machinevsmachine 
machinevsmachine = False

#spēles sākums
def chose_number(value):
  global gameNumbers
  global game_status
  print(gameNumbers)
  print(value)
  print("Game Status:")
  print(game_status)
  
  if(game_status == 0):
    
    if value not in gameNumbers:
      print("skaitlis nav izvelets!")
      #ja izvēlas pareizo skaitli
    
    elif value in gameNumbers:
      print("izvelejos skaitli!")
      global number
      number = value
      
      print('selected number:')
      print(number)
      
      return number
  
  else:
    print("Speles laika nevar mainit sākuma skaitli!!")

global firstGoes 
firstGoes = 1

global algorithm
algorithm = 1

def who_starts(whoStarts):
  global firstGoes
  firstGoes = whoStarts
  print(whoStarts)

def algorithm(whichAlgorithm):
  global algorithm
  algorithm = whichAlgorithm
  print(whichAlgorithm)

def prepare_start():
  global firstGoes

  if firstGoes == '1':
    turn = 1 #Speli sāk Spēlētājs
    
  elif firstGoes == '2':
    turn = 2 #Spēli sāk AI
  
  elif firstGoes == '3':
    machinevsmachine = True
    turn = 1

def print_currentNr():
  global number
  return number    

# Mann vs Machine gamemode
def man_vs_machine(turn,divisor):
  while machinevsmachine == False:
    
    global number
    print(f'Skaitlis: {number}')

    if number <= 10:
      break
    if number % 2 != 0 and number % 3 != 0 and number % 4 != 0:
      print(
          "\n \n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
      )
      print("\n \n WAOW SPELE BEIGUSIES 🪥")
      print('  Skaitlis vairs nedalās ar 2,3 vai 4')
      break

    if turn == 1:
      if divisor in [2, 3, 4] and number % divisor == 0:
        number = number // int(divisor)
        result(number)
        turn = 2
        break
      else:
        print('Nederīgs dalītājs')
    else:
      if algorithm == '1':
        eval = minimax(number, 5, 1)
        if eval == 0:
          print(sad())

        if eval == 2 or eval == 3 or eval == 4:

          print(f'Datora izvēlētais dalītājs: {eval}')
          number = number // eval
          result(number)
          break
        else:
          print(f'spēle beidzas {eval}')
        break

      else:
        eval = alpha_beta(number, 5, float('-inf'), float('inf'), 1)
        if eval == 2 or eval == 3 or eval == 4:
          print('-----------------------------------')
          print(f'Datora izvēlētais dalītājs: {eval}')
          number = number // eval
          result(number)
          break
        else:
          print(f'spēle beidzas {eval}')
          break
        

# Machine vs Machine gamemode

def machine_vs_machine():
  if machinevsmachine == True:
    turn = random.randint(1, 2)

  while machinevsmachine == True:
    print(f'Skaitlis: {number}')

    if number <= 10:
      break
    if number % 2 != 0 and number % 3 != 0 and number % 4 != 0:
      print(
          "\n \n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
      )
      print("\n \n WAOW SPELE BEIGUSIES 🪥")
      print('  Skaitlis vairs nedalās ar 2,3 vai 4')
      break

    if turn == 1:
      if algorithm == '1':
        eval = minimax(number, 2, 1)
        if eval == 0:
          print(sad())

        if eval == 2 or eval == 3 or eval == 4:
          print('-----------------------------------')
          print(f'Datora 1 izvēlētais dalītājs: {eval}')
          number = number // eval
          result(number)
        else:
          print(f'spēle beidzas {eval}')
        turn = 2
      else:
        eval = alpha_beta(number, 2, float('-inf'), float('inf'), 1)
        if eval == 2 or eval == 3 or eval == 4:
          print('-----------------------------------')
          print(f'Datora 1 izvēlētais dalītājs: {eval}')
          number = number // eval
          result(number)
        else:
          print(f'spēle beidzas {eval}')
        turn = 2
    else:
      if algorithm == '1':
        eval = minimax(number, 2, 1)
        if eval == 0:
          print(sad())

        if eval == 2 or eval == 3 or eval == 4:
          print('-----------------------------------')
          print(f'Datora 2 izvēlētais dalītājs: {eval}')
          number = number // eval
          result(number)
        else:
          print(f'spēle beidzas {eval}')
        turn = 1
      else:
        eval = alpha_beta(number, 2, float('-inf'), float('inf'), 1)
        if eval == 2 or eval == 3 or eval == 4:
          print('-----------------------------------')
          print(f'Datora 2 izvēlētais dalītājs: {eval}')
          number = number // eval
          result(number)
        else:
          print(f'spēle beidzas {eval}')
        turn = 1

  if machinevsmachine == False:
    var = {
        p1Points: "Speletajs 1 (Cilveks)",
        p2Points: "Speletajs 2 (Dators)  (Tu zaudēji)"
    }
  else:
    var = {p1Points: "Dators 1", p2Points: "Dators 2"}
  print("\n")
  print('Pirmā spēlētāja punkti: ' + str(p1Points))
  print('Otrā spēlētāja punkti: ' + str(p2Points))
  if p1Points > p2Points and machinevsmachine == False:
    print(happi())
    print("\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
  elif p1Points < p2Points:
    print(sad())
    print("\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
  if p2Points == p1Points:
    print("\nNeizšķirts")
    print("\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
  else:
    print("\n Uzvar:", var.get(max(p2Points, p1Points)))
    print("\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
  if machinevsmachine == True:
    print(botvbot())
    var = {p1Points: "Dators 1)", p2Points: "Dators 2"}
    print(
        "\n \n \n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    )