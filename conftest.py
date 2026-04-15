import ast
# backward-compat for older code that expects old AST node names
if not hasattr(ast, "NameConstant") and hasattr(ast, "Constant"):
    class NameConstant(ast.Constant):
        pass
    ast.NameConstant = NameConstant
if not hasattr(ast, "Str") and hasattr(ast, "Constant"):
    class Str(ast.Constant):
        pass
    ast.Str = Str
if not hasattr(ast, "Num") and hasattr(ast, "Constant"):
    class Num(ast.Constant):
        pass
    ast.Num = Num
# add more aliases if pytest tracebacks ask for them (Bytes, Ellipsis, etc.)
