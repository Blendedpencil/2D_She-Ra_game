import turtle as trtl
import time as tm
import random as rand
wn = trtl.Screen()
wn.bgcolor("purple")
#turtle setup
background_drawer = trtl.Turtle()
background_drawer.hideturtle()
background_drawer.speed(0)
drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()
character_drawer = trtl.Turtle()
character_drawer.penup()
character_drawer.hideturtle()
special_attack_a = 0
special_attack_duration = 10
normal_attack_duration = 2
aura_drawer = trtl.Turtle()
aura_drawer.speed(0)
aura_drawer.hideturtle()
aura_drawer.penup()
aura_drawer2 = trtl.Turtle()
aura_drawer2.speed(0)
aura_drawer2.hideturtle()
aura_drawer2.penup()
aura_drawer2.fillcolor('yellow')


#globals
xc = 0
yc = -300
times_moved = 0
character_pose = "standing"
faceing = "right"
jumping = 0
jump_height = 100
top_ground_color = "light green"
under_ground_color = "light green"
land = "village"
sa_distance_traveled = 0
normal_attack = 0
normal_attack_duration_c = 0
special_attack_duration_c = 0
stop_game = 0
cutscene = 0
transformation_ongoing = 0
c_mode = "adora"
can_transform = 0
can_do_normal_attack = 0
phase = 1
s_attack_in_prog = 0
s_attack_duration = 0
spider_x_displ = 0
spider_y_displ = 0
energy_ball_displ = 0
player_health = 100
enemy_health = 400
victory = 0
sparkles_in_prog = 0
xca = 0
yca = 0

def draw_sky(sky_color):
 background_drawer.penup()
 background_drawer.fillcolor(sky_color)
 background_drawer.goto(-1400,-1000)
 background_drawer.begin_fill()
 background_drawer.goto(-1400, 1000)
 background_drawer.goto(1400, 1000)
 background_drawer.goto(1400, -1000)
 background_drawer.end_fill()

def draw_ground(top_groundc, under_groundc):
 global yc
 background_drawer.pendown()
 background_drawer.fillcolor(under_groundc)
 background_drawer.pencolor(top_groundc)
 background_drawer.pensize(20)
 background_drawer.goto(-1400,yc)
 background_drawer.begin_fill()
 background_drawer.goto(-1400, yc-100)
 background_drawer.goto(1400, yc-100)
 background_drawer.goto(1400, yc)
 background_drawer.end_fill()
 background_drawer.penup()

def jump():
  global jumping
  if jumping == 0:
    jumping = 1

def move_left():
 global xca,yca, xc, yc, times_moved,character_pose, faceing, jumping, cutscene, land, stop_game
 if cutscene == 0:
  faceing = "left"
  times_moved+=.5
  if xc < 50 and land == "village":
    xc+=40
  elif xc < -7500:
    xc+= 40
  if (character_pose == "standing" or jumping == 1 or jumping == 2) and stop_game == 0:
    draw_character(0,-300,"yes", "left", "mid")
    character_pose = "walking"
  elif stop_game == 0:
    draw_character(0,-300,"no", "left", "mid")
    character_pose = "standing"
  
def move_right():
 global xc,yc, times_moved,character_pose, faceing, jumping, cutscene, stop_game
 if cutscene == 0:
  faceing = "right"
  times_moved+=.5
  if xc > -9000:
    xc-=40
  if (character_pose == "standing" or jumping == 1 or jumping == 2) and stop_game == 0:
    draw_character(0,-300,"yes", "right", "mid")
    character_pose = "walking"
  elif stop_game == 0:
    draw_character(0,-300,"no", "right", "mid")
    character_pose = "standing"
#game parts
 
def draw_house(x,y):
 drawer.fillcolor("brown")
 drawer.goto(x,y)
 drawer.begin_fill()
 drawer.goto(x,y)
 drawer.goto(x+400,y)
 drawer.goto(x+400,y+200)
 drawer.goto(x,y+200)
 drawer.end_fill()
 drawer.fillcolor("yellow")
 drawer.begin_fill()
 drawer.goto(x+400,y+200)
 drawer.goto(x+400,y+300)
 drawer.goto(x,y+300)
 drawer.end_fill()
 
