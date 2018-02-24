import math 


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

def dist_between_points(x1, y1, x2, y2):
    dist = x1 - x2
    dist2 = y1 - y2
    dist *= dist
    dist2 *= dist2

    return dist + dist2

def collideBallVsRect(ballPos, radius, rect):
    rect_centreX = rect.x + (rect.width / 2)
    rect_centreY = rect.y + (rect.height / 2)

    distx = math.fabs(ballPos.x - rect_centreX)
    disty = math.fabs(ballPos.y - rect_centreY)

    if distx > ((rect.width / 2) + radius): return False
    if disty > ((rect.height / 2) + radius): return False

    if distx <= (rect.width / 2): return True
    if disty <= (rect.height / 2): return True

    dist_sq = math.pow(distx - (rect.width / 2), 2) + \
                math.pow(disty - (rect.height / 2), 2)

    return dist_sq <= (radius * radius)

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
