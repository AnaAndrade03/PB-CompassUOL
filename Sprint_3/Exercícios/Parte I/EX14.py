def parametros(*args, **kwargs):
    for arg in args:
        print(arg)
    for item in kwargs.values():
        print(item)

parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)