import pygame as py
import environment as env
import player
from config import screen, FPS, clock, BACKGROUND, update_offsets, font, WIDTH, HEIGHT
from event import EVENT
import Graph

# === Setup ===
agents = 7
graph = Graph.Graph()
city = env.City()
cars = []
tree = env.Trees()

for _ in range(agents):
    cars.append(player.Car(500, 670, graph.points, AI=False if _ == 0 else True, place=_))

score = 0
running = True


# === Game Loop ===
while running:
    screen.fill(BACKGROUND)

    # === Update ===
    update_offsets()
    graph.update()
    tree.update()
    city.update()


    # === Draw ===
    for car in cars:
        car.update(cars)

    # ============== HUD & Display ==============
    text = font.render(f"FPS: {int(clock.get_fps())}", True, (220, 220, 220))
    screen.blit(text, (10, 10))
    py.display.flip()
    clock.tick(FPS)
    running = EVENT(py.event.get())


