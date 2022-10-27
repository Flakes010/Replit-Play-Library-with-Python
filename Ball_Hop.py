import play


balls = []

@play.when_mouse_clicked
def make_ball():
    for ball in balls:
        if play.mouse.is_touching(ball):
            return
    ball = play.new_circle(color=play.random_color(),
                           x=play.mouse.x, y=play.mouse.y, radius=20)
    ball.start_physics(bounciness=0.5, mass=100, friction=1)
    ball.is_being_dragged = False
    
    @ball.when_clicked
    def click_ball():
        ball.is_being_dragged = True
        ball.color = play.random_color()
        
    @play.mouse.when_click_released
    def release_ball():
        for ball in balls:
            ball.is_being_dragged = False
    balls.append(ball)
    
@play.when_key_pressed('z')
def press_key(key):
    for ball in balls:
        ball.physics.y_speed = play.random_number(80, 100)
        ball.physics.x_speed = play.random_number(-30, 30)
        
@play.repeat_forever 
def loop():
    for ball in balls:
        if ball.is_being_dragged:
            ball.physics.x_speed = play.mouse.x - ball.x
            ball.physics.y_speed = play.mouse.y - ball.y
            
            
play.start_program()
