import ast, importlib, pprint
importlib.reload(ast)
print('ast module:', ast)
print('ast.__file__:', getattr(ast, '__file__', None))
print('has Str:', hasattr(ast, 'Str'))
print('has Constant:', hasattr(ast, 'Constant'))
print('some names:', [n for n in dir(ast) if n in ('Str','Constant','Num','Name','In','Compare')])
pprint.pprint({n: type(getattr(ast, n)) for n in ('Str','Constant') if hasattr(ast, n)})