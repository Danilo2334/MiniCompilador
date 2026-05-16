# MiniCompilador de Impuestos (ANTLR4 + Python)

## Instalación

Desde `MiniCompilador/`:

```bash
pip install -r requirements.txt
```

## Generación del parser/lexer (ANTLR4)

```bash
antlr4 -Dlanguage=Python3 -visitor gramatica.g4 -o generated
```

## Ejecución

1. Coloca tu programa fuente en `input.txt`
2. Ejecuta:

```bash
python main.py
```

Se generarán:

- `output.txt` (logs + TAC)
- `output_program.py` (Python ejecutable)

