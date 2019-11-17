import tokenize
reader=open("迭代器.py").readline
tokens=tokenize.generate_tokens(reader)
print(next(tokens))
print(next(tokens))
print(next(tokens))
print(next(tokens))