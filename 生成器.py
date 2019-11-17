def power(values):
	for value in values:
		print("powering %s"%value)
		yield value

def adder(values):
	for value in values:
		print("adding to %s"%value)
		if value%2==0:
			yield value+3
		else:
			yield value+2

elements=[1,4,7,9,12,19]
results=adder(power(elements))


def psychologist():
	print("please tell me your problems")
	while True:
		answer=(yield)
		if answer is not None:
			if answer.endswith("?"):
				print("Don't ask yourself too many questions")
			elif "good" in answer:
				print("Ahh that's good,go on")
			elif "bad" in answer:
				print("Don't be so negative")

free=psychologist()
print(next(free))
free.send("I feel bad")
free.send("why I shouldn't ?")
free.send("ok the i should find what is good for me")