def draw_hut(x,y):
 drawer.goto(x,y)
 drawer.fillcolor("brown")
 drawer.begin_fill()
 drawer.setheading(90)
 drawer.circle(200,180)
 drawer.end_fill()
 drawer.fillcolor("blue")
 drawer.goto(x-180, y)
 drawer.begin_fill()
 drawer.goto(x-180,y+100)
 drawer.goto(x-220, y+100)
 drawer.goto(x-220, y)
 drawer.end_fill()

def draw_villager_house(x,y):
 drawer.goto(x,y)
 drawer.fillcolor("brown")
 drawer.goto(x,y)
 drawer.begin_fill()
 drawer.goto(x,y)
 drawer.goto(x+400,y)
 drawer.goto(x+400,y+200)
 drawer.goto(x,y+200)
 drawer.end_fill()
 drawer.fillcolor("yellow")
 drawer.begin_fill()
 drawer.goto(x+400,y+200)
 drawer.goto(x+400,y+300)
 drawer.goto(x,y+300)
 drawer.end_fill()
 drawer.fillcolor("green")
 drawer.goto(x+180, y)
 drawer.begin_fill()
 drawer.goto(x+180,y+100)
 drawer.goto(x+220, y+100)
 drawer.goto(x+220, y)
 drawer.end_fill()

def draw_tower(x,y):
 drawer.goto(x,y)
 drawer.fillcolor("brown")
 drawer.goto(x,y)
 drawer.begin_fill()
 drawer.goto(x,y)
 drawer.goto(x+400,y)
 drawer.goto(x+400,y+800)
 drawer.goto(x,y+800)
 drawer.end_fill()
 drawer.fillcolor("yellow")
 drawer.begin_fill()
 drawer.goto(x+400,y+800)
 drawer.goto(x+400,y+1000)
 drawer.goto(x,y+800)
 drawer.end_fill()
 drawer.fillcolor("black")
 drawer.goto(x+180, y)
 drawer.begin_fill()
 drawer.goto(x+180,y+100)
 drawer.goto(x+220, y+100)
 drawer.goto(x+220, y)
 drawer.end_fill()
  
def draw_tree(x,y):
  drawer.goto(x,y+10)
  drawer.color("brown")
  drawer.pendown()
  drawer.pensize(20)
  drawer.setheading(90)
  drawer.forward(40)
  drawer.setheading(50)
  drawer.pensize(16)
  drawer.forward(80)
  drawer.forward(-80)
  drawer.setheading(90)
  drawer.forward(120)
  drawer.turtlesize(8)
  drawer.shape("circle")
  drawer.color("green")
  drawer.stamp()
  drawer.penup()

def draw_cloud(x,y,cloud_height,ccolor):
 drawer.goto(x,y)
 I = 1
 drawer.color(ccolor)
 drawer.shape("circle")
 drawer.turtlesize(3)
 while(cloud_height > I):
  cloud_width = cloud_height
  clouddx = drawer.xcor()
  clouddy = drawer.ycor()
  while(cloud_width>0):
   drawer.turtlesize(4)
   drawer.stamp()
   drawer.setheading(0)
   drawer.forward(30)
   cloud_width-=1
  drawer.goto(clouddx,clouddy)
  cloud_width = cloud_height - 1
  while(cloud_width>0):
   drawer.turtlesize(3)
   drawer.stamp()
   drawer.setheading(180)
   drawer.forward(20)
   cloud_width-=1
  drawer.goto(clouddx,clouddy)
  drawer.setheading(90)
  drawer.forward(20)
  cloud_height -= 1

def draw_mountains(size,x,y):
  drawer.goto(x,y)
  drawer.shape("triangle")
  drawer.color("grey")
  drawer.turtlesize(size)
  drawer.setheading(90)
  drawer.stamp()

def draw_first_ones_temple(x,y):
 drawer.goto(x,y)
 drawer.fillcolor("dark blue")
 drawer.pencolor("purple")
 drawer.pendown()
 drawer.setheading(0)
 drawer.begin_fill()
 drawer.forward(800)
 drawer.setheading(120)
 drawer.forward(800)
 drawer.setheading(90)
 drawer.forward(800)
 drawer.setheading(130)
 drawer.forward(80)
 drawer.setheading(30) 
 drawer.forward(-80)
 drawer.setheading(90)
 drawer.forward(-400)
 drawer.setheading(60)
 drawer.forward(-400)
 drawer.goto(x,y)
 drawer.end_fill()
 drawer.penup()

