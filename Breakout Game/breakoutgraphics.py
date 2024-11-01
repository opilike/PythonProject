"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Make a breakoutgraphics game (Project)
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # make brick_count as number of bricks
        self.brick_count = int(brick_cols * brick_rows)
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'Orange'
        self.paddle.color = 'Black'
        self.window.add(self.paddle, x=(window_width/2-(paddle_width/2)), y=window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width/2-(ball_radius/2)), y=(window_height/2-(ball_radius/2)))
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        self.__dx = random.randrange(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        self.mouse_click = False
        onmouseclicked(self.ball_bounced)
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                #  change color , total have 5 color and change color after 2 rows !
                if i % 10 == 0 or i % 10 == 1:
                    self.brick.fill_color = 'Red'
                elif i % 10 == 2 or i % 10 == 3:
                    self.brick.fill_color = 'Orange'
                elif i % 10 == 4 or i % 10 == 5:
                    self.brick.fill_color = 'Yellow'
                elif i % 10 == 6 or i % 10 == 7:
                    self.brick.fill_color = 'Green'
                elif i % 10 == 8 or i % 10 == 9:
                    self.brick.fill_color = 'Blue'
                self.window.add(self.brick,
                                x=(brick_spacing*j+brick_width*j), y=(brick_offset+brick_spacing*i+brick_height*i))

    # move paddle function , event be mouse input

    def move_paddle(self, event):
        #  make paddle moveX with mouse x,mouse x pointer middle of paddle
        if event.x <= (self.paddle.width / 2):
            self.paddle.x = 0
        elif event.x >= self.window.width - (self.paddle.width / 2):
            self.paddle.x = (self.window.width - self.paddle.width)
        else:
            self.paddle.x = event.x - (self.paddle.width / 2)
        self.window.add(self.paddle, x=self.paddle.x, y=self.paddle.y)

    def reset_dx(self):
        self.__dx = random.randrange(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
    # Clicked mouse make ball bounced init the ball dx dy

    def ball_bounced(self, event):
        if not self.mouse_click:
            self.reset_dx()
            self.__dy = INITIAL_Y_SPEED
            self.mouse_click = True

    # get_ball_dx function
    def get_ball_dx(self):
        return self.__dx

    # get_ball_dy function
    def get_ball_dy(self):
        return self.__dy

    # detect collision
    def check_for_collision(self):
        #  check 4 conner of ball
        for x in (self.ball.x, self.ball.x + self.ball.width):
            for y in (self.ball.y, self.ball.y + self.ball.height):
                obj = self.window.get_object_at(x, y)
                # if detect collision
                if obj is not None:
                    #  if detect it is paddle!
                    if obj == self.paddle:
                        # reset dx
                        self.reset_dx()
                        return 'paddle'

                    else:
                        #  if detect it is brick
                        self.window.remove(obj)
                        self.brick_count -= 1
                        # reset dx
                        self.reset_dx()
                        return 'brick'
        return None

    # reset ball function and reset ball move dx & dy Reset game!
    def reset_ball_position(self):
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball,
                        x=(self.window.width/2-(self.ball.width/2)), y=(self.window.height/2-(self.ball.height/2)))
        self.mouse_click = False
