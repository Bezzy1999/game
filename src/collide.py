
def check(ball, level, paddle):
    ballRect = ball.rect

    for block in level:
        if collides(ballRect, block):
            respond_to_collision(ball, block)
            break

    if collides(ballRect, paddle.rect):
        respond_to_collision(ball, paddle.rect)


def collides(rect1, rect2):
    if rect1.x > (rect2.x + rect2.width): return False
    if rect2.x > (rect1.x + rect1.width): return False
    if rect1.y > (rect2.y + rect2.height): return False
    if (rect1.y + rect1.height) < rect2.y: return False

    return True

def respond_to_collision(ball, rect):
    ball.rect.x = ball.rect.x - ball.speed[0]
    ball.rect.y = ball.rect.y - ball.speed[1]

    diff_x = (ball.rect.x + (ball.rect.width / 2)) - \
             (rect.x + (rect.width / 2))

    diff_y = (ball.rect.y + (ball.rect.height / 2)) - \
             (rect.y + (rect.height / 2))

    if abs(diff_y) > abs(diff_x):
        ball.speed[1] = -ball.speed[1]
    else:
        ball.speed[0] = -ball.speed[0]
