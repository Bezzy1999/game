import collide

class rect(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class rect_with_speed(rect):
    def __init__(self, pos, speed):
        self.rect = rect(pos.x, pos.y, pos.width, pos.height)
        self.speed = speed

def test_collides_rect1_leftof_rect2_not_touching():
    rect1 = rect(2, 2, 4, 4)
    rect2 = rect(7, 2, 4, 4)

    assert not collide.collides(rect1, rect2)

def test_collides_rect1_righttof_rect2_not_touching():
    rect1 = rect(7, 2, 4, 4)
    rect2 = rect(2, 2, 4, 4)

    assert not collide.collides(rect1, rect2)

def test_collides_rect1_above_rect2_not_touching():
    rect1 = rect(2, 2, 6, 4)
    rect2 = rect(3, 7, 7, 4)

    assert not collide.collides(rect1, rect2)

def test_collides_rect1_below_rect2_not_touching():
    rect1 = rect(2, 12, 6, 4)
    rect2 = rect(3, 7, 7, 4)

    assert not collide.collides(rect1, rect2)

def test_collides_rect1_leftof_rect2_touching():
    rect1 = rect(2, 3, 6, 4)
    rect2 = rect(7, 3, 7, 4)

    assert collide.collides(rect1, rect2)

def test_collides_rect1_rightof_rect2_touching():
    rect1 = rect(7, 3, 6, 4)
    rect2 = rect(3, 3, 4, 4)

    assert collide.collides(rect1, rect2)

def test_collides_rect1_above_rect2_touching():
    rect1 = rect(2, 2, 6, 4)
    rect2 = rect(3, 6, 7, 4)

    assert collide.collides(rect1, rect2)

def test_collides_rect1_below_rect2_touching():
    rect1 = rect(2, 11, 6, 4)
    rect2 = rect(3, 7, 7, 4)

    assert collide.collides(rect1, rect2)

def test_respond_to_collision_bounce_above_left_to_right():
    rect1 = rect(2, 2, 4, 4)
    ball = rect_with_speed(rect1, [2, 2])
    rect2 = rect(2, 5, 6, 4)

    collide.respond_to_collision(ball, rect2)
    assert ball.speed == [2, -2]

def test_respond_to_collision_bounce_below_left_to_right():
    rect1 = rect(2, 8, 4, 4)
    ball = rect_with_speed(rect1, [2, -2])
    rect2 = rect(2, 2, 6, 2)

    collide.respond_to_collision(ball, rect2)
    assert ball.speed == [2, 2]