def draw_door(x,y):
  drawer.penup()
  drawer.fillcolor("black")
  drawer.goto(x+40,y+200)
  drawer.begin_fill()
  drawer.goto(x+40,y)
  drawer.goto(x-40, y)
  drawer.goto(x-40, y + 200)
  drawer.end_fill()
  drawer.penup()
  drawer.goto(x,y+200)
  drawer.color("dark blue")
  drawer.turtlesize(4)
  drawer.setheading(-90)
  drawer.shape("arrow")
  drawer.stamp()
  drawer.setheading(90)
  drawer.goto(x+60,y)
  drawer.stamp()
  drawer.goto(x-60, y)
  drawer.stamp()

#temple interior

def draw_chamber(x,y):
  drawer.goto(x,y)
  drawer.pendown()
  drawer.pencolor("purple")
  drawer.pensize(30)
  drawer.fillcolor("blue")
  drawer.begin_fill()
  drawer.goto(x, y+1000)
  drawer.goto(x+2000, y+1000)
  drawer.goto(x+2000, y)
  drawer.end_fill()
  drawer.penup()
  drawer.goto(x,y+1000)
  drawer.pendown()
  x = 0
  while(x<20):
    drawer.setheading(0)
    drawer.forward(100)
    drawer.setheading(-90)
    drawer.forward(1000)
    drawer.forward(-1000)
    x+= 1
  drawer.penup()

#draw the sword

def draw_sword(x,y):
  
  #sword of protection
  drawer.pensize(1)
  drawer.pencolor("black")
  drawer.goto(x,y+100)
  drawer.pendown()
  drawer.fillcolor("light blue")
  drawer.begin_fill()
  drawer.setheading(90)
  drawer.forward(-100)
  drawer.setheading(45)
  drawer.forward(20)
  drawer.setheading(90)
  drawer.forward(90)
  drawer.end_fill()
  drawer.penup()
  drawer.begin_fill()
  drawer.goto(x,y+100)
  drawer.pendown()
  drawer.goto(x,y)
  drawer.setheading(135)
  drawer.forward(20)
  drawer.setheading(90)
  drawer.forward(90)
  drawer.end_fill()
  drawer.penup()
  drawer.goto(x,y+120)
  drawer.shape('arrow')
  drawer.setheading(-90)
  drawer.turtlesize(3)
  drawer.color("gold")
  drawer.stamp()
  drawer.pencolor('gold')
  drawer.pensize(10)
  drawer.pendown()
  drawer.goto(x,y+150)
  drawer.penup()
  drawer.turtlesize(1)
  drawer.color("gold")
  drawer.shape("arrow")
  drawer.setheading(0)
  drawer.goto(x+10,y+100)
  drawer.stamp()
  drawer.setheading(180)
  drawer.goto(x-10, y+100)
  drawer.stamp()
  drawer.goto(x,y+110)
  drawer.turtlesize(1)
  drawer.shape("circle")
  drawer.color("dark blue")
  drawer.stamp()

#projectiles

def draw_energy_ball(x,y,e_ball_color1, e_ball_color2,e_ball_color3,shape1,shape2,shape3,size1,size2,size3):
 drawer.goto(x,y)
 drawer.shape(shape1)
 drawer.color(e_ball_color1)
 drawer.turtlesize(size1)
 drawer.setheading(rand.randint(0,359))
 drawer.stamp()
 drawer.setheading(rand.randint(0,359))
 drawer.stamp()
 drawer.color(e_ball_color2)
 drawer.shape(shape2)
 drawer.turtlesize(size2)
 drawer.stamp()
 drawer.shape(shape3)
 drawer.color(e_ball_color3)
 drawer.turtlesize(size3)
 drawer.setheading(rand.randint(0,359))
 drawer.stamp()

