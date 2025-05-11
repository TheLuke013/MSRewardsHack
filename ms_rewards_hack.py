import subprocess
import time
import random
import string
import pyautogui
from pynput.keyboard import Controller  

prefixes = [
    "a", "ab", "abs", "ad", "ante", "bene", "circum", "circun", "co", "com",
    "con", "contra", "de", "des", "dis", "di", "e", "ex", "extra", "in",
    "im", "i", "inter", "intra", "juxta", "mal", "malé", "multi", "non", "ob",
    "oc", "of", "per", "pós", "post", "pre", "prae", "pro", "re", "retro",
    "semi", "sub", "sob", "su", "super", "sobre", "trans", "tra", "tres", "ultra",
    "an", "ana", "anti", "apo", "cata", "cat", "dia", "dís", "en", "em",
    "epi", "eu", "hemi", "hiper", "hipo", "meta", "mono", "neo", "pan", "para",
    "perí", "poli", "proto", "pseudo", "sin", "sim", "si", "taqui", "tele", "xeno",
    "auto", "bi", "bis", "tri", "tetra", "hexa", "deca", "duo", "eco", "eletro",
    "foto", "geo", "hidro", "ideo", "info", "linguo", "micro", "macro", "necro", "orto",
    "psico", "quimi", "radio", "socio", "tecno", "termo", "turbo", "uni", "video", "zoo"
]

suffixes = [
    "aço", "ada", "agem", "alho", "alho", "alho", "amento", "ância", "ante", "ar",
    "ário", "ás", "ável", "eira", "eiro", "ência", "ente", "ento", "esco", "ez",
    "eza", "ice", "ício", "ico", "ido", "iente", "il", "ilho", "im", "ina",
    "inho", "io", "ismo", "ista", "ita", "iz", "ização", "izar", "mente", "nte",
    "oso", "oso", "ota", "ote", "ou", "oura", "oz", "são", "sse", "sso",
    "tão", "tivo", "tor", "triz", "uço", "uda", "udo", "ulento", "ura", "us",
    "uto", "ável", "ível", "ível", "eável", "ável", "douro", "dura", "sório", "sor",
    "ário", "ório", "al", "ar", "il", "oso", "ento", "iço", "ento", "ura",
    "ista", "eiro", "ado", "ido", "ido", "alha", "elho", "ona", "eco", "enta",
    "iço", "ucho", "udo", "uinho", "zão", "zito", "oca", "ento", "inhado", "ínho"
]

def search():
    random_search = generate_random_word()
    print(f"Random Search: {random_search}")
    
    keyboard = Controller()

    keyboard.type(random_search)
    time.sleep(1)
    pyautogui.press('enter')

def generate_random_word():
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    middle = ''.join(random.choices(string.ascii_lowercase, k=random.randint(0, 3)))
    return prefix + middle + suffix

def main():
    print("Opening MS Edge")
    msedge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" #caminho para o microsoft edge
    
    process = subprocess.Popen([msedge_path], shell=True) #abre o processo do microsoft edge
    
    time.sleep(10) #aguarda 10 seg até que o edge seja completamento aberto
    
    #faz 30 pesquisas aleatorias para alcançar 90 pontos no total
    for i in range(30):
        print("Searching..")
        pyautogui.hotkey('ctrl', 'l') #foca na barra de pesquisa
        search()
        time.sleep(5)

if __name__ == "__main__":
    main()
