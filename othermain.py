import random
from timeit import default_timer as timer

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


def generate_numbers():
  numbers = []
  while len(numbers) < 5:
    number = random.randint(20000, 30000)
    if number % 2 == 0 and number % 3 == 0 and number % 4 == 0:
      numbers.append(number)
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


#ģenerē spēles ciparus

gameNumbers = generate_numbers()
number = 0
machinevsmachine = False

#spēles sākums

while number not in gameNumbers:
  print(gameNumbers)
  number = int(input('Izvēlieties sākuma skaitli : '))
  #ja izvēlas pareizo skaitli
  if number in gameNumbers:
    break

firstGoes = input(
    'Pirmais ies Lietotājs(1)  vai  Dators(2)  vai  Dators pret Datoru(3)? \n')
algorithm = input('Algoritms: 1 - Minimax, 2 - Alpha-beta pruning: \n')

if firstGoes == '1':
  turn = 1
elif firstGoes == '2':
  turn = 2
elif firstGoes == '3':
  machinevsmachine = True
  turn = 1

# Mann vs Machine gamemode

while machinevsmachine == False:
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
    divisor = int(input('Izvēlieties dalītāju: \n'))
    if divisor in [2, 3, 4] and number % divisor == 0:
      number = number // int(divisor)
      result(number)
      turn = 2
    else:
      print('Nederīgs dalītājs')
  else:
    if algorithm == '1':
      # timeris
      time1 = timer()
      eval = minimax(number, 5, 1)
      print('minmax time taken: ' + str(timer()-time1))
      # timeris end
      if eval == 0:
        print(sad())

      if eval == 2 or eval == 3 or eval == 4:

        print(f'Datora izvēlētais dalītājs: {eval}')
        number = number // eval
        result(number)
      else:
        print(f'spēle beidzas {eval}')
      turn = 1
    else:
      # timeris
      time2 = timer()
      eval = alpha_beta(number, 5, float('-inf'), float('inf'), 1)
      print('alpha beta taken: ' + str(timer()-time2))
      # timeris end
      if eval == 2 or eval == 3 or eval == 4:
        print('-----------------------------------')
        print(f'Datora izvēlētais dalītājs: {eval}')
        number = number // eval
        result(number)
      else:
        print(f'spēle beidzas {eval}')
      turn = 1

# Machine vs Machine gamemode

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