def aura (ray_len, aura_flash, heading):
 colors = ["yellow", "orange", "red", "pink", "purple", "blue", "green"]
 color_tracker = 1
 #aura_drawer.fillcolor(colors(0))
 aura_drawer.goto(0,-217)
 aura_drawer2.goto(0,-217)
 total_heading = heading + 391
 wn.tracer(True)
 wn.tracer(False)
 tm.sleep(.1)
 aura_drawer.clear()
 aura_drawer2.clear()
 aura_drawer.pendown()
 aura_drawer.pencolor("white")
 aura_drawer.pensize(3)
 while(heading < total_heading):
  color_tracker += 1
  if color_tracker == 7:
    color_tracker = 0
  aura_drawer.setheading(heading)
  aura_drawer.forward(ray_len)
  aura_drawer.end_fill()
  aura_drawer.forward(-ray_len)
  aura_drawer.setheading(heading+20)
  aura_drawer.forward(ray_len)
  #drawer.forward(-200)
  aura_drawer.end_fill()
  aura_drawer.fillcolor(colors[color_tracker])
  aura_drawer.begin_fill()
  aura_drawer.forward(-ray_len)
  heading += 30
  #second flash
  heading2 = -heading
  aura_drawer2.setheading(heading2)
  aura_drawer2.forward(ray_len-100)
  aura_drawer2.end_fill()
  aura_drawer2.forward(-ray_len+100)
  aura_drawer2.setheading(heading+20)
  aura_drawer2.forward(ray_len-100)
  #drawer.forward(-200)
  aura_drawer2.end_fill()
  aura_drawer2.begin_fill()
  aura_drawer2.forward(-ray_len+100)
 aura_drawer.penup()
 #flash
 aura_drawer.shape("circle")
 aura_drawer.color("white")
 if aura_flash > 0:
  aura_drawer.turtlesize(3**aura_flash)
  aura_drawer.stamp()

#spider

def spider_enemy(spider_rush,x,y):
 drawer.goto(x,y)
 #body main
 drawer.fillcolor("black")
 drawer.penup()
 drawer.begin_fill()
 drawer.setheading(0)
 drawer.forward(100)
 drawer.goto(x,y+200)
 drawer.goto(x-100,y)
 drawer.end_fill()
 
 #left leg 

 incrementor = 0
 leg_angle = 0
 while incrementor < 3:
  if spider_rush == 1:
   leg_angle = rand.randint(1,50)
  drawer.goto(x-60+leg_angle,y+100-leg_angle)
  drawer.begin_fill()
  drawer.goto(x-90-leg_angle,y-50+leg_angle)
  drawer.goto(x-120+leg_angle,y+100+leg_angle)
  drawer.end_fill()
  incrementor += 1  

 #right leg

 incrementor = 0
 while incrementor < 3:
  if spider_rush == 1:
   leg_angle = rand.randint(1,50)
  drawer.goto(x+60-leg_angle,y+100-leg_angle)
  drawer.begin_fill() 
  drawer.goto(x+90+leg_angle,y-50+leg_angle)
  drawer.goto(x+120-leg_angle,y+100+leg_angle)
  drawer.end_fill()
  incrementor += 1 

#words

def screen_words(y, words, font_size):
    drawer.goto(0,y)
    drawer.write(words, align="center", font=(font_size))

#controles

def end_game():
  global stop_game, victory
  wn.tracer(False)
  stop_game = 1
  drawer.clear()
  character_drawer.clear()
  background_drawer.clear()
  drawer.color("white")
  if victory == 0:
    wn.bgcolor("black")
    screen_words(0,"Game Over", 100)
  if victory == 1:
    wn.bgcolor("purple")
    screen_words(0, "Thanks For Playing!", 100)
  stop_game = 1
  wn.tracer(True)
  wn.tracer(False)

  
def s_special_attack():
  global special_attack_a
  special_attack_a = 1

def s_normal_attack():
  global normal_attack, can_do_normal_attack
  if can_do_normal_attack == 1:
   normal_attack = 1

def dash():
  global faceing, sparkles_in_prog, xc, yc
  if faceing == "right" and -7000 > xc > -9000:
    xc -= 400
  elif -7000 > xc > -9000:
    xc += 400
  sparkles_in_prog = 10

#sparkles from teleporting
def sparkles(xc,yc,v):
  for i in range (1,v):
    drawer.goto(rand.randint(xc-30,xc+30), rand.randint(yc-250,yc-100))
    drawer.shape("turtle")
    drawer.color("pink")
    drawer.turtlesize(1)
    drawer.setheading(rand.randint(1,360))
    drawer.stamp()
    drawer.color("white")
    drawer.setheading(rand.randint(1,360))
    drawer.stamp()
    
 
