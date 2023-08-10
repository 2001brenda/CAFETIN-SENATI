def input_int(mensaje, mensaje_error):
    while True:
        try:
            v = int(input(mensaje))
        except ValueError:
            print(mensaje_error)
        else:
            return v
        # break
    
