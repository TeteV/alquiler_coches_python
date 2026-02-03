import sys
from pathlib import Path

# Agregar el directorio actual al path para que Python encuentre el módulo
sys.path.insert(0, str(Path(__file__).parent))

from alquiler_coches.presentation.menu import main

if __name__ == "__main__":
    main()