def special_attack(x,y,mult,heading):
 drawer.goto(x,y)
 drawer.fillcolor("yellow")
 drawer.begin_fill()
 drawer.setheading(heading)
 drawer.circle(mult*100,160)
 drawer.setheading(heading)
 drawer.circle(mult*-110,170)
 drawer.end_fill()
 
def transform():
 global cutscene, transformation_ongoing, c_mode, can_transform, can_do_normal_attack
 if c_mode == "adora" and can_transform == 1:
  cutscene = 1
  transformation_ongoing = 1
  can_do_normal_attack = 1

def player_health_bar():
  global player_health
  drawer.fillcolor("red")
  drawer.goto(-200, 300)
  drawer.begin_fill()
  drawer.goto(-100, 300)
  drawer.goto(-100, 280)
  drawer.goto(-200, 280)
  drawer.end_fill()

  drawer.fillcolor("green")
  drawer.begin_fill()
  drawer.goto(-200, 300)
  drawer.goto(-200+player_health, 300)
  drawer.goto(-200+player_health, 280)
  drawer.goto(-200, 280)
  drawer.end_fill()

def enemy_health_bar():
  drawer.fillcolor("red")
  drawer.goto(-200,350)
  drawer.begin_fill()
  drawer.goto(-200+enemy_health, 350)
  drawer.goto(-200+enemy_health, 360)
  drawer.goto(-200,360)
  drawer.end_fill()

#start screen
wn.tracer(False)
drawer.goto(0,-100)
drawer.turtlesize(10)
drawer.write("Press s to start \n left arrow to move left \n right arrow to move right \n up arrow to jump \n z to teleport(once in dungeon) \n x to swing sword(once you get one) \n e to exit while game is running \n I suggest playing in full screen mode", align = "center", font = 10)
draw_sword(0,50)
wn.tracer(True)
wn.tracer(False)
#drawer.clear()

