# 1.0 version
import pyautogui
import time

TEXTO = "Olá chefe, esse é um teste automático com PyAutoGUI!"  
VELOCIDADE = 0.1  
PAUSA_MOUSE = 5   


def main():
    print(f"Você tem {PAUSA_MOUSE} segundos para posicionar o mouse...")
    time.sleep(PAUSA_MOUSE)


    x, y = pyautogui.position()
    print(f"Mouse na posição: ({x}, {y})")


    pyautogui.click(x, y)


    for char in TEXTO:
        pyautogui.typewrite(char)  
        time.sleep(VELOCIDADE)     

if __name__ == "__main__":
    main()
