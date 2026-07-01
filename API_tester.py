from File_API import File_manipulator
from Internet_API import internet_parser
from Inpu_Manip_API import inpu_manipulator
import time

obje = File_manipulator("tester.txt")
parser = internet_parser("https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch")
parser.open_site()
time.sleep(2)
obje.create_file()
inp = inpu_manipulator(parser.parse_site_text())

obje.append_to_file(inp.str_space_remover())

parser.close_tab()

parser.set_link("https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch")
parser.open_site()
time.sleep(2)
inp = inpu_manipulator(parser.parse_site_text())

obje.append_to_file(inp.str_space_remover())

parser.close_tab()