def start_game():
 global xc,yc,character_pose, faceing, jumping, jump_height, top_ground_color, under_ground_color, land, special_attack_a, normal_attack, sa_distance_traveled, special_attack_duration, normal_attack_duration, special_attack_duration_c, normal_attack_duration_c, stop_game, transformation_ongoing, c_mode, cutscene, can_transform, phase, s_attack_in_prog, s_attack_duration, spider_x_displ, spider_y_displ, energy_ball_displ, player_health, sparkles_in_prog, victory, enemy_health
 stop_game == 0
 while(stop_game == 0):
   tm.sleep(.05)
   aura_flash = 0
   ray_len = 1000
   heading = 0
   while transformation_ongoing == 1:
    heading+=1
    ray_len = heading * 20
    if heading > 40:
     aura_flash += 1
    aura(ray_len, aura_flash, heading)
    if heading > 50:
     transformation_ongoing = 0
     c_mode = "she_ra"
     cutscene = 0
     aura_drawer.clear()
     aura_drawer2.clear()

   wn.tracer(False)
   drawer.penup()
   drawer.hideturtle()
   drawer.clear()
   background_drawer.clear()
   if jump_height == 0:
    jumping = 2
   if jumping == 2 and jump_height > 99:
    jumping = 0
   if jumping == 1 and jump_height > 0:
    yc -= jump_height
    jump_height -= 10
   if jumping == 2 and jump_height < 100:
    jump_height += 10
    yc += jump_height
   if xc < -4000:
    can_transform = 1
    transform()
   if xc<-7200:
    land = "inside_temple"
   else:
    land = "village"
   if land == "village":
    cloud_color = "pink"
    c1n = 8
    c2n = 10
    sun_s = "circle"
    sun_c = "white"
    sky_c = "purple"

    if xc > -5000:
     cloud_color = "white"
     c1n = 4
     c2n = 5
     sky_c = "sky blue"
     sun_s = "circle"
     sun_c = "orange"

    draw_sky(sky_c)
    draw_energy_ball(300,300, sun_c, sun_c, sun_c,sun_s, sun_s, sun_s,3,3,3)
    draw_mountains(20,-200,-300)
    draw_mountains(30,-400,-300)
    draw_cloud(50,100,c1n,cloud_color)
    draw_cloud(-200,130,c2n,cloud_color)
    draw_first_ones_temple(xc+7000, yc)
    if xc <= -6900:
      draw_door(xc+7300, yc)
    draw_ground(top_ground_color, under_ground_color)
    if xc<=500 and xc>-1000:
      draw_house(xc-50,yc)
    draw_villager_house(xc+400,yc)
    draw_villager_house(xc+1000,yc)
    draw_villager_house(xc+1600,yc)
    draw_villager_house(xc+1900,yc)
    draw_villager_house(xc+2500,yc)
    draw_hut(xc+4000,yc)
    if can_transform == 0:
      draw_sword(xc+4000,yc)
    v = 4300
    while v<6000:
      draw_tree(xc + v, yc)
      v+=100
    v = 4300
    while v<6000:
      draw_tree(xc + v, yc)
      v += 450
    v = 4300
    while v < 6000:
      v += 221
      draw_tree(xc+v, yc)
   else:
    draw_chamber(xc+7200, yc)
    #resets
    if s_attack_in_prog == 0:
      s_attack = rand.randint(0,3)
      if xc+8000+spider_x_displ > 0:
        r = 0
      if xc+8000+spider_x_displ < 0:
        r = 1
      v = rand.randint(0,1)
      s_attack_in_prog = 1
    #rush
    if s_attack == 1 or s_attack == 0:
      spider_enemy(1,xc+8000+spider_x_displ, yc+40+spider_y_displ)
      s_attack_duration+=1
      if r == 1 and spider_x_displ < 1000:
       spider_x_displ += 10
      elif r==1:
        r = 0
      if r == 0 and spider_x_displ > -1000:
        spider_x_displ -= 10
      elif r==0:
        r = 1
      if s_attack_duration > 30:
        s_attack_duration = 0
        s_attack_in_prog = 0
    #jump attack
    if s_attack == 2:
      s_attack_duration+=1
      if r == 1 and spider_x_displ < 1000:
        spider_x_displ += 5
      elif r==1:
        r = 0
      if r == 0 and spider_x_displ > -1000:
        spider_x_displ -= 5
      elif r == 0:
        r = 1
      if s_attack_duration > 32:
        spider_y_displ -= 20
      elif s_attack_duration < 3:
        spider_y_displ -= 20
      else:
        spider_y_displ+=20
      if s_attack_duration > 59:
        s_attack_duration = 0
        s_attack_in_prog = 0
      spider_enemy(0,xc+8000+spider_x_displ, yc+50+spider_y_displ)
    #fireball
    if s_attack == 3:
      s_attack_duration+=1
      spider_enemy(0,xc+8000+spider_x_displ, yc+50+spider_y_displ)
      draw_energy_ball(xc+8000+spider_x_displ+energy_ball_displ,yc+50+spider_y_displ,"red","red","red","turtle","turtle","turtle",3,3,3)
      if r == 1:
        energy_ball_displ += 20
      if r == 0:
        energy_ball_displ -= 20
      if s_attack_duration > 30:
        s_attack_duration = 0
        s_attack_in_prog = 0
        energy_ball_displ = 0
    #sparkles from dashing
    if sparkles_in_prog > 0:
      sparkles_in_prog-=1
      if sparkles_in_prog == 9:
        s_placex = -xc
        s_placey = -yc
      sparkles(s_placex+xc, s_placey+yc, sparkles_in_prog)
        
    #health
    #energy ball health check
    if xc+8000+spider_x_displ+energy_ball_displ >= -10 and xc+8000+spider_x_displ+energy_ball_displ <= 10 and s_attack == 3 and jumping == 0:
      if r == 0:
        xc += 160
      else:
        xc -= 160
      player_health -= 10
    #base hit health check
    if xc+8000+spider_x_displ >= -80 and xc+8000+spider_x_displ <= 80 and jumping == 0 and s_attack != 2:  # I had energy ball displacement added to both of these
      if r == 0:
        xc += 160
      else:
        xc -= 160
      player_health -= 10
    enemy_health_bar()
    player_health_bar()
    if player_health < 10:
      end_game()
    if enemy_health < 20:
      victory = 1
      end_game()

   if (normal_attack == 1 and faceing == "right"):
    special_attack(20,-300,1,0)
    if(xc+8000+spider_x_displ >= -200 and xc+8000+spider_x_displ <= 200 and r == 0):
      enemy_health-=5
      #sparkles(200,100,9)
   if (normal_attack == 1 and faceing == "left"):
     special_attack(-20,-300,-1,180)
     if(xc+8000+spider_x_displ >= -200 and xc+8000+spider_x_displ <= 200 and r == 1):
      enemy_health-=5
      #sparkles(200,100,9)


   if (normal_attack == 1):
     normal_attack_duration_c += 1
     if(normal_attack_duration_c > normal_attack_duration):
       normal_attack_duration_c = 0
       normal_attack = 0
   if character_pose == "standing":
     if faceing == "right":
       draw_character(0,-300,"no", "right", "mid")
     if faceing == "left":
       draw_character(0,-300,"no", "left", "mid")
   if character_pose == "walking":
     if faceing == "right":
       draw_character(0,-300,"yes", "right", "mid")
     if faceing == "left":
       draw_character(0,-300,"yes", "left", "mid")
   drawer.goto(xc,yc)
   wn.tracer(True)
 
