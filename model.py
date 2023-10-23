import random

def call_model_execution(filepath: str) -> list[dict]:
	"""
	Generate a rand list of diagnostic elements
	"""
 
	numberOfElements = random.randint(2, 10)
	return [
		{
			"x": random.randint(0, 1944),
			"y": random.randint(0, 1944),
		} for _ in range(numberOfElements)
	]
