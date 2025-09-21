from machine import Pin
import time

# Configuração dos pinos do encoder
CLK_PIN = 25
DT_PIN = 26
SW_PIN = 27

POSICAO_ALVO = 10  # Altere para a posição desejada

def main():
    clk = Pin(CLK_PIN, Pin.IN, Pin.PULL_UP)
    dt = Pin(DT_PIN, Pin.IN, Pin.PULL_UP)
    sw = Pin(SW_PIN, Pin.IN, Pin.PULL_UP)

    posicao = 0
    clk_ant = clk.value()

    while True:
        clk_atual = clk.value()

        # Detecta mudança no CLK
        if clk_atual != clk_ant:
            # Determina a direção do giro
            if dt.value() != clk_atual:
                posicao += 1
            else:
                posicao -= 1
            print("Posição atual:", posicao)

            # Verifica se atingiu a posição alvo
            if posicao == POSICAO_ALVO:
                print("Posição alvo atingida!")

        clk_ant = clk_atual

        # Detecta pressionamento do botão
        if sw.value() == 0:
            print("Botão do encoder pressionado!")
            time.sleep(0.3)  # debounce simples

        time.sleep(0.001)  # pequeno delay para estabilidade

# Executa a função principal
if __name__ == "__main__":
    main()

