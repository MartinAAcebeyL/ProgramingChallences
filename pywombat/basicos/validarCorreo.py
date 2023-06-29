correo = input()
if correo.count('@') == 1 and correo[-4:] == '.com':
    print('¡Es válido!')
else:
    print('¡No es válido!')
