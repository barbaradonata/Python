import pygame
import random
import math

# Inicializa o Pygame
pygame.init()

# Constantes
LARGURA = 800
ALTURA = 600
COR_FUNDO = (0, 0, 0)
COR_PACMAN = (255, 255, 0)
COR_PONTOS = (255, 0, 0)
COR_FANTASMA = (0, 0, 255)
TAMANHO_PACMAN = 40
TAMANHO_PONTO = 20
TAMANHO_FANTASMA = 40
NUM_FANTASMAS = 3
VELOCIDADE_FANTASMA = 2

# Configura a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Pac-Man com Fantasmas')

# Função para desenhar o Pac-Man
def desenhar_pacman(x, y):
    pygame.draw.circle(tela, COR_PACMAN, (x, y), TAMANHO_PACMAN // 2)

# Função para desenhar um ponto
def desenhar_ponto(x, y):
    pygame.draw.circle(tela, COR_PONTOS, (x, y), TAMANHO_PONTO // 2)

# Função para desenhar um fantasma
def desenhar_fantasma(x, y):
    pygame.draw.circle(tela, COR_FANTASMA, (x, y), TAMANHO_FANTASMA // 2)

# Função para verificar colisão
def verificar_colisao(x1, y1, x2, y2, tamanho):
    return x1 - tamanho // 2 < x2 < x1 + tamanho // 2 and y1 - tamanho // 2 < y2 < y1 + tamanho // 2

# Função para mover um fantasma na direção do Pac-Man
def mover_fantasma(fantasma, pacman, velocidade):
    x_fantasma, y_fantasma = fantasma
    x_pacman, y_pacman = pacman

    dx = x_pacman - x_fantasma
    dy = y_pacman - y_fantasma
    distancia = math.hypot(dx, dy)
    
    if distancia > 0:
        dx /= distancia
        dy /= distancia
        
    x_fantasma += dx * velocidade
    y_fantasma += dy * velocidade

    # Mantém os fantasmas dentro dos limites da tela
    x_fantasma = max(TAMANHO_FANTASMA // 2, min(x_fantasma, LARGURA - TAMANHO_FANTASMA // 2))
    y_fantasma = max(TAMANHO_FANTASMA // 2, min(y_fantasma, ALTURA - TAMANHO_FANTASMA // 2))

    return (x_fantasma, y_fantasma)

# Função principal do jogo
def jogo():
    x_pacman = LARGURA // 2
    y_pacman = ALTURA // 2
    velocidade = 5

    # Geração inicial de pontos
    pontos = [(random.randint(TAMANHO_PONTO, LARGURA - TAMANHO_PONTO), random.randint(TAMANHO_PONTO, ALTURA - TAMANHO_PONTO)) for _ in range(5)]

    # Geração inicial de fantasmas
    fantasmas = [(random.randint(TAMANHO_FANTASMA, LARGURA - TAMANHO_FANTASMA), random.randint(TAMANHO_FANTASMA, ALTURA - TAMANHO_FANTASMA)) for _ in range(NUM_FANTASMAS)]

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        # Captura das teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            x_pacman -= velocidade
        if teclas[pygame.K_RIGHT]:
            x_pacman += velocidade
        if teclas[pygame.K_UP]:
            y_pacman -= velocidade
        if teclas[pygame.K_DOWN]:
            y_pacman += velocidade

        # Atualiza a posição dos fantasmas
        for i in range(len(fantasmas)):
            fantasmas[i] = mover_fantasma(fantasmas[i], (x_pacman, y_pacman), VELOCIDADE_FANTASMA)

        # Verifica se o Pac-Man comeu um ponto
        pontos = [ponto for ponto in pontos if not verificar_colisao(x_pacman, y_pacman, ponto[0], ponto[1], TAMANHO_PONTO)]

        # Verifica se o Pac-Man colidiu com um fantasma
        for fantasma in fantasmas:
            if verificar_colisao(x_pacman, y_pacman, fantasma[0], fantasma[1], TAMANHO_FANTASMA):
                print("Game Over!")
                pygame.quit()
                return

        # Verifica se o Pac-Man comeu todos os pontos
        if not pontos:
            print("Você Venceu!")
            pygame.quit()
            return

        # Atualiza a tela
        tela.fill(COR_FUNDO)
        desenhar_pacman(x_pacman, y_pacman)

        for ponto in pontos:
            desenhar_ponto(ponto[0], ponto[1])

        for fantasma in fantasmas:
            desenhar_fantasma(fantasma[0], fantasma[1])

        pygame.display.flip()
        pygame.time.delay(30)

if __name__ == "__main__":
    jogo()
