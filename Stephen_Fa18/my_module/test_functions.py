import functions as fn


def test_Player():
    test = fn.Player(x = 0, y = 0, width = 5, height = 5, vel = 2)
    assert type(test.x and test.y and test.width and test.height and test.vel) == int
    assert test.left or test.right or test.up or test.down == False