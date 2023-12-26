import pygame
import sys
import random
import time

# Pygame'ı başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Oyun penceresi oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch The Squirtle")

# Kaplumbağa boyutları
TURTLE_SIZE = 50

# Kaplumbağa başlangıç konumu
turtle_x = random.randint(0, WIDTH - TURTLE_SIZE)
turtle_y = random.randint(0, HEIGHT - TURTLE_SIZE)

# Oyun zamanlayıcıları
hide_time = 1  # Kaplumbağayı gizleme süresi (saniye)
show_time = 2  # Kaplumbağayı gösterme süresi (saniye)
total_game_time = 30  # Toplam oyun süresi (saniye)
start_time = time.time()

score = 0
score_increment = 2  # Her doğru tıklama için kazanılan puan
penalty = 1  # Her yanlış tıklama için kaybedilen puan

# Kaplumbağa resmini yükle
turtle_image = pygame.image.load("squirtle.png")

# Oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Fare tıklamasını kontrol et
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Eğer fare tıklaması kaplumbağanın üzerindeyse, puanı artır
            if turtle_x < mouse_x < turtle_x + TURTLE_SIZE and turtle_y < mouse_y < turtle_y + TURTLE_SIZE:
                score += score_increment
                print("Doğru tıklama! Puan: ", score)
                # Doğru tıklama durumunda uyarı
                pygame.display.set_caption("Catch The Squirtle - Doğru tıklama!")
            else:
                # Yanlış tıklama durumunda puanı azalt
                score -= penalty
                print("Yanlış tıklama! Puan: ", score)
                # Yanlış tıklama durumunda uyarı
                pygame.display.set_caption("Catch The Squirtle - Yanlış tıklama!")

    current_time = time.time()
    elapsed_time = current_time - start_time
    remaining_time = max(0, total_game_time - elapsed_time)

    # Belirli bir süre boyunca kaplumbağayı gizle
    if elapsed_time < hide_time:
        screen.fill(WHITE)
    else:
        # Belirli bir süre boyunca kaplumbağayı göster
        screen.fill(WHITE)
        screen.blit(pygame.transform.scale(turtle_image, (TURTLE_SIZE, TURTLE_SIZE)), (turtle_x, turtle_y))

        # Her 2 saniyede bir kaplumbağanın konumunu rastgele değiştir
        if elapsed_time > hide_time and elapsed_time % show_time < 0.1:
            turtle_x = random.randint(0, WIDTH - TURTLE_SIZE)
            turtle_y = random.randint(0, HEIGHT - TURTLE_SIZE)

    # Skoru ekrana yazdır
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Skor: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Zamanlayıcıyı ekrana yazdır
    timer_text = font.render(f"Kalan Zaman: {int(remaining_time)} saniye", True, BLACK)
    screen.blit(timer_text, (WIDTH // 2 - 100, 10))

    # Toplam oyun süresi bittiğinde oyunu sonlandır
    if elapsed_time >= total_game_time:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
