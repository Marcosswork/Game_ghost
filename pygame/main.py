# pygame:
# pip install pygame

# 1. IMPORT -------------------------------
import pygame
import random

from ghost import Ghost
from bat import Bat
from shoot import Shoot

# 2. INICIALIZAÇÃO ------------------------

# 2.1 Iniciar o pygame
pygame.init()

# 2.2 Iniciar a janela com a configuração de resolução de 840x480

# 2.2.1 Costantes de largura e altura da tela
WIDTH_SCREEN = 840  # LARGURA
HEIGHT_SCREEN = 480  # ALTURA

# 2.2.2 Criar a janela
display = pygame.display.set_mode([WIDTH_SCREEN, HEIGHT_SCREEN])

# 2.2.3 Preencher o fundo da janela com rgb
display.fill([5, 95, 240])

# 2.2.4 Mudar o titulo da janela
pygame.display.set_caption("Game Ghost - Python")


# 2.2.5 Caregar img para criar o icone
icone = pygame.image.load("data/icone.png")
pygame.display.set_icon(icone)

# 3. ELEMENTOS DE TELA --------------------

# 3.1 PERSONAGENS

# Criar um grupo de imgs para caregar todos os elementos(img) e desenhar em uma unica vez
objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

# Criar um cenário (backgrooud) para o fantasma
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image, [840,480])
bg.rect = bg.image.get_rect()

# Criar um obj Sprite para manipular a img - fantasma
ghost = Ghost(objectGroup)

# 3.2 FONTES ------------------------------
score_font = pygame.font.Font("font/Pixeltype.ttf", 50)
gameOver_font = pygame.font.Font("font/Pixeltype.ttf", 200)

# 3.3 MUSICA -------------------------------
pygame.mixer.music.load("data/alienblues.wav")
pygame.mixer.music.play(-1)

# 3.4 SOM (SFX) -------------------------------
attack = pygame.mixer.Sound("data/magic1.wav")

# 4. VARIAVEIS GLOBAIS --------------------
gameloop = True
gameOver = False

timer = 20
pontos = 0

# 4.1 criar um clock para ajustar os frames pos segundo (fps)
clock = pygame.time.Clock()

# 5. FUNÇÃO PRINCIPAL ---------------------


def main():
    global gameloop
    global gameOver
    global timer
    global pontos

    # Criar o game loop
    while gameloop:

        # clock para 60fps
        clock.tick(120)

        # verificação dos eventos posiveis
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    newShoot = Shoot(objectGroup, shootGroup)
                    newShoot.rect.center = ghost.rect.center
                    attack.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                newShoot = Shoot(objectGroup, shootGroup)
                newShoot.rect.center = ghost.rect.center
                attack.play()

        if not gameOver:

            #cor de fundo da janela
            display.fill([5, 95, 240])

            # criar os inquilinos(morcegos)
            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newBat = Bat(objectGroup, batGroup)

            #colisão dos morcegos com o fantasma
            colisao = pygame.sprite.spritecollide(ghost, batGroup, False, pygame.sprite.collide_mask)
            if colisao:
                print("GAME OVER")
                gameOver = True

            # Colisão do tiro com o morcego
            tiros = pygame.sprite.groupcollide(shootGroup, batGroup, True, True, pygame.sprite.collide_mask)

            #contagem de abates
            if tiros:
                pontos += 1
                print("SCORE:", pontos)

            objectGroup.update()

        

        # desenhando os elementos dos grupos na janela
        objectGroup.draw(display)

        #inserindo a pontuação na tela
        score_render = score_font.render(f'Score: {pontos}', False, 'white')
        display.blit(score_render, (650, 50))

        # inserindo o game over na tela
        if gameOver:
            gameOverMs = gameOver_font.render('GAME OVER', False, 'white')
            display.blit(gameOverMs, (100,150))

        # atualização de tela
        pygame.display.update()


if __name__ == "__main__":
    main()
