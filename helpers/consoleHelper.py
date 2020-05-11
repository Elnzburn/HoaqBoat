from common.constants import bcolors
from objects import glob

def printServerStartHeader(asciiArt=True):
	"""
	Print server start message

	:param asciiArt: print BanchoBoat ascii art. Default: True
	:return:
	"""
	if asciiArt:
		print("{}   __                 _ _                 ".format(bcolors.PINK))
		print("  / / _   _ _ __ ___ (_) | ___  _   _ ___ ")
		print(" / / | | | | '_ ` _ \| | |/ _ \| | | / __|")
		print("/ /__| |_| | | | | | | | | (_) | |_| \__ ")
		print("\____/\__,_|_| |_| |_|_|_|\___/ \__,_|___/{}".format(bcolors.ENDC))

	printColored("> Welcome to HoaqBoat osu!bancho server v{}".format(glob.VERSION), bcolors.PINK)
	printColored("> Made by the Ripple team, custom by osu!lumilous", bcolors.GREEN)
	printColored("> {}https://zxq.co/ripple/pep.py".format(bcolors.UNDERLINE), bcolors.PINK)
	printColored("> Press CTRL+C to exit\n", bcolors.PINK)

def printNoNl(string):
	"""
	Print a string without \n at the end

	:param string: string to print
	:return:
	"""
	print(string, end="")

def printColored(string, color):
	"""
	Print a colored string

	:param string: string to print
	:param color: ANSI color code
	:return:
	"""
	print("{}{}{}".format(color, string, bcolors.ENDC))

def printError():
	"""
	Print a red "Error"

	:return:
	"""
	printColored("Error", bcolors.RED)

def printDone():
	"""
	Print a green "Done"

	:return:
	"""
	printColored("Done", bcolors.GREEN)

def printWarning():
	"""
	Print a yellow "Warning"

	:return:
	"""
	printColored("Warning", bcolors.YELLOW)
