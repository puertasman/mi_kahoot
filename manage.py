
#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kahoot_django_game.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'No se puede importar Django. ¿Está instalado y disponible en tu entorno?'
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
