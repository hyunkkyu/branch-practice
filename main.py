from random import sample
from random import choice
from random import randint

def get_randint() -> list:
	return [randint(1,45) for _ in range(7)]

def get_choice() -> list:
	return [choice(range(1,45+1)) for _ in range(7)]


if __name__=='__main__':
	print(get_randint())
	print(get_choice())