def draw_character(x,y,leg_forward,direction, extension):
 global c_mode
 wn.tracer(False)
 character_drawer.clear()
 if c_mode == "she_ra":
  clothes_color = "white"
 else:
  clothes_color = "black"
 if leg_forward == "yes":
   character_drawer.goto(x+10,y)
   character_drawer.fillcolor(clothes_color)
   character_drawer.begin_fill()
   character_drawer.goto(x,y+50)
   character_drawer.goto(x+10, y+50)
   character_drawer.goto(x+20, y)
   character_drawer.end_fill()
   character_drawer.goto(x-10,y)
   character_drawer.fillcolor(clothes_color)
   character_drawer.begin_fill()
   character_drawer.goto(x,y+50)
   character_drawer.goto(x-10, y+50)
   character_drawer.goto(x-20, y)
   character_drawer.end_fill()
 else:
   character_drawer.goto(x+5,y)
   character_drawer.fillcolor(clothes_color)
   character_drawer.begin_fill()
   character_drawer.goto(x+5,y+50)
   character_drawer.goto(x-5, y+50)
   character_drawer.goto(x-5, y)
   character_drawer.end_fill()
 character_drawer.goto(x+10,y+50)
 character_drawer.begin_fill()
 character_drawer.goto(x+10,y+100)
 character_drawer.goto(x-10,y+100)
 character_drawer.goto(x-10,y+50)
 character_drawer.end_fill()

 #skirt

 if c_mode == "she_ra":
  character_drawer.goto(x,y+50)
  character_drawer.turtlesize(2)
  character_drawer.color("white")
  character_drawer.shape("arrow")
  character_drawer.setheading(90)
  character_drawer.stamp()

 #head

 character_drawer.goto(x,y+110)
 character_drawer.shape("circle")
 character_drawer.color("orange")
 character_drawer.turtlesize(2)
 character_drawer.stamp()
 if direction == "right":
   character_drawer.goto(x+3,y+110)
 else:
   character_drawer.goto(x-3,y+110)
 character_drawer.turtlesize(2)
 character_drawer.shape("arrow")
 character_drawer.setheading(90)
 character_drawer.stamp()

 #arms

 character_drawer.fillcolor("orange")
 character_drawer.goto(x,y+100)
 character_drawer.shape("circle")
 character_drawer.turtlesize(.5)
 if direction == "right":
   character_drawer.begin_fill()
   character_drawer.goto(x-3, y+90)
   character_drawer.goto(x-9, y+78)
   character_drawer.goto(x+25, y+70)
   character_drawer.goto(x+25, y+75)
   character_drawer.goto(x-4, y+79)
   character_drawer.goto(x+3, y+75)
   character_drawer.end_fill()
 else:
   character_drawer.begin_fill()
   character_drawer.goto(x+3, y+90)
   character_drawer.goto(x+9, y+78)
   character_drawer.goto(x-25, y+70)
   character_drawer.goto(x-25, y+75)
   character_drawer.goto(x+4, y+79)
   character_drawer.goto(x-3, y+75)
   character_drawer.end_fill()
 
wn.tracer(True)
wn.onkeypress(move_right,"Right")
wn.onkeypress(move_left,"Left")
wn.onkeypress(jump, "Up")
wn.onkeypress(start_game, "s")
wn.onkeypress(s_normal_attack, "x")
wn.onkeypress(end_game, "e")
wn.onkeypress(dash, "z")
wn.listen()
#wn.exitonclick()
wn.mainloop()
