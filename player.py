import pygame as py
import config as cfg
import math
import random as rn
import neuralNetwork as NN

def normalize(x):
    return round(x/60, 2)

def check_collision(start_pos, end_pos, obj):
    
    # Ensure the object has a mask and position
    if not hasattr(obj, 'mask') or not hasattr(obj, 'rotated_rect'):
        return False
    
    obj_mask = obj.mask
    obj_pos = obj.rotated_rect.topleft  # Top-left corner of the object's bounding box

    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    line_length = math.sqrt(dx**2 + dy**2)
    num_points = max(10, int(line_length))  
    
   
    for i in range(0, num_points + 1, 5):
        t = i / num_points
        x = start_pos[0] + t * dx
        y = start_pos[1] + t * dy
        

        mask_x = int(x - obj_pos[0])
        mask_y = int(y - obj_pos[1])
        
        if (0 <= mask_x < obj_mask.get_size()[0] and 
            0 <= mask_y < obj_mask.get_size()[1]):
            if obj_mask.get_at((mask_x, mask_y)):
                return True
    
    return False

class Car:
    def __init__(self, x=cfg.WIDTH/2, y=cfg.HEIGHT/2, gp=[], color=cfg.GREEN, op=256, AI=False, place=-1):
        self.AI = AI
        self.color = color
        self.score = 0
        self.speed = 0
        self.max_speed = 1.5 if not AI else rn.uniform(1, 2)
        self.acceleration = 0.03
        self.angle = 0
        self.rotation_speed = 1
        self.width = 17
        self.height = 27
        self.running = False
        self.direction = 1
        self.follow_player = False  # Camera follow toggle
        self.delay = 0
        self.auto_mode = True  # Automatic movement enabled by default
        self.gp = gp

        self.car_image = py.image.load(f'cars/car{rn.randint(1, 4)}.png').convert_alpha()
        self.car_image = py.transform.scale(self.car_image, (self.width, self.height))
        self.car_image.set_alpha(op)

        self.leftside = 0
        self.rightside = 0
        self.rotated_rect = None
        self.mask = None

        self.pathway = [p.get() for p in gp]
        self.path_index = 0 if not self.AI else rn.randint(1, len(self.pathway) - 2)
        self.x = self.pathway[self.path_index][0]
        self.y = self.pathway[self.path_index][1]

        # For the neural network
        self.displacement = (0, 0)
        self.neuralInformation = [0, 0, 0, 0]
        self.inputs = [0, 0]
        self.reward = 0
        self.actions = [0, 0, 0, 0]
        self.distance = 0
        self.normalizedAngle = [0, 0]
        self.sensor_angle = 0
        self.place_angle = 0
        self.start_pos = ()
        self.end_pos = ()

        self.countdown = 30

        self.draw()

    def draw(self):
        #py.draw.circle(cfg.screen, cfg.RED, (self.pathway[self.path_index][0] + cfg.ofx, self.pathway[self.path_index][1] + cfg.ofy), 3)
        #py.draw.line(cfg.screen, cfg.RED, (self.neuralInformation[0], self.neuralInformation[1]), (self.neuralInformation[2], self.neuralInformation[3]))

        rotated_surface = py.transform.rotate(self.car_image, -self.angle)
        self.rotated_rect = rotated_surface.get_rect(center=(self.x + cfg.ofx, self.y + cfg.ofy))
        cfg.screen.blit(rotated_surface, self.rotated_rect.topleft)
        self.mask = py.mask.from_surface(rotated_surface)

        # Sensor
        sensor_length = 65 
        self.start_pos = (self.x + cfg.ofx, self.y + cfg.ofy)
        
        total_angle = -self.angle + 90 
        end_x = self.start_pos[0] + sensor_length * math.cos(math.radians(total_angle))
        end_y = self.start_pos[1] - sensor_length * math.sin(math.radians(total_angle))  
        self.end_pos = (end_x, end_y)
        
        
        #py.draw.line(cfg.screen, cfg.BLUE, self.start_pos, self.end_pos, 3)

    def update(self, other):
        keys = cfg.KEYS()
        
        if self.countdown > 0:
            self.countdown -= 1
            self.rotation_speed = 10
        else:
            self.rotation_speed = 1.5

        if keys[py.K_c] and not self.AI:  # Toggle camera follow with 'c' key
            if self.delay <= 0:
                self.follow_player = not self.follow_player
                self.delay = 20

        if keys[py.K_m]:  # Toggle auto mode with 'm' key
            if self.delay <= 0:
                self.auto_mode = not self.auto_mode
                self.delay = 20

        if self.delay > 0:
            self.delay -= 1
        
        tx = self.x + cfg.ofx if not self.follow_player else cfg.WIDTH / 2
        ty = self.y + cfg.ofy if not self.follow_player else cfg.HEIGHT / 2

        # Calculate the angle to the destination point
        dest_x = self.pathway[self.path_index][0] + cfg.ofx
        dest_y = self.pathway[self.path_index][1] + cfg.ofy
        dx = dest_x - (self.x + cfg.ofx)
        dy = dest_y - (self.y + cfg.ofy)
        
        # Compute the destination angle using atan2 (in degrees)
        self.place_angle = math.degrees(math.atan2(dy, dx)) + 90
        # Update displacement and neural information
        if self.follow_player and not self.AI:
            self.displacement = (self.x - self.pathway[self.path_index][0], self.y - self.pathway[self.path_index][1])
            self.neuralInformation[0] = cfg.WIDTH/2
            self.neuralInformation[1] = cfg.HEIGHT/2
            self.neuralInformation[2] = self.pathway[self.path_index][0] + cfg.ofx
            self.neuralInformation[3] = self.pathway[self.path_index][1] + cfg.ofy
            
            if abs(self.displacement[0]) < 40 and abs(self.displacement[1]) < 40:
                self.reward += 10
                self.path_index += 1
                self.path_index %= len(self.pathway)
        else:
            self.displacement = (tx - (self.pathway[self.path_index][0] + cfg.ofx), ty - (self.pathway[self.path_index][1] + cfg.ofy))
            self.neuralInformation[0] = tx
            self.neuralInformation[1] = ty
            self.neuralInformation[2] = self.pathway[self.path_index][0] + cfg.ofx
            self.neuralInformation[3] = self.pathway[self.path_index][1] + cfg.ofy
            
            if abs(self.displacement[0]) < 40 and abs(self.displacement[1]) < 40:
                self.reward += 10
                self.path_index += 1
                self.path_index %= len(self.pathway)

        self.inputs = [normalize(self.neuralInformation[0] - self.neuralInformation[2]), normalize(self.neuralInformation[1] - self.neuralInformation[3])]
        self.distance = math.sqrt(self.inputs[0] ** 2 + self.inputs[1] ** 2)
        self.normalizedAngle = [math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle))]

        if abs(self.inputs[0]) > 5 or abs(self.inputs[1]) > 5:
            self.reward -= 0.1
        
        if self.direction == -1:
            self.reward -= 1

        # Movement logic
        if self.auto_mode:
            # Directly set the car's angle to face the destination
            if self.angle > self.place_angle:
                self.angle -= self.rotation_speed * self.direction
            if self.angle < self.place_angle:
                self.angle += self.rotation_speed * self.direction
            
            if abs(self.angle - self.place_angle) > 300:
                self.angle = self.place_angle
            # Move forward automatically
            self.running = True
            self.direction = 1
            self.score += 0.1 * self.direction
        else:
            # Manual control
            if self.running:
                if keys[py.K_a]:
                    self.angle -= self.rotation_speed * self.direction
                if keys[py.K_d]:
                    self.angle += self.rotation_speed * self.direction
            
            if keys[py.K_w]:
                self.running = True
                self.direction = 1
                self.score += 0.1 * self.direction
            elif keys[py.K_s]:
                self.running = True
                self.direction = -1
                self.score += 0.1 * self.direction
            else:
                self.running = False
        for car in other:
            if car != self:
                if check_collision(self.start_pos, self.end_pos, car):
                    self.running = False
                    break

        # Update speed
        if self.running:
            self.speed += self.acceleration
        else:
            self.speed -= self.acceleration

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0

        # Update position
        angle_radians = math.radians(self.angle)
        self.x += self.speed * math.sin(angle_radians) * self.direction
        self.y -= self.speed * math.cos(angle_radians) * self.direction

        # Pass car position to config for camera following
        if not self.AI:
            cfg.update_car_position(self.x, self.y, self.follow_player)

        self.draw()
        return self.running