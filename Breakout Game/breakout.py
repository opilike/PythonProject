"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    vx = 0
    vy = 0
    life = NUM_LIVES
    # Add the animation loop here!
    while True:
        if graphics.mouse_click and life > 0:
            while True:
                # if restart the game
                if vx == 0 and vy == 0:
                    vx = graphics.get_ball_dx()
                    vy = graphics.get_ball_dy()
                graphics.ball.move(vx, vy)
                #  bounce from window (not include bottom of window)
                if graphics.ball.y <= 0:
                    vy = -vy
                if graphics.ball.x <= 0 or (graphics.ball.x + graphics.ball.width) >= graphics.window.width:
                    vx = -vx

                #  check collision
                collision = graphics.check_for_collision()  # make collision be graphics.check_for_collision()
                if collision:
                    if collision == 'paddle':
                        #  check ball dy is down then change if no didn't change vy
                        if vy >= 0:
                            vy = -vy
                    elif collision == 'brick':
                        vy = -vy
                    vx = graphics.get_ball_dx()  # update dx
                pause(FRAME_RATE)
                #  check still have bricks or not if no have print "you win"
                if graphics.brick_count == 0:
                    print('You won the game !')
                    return
                #  check is ball outside bottom of window
                if (graphics.ball.y + graphics.ball.height) >= graphics.window.height:
                    break
            graphics.reset_ball_position()
            vx, vy = 0, 0
            life -= 1
        #  if life <= 0 print you lose
        if life <= 0:
            print('You lose the game !')
            return
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
