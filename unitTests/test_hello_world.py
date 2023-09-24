from useCase import hello_world

def test_say_hello():
    assert hello_world.say_hello() == "Hello World"