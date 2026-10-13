# Resolução do TPC3 - Analisador Léxico

- <img width="176" height="180" alt="image" src="https://github.com/user-attachments/assets/3819922b-6d5a-4bd9-a2a2-3a591171f460" />
- **Nome:** João Afonso Peixoto Pinheiro
- **ID:** A100089

## Descrição

Pequeno analisador léxico em Python para uma linguagem de query, feito com o módulo `lex` da biblioteca `ply`. Este programa identifica e processa os diferentes tokens da linguagem definida:

| Elemento | Texto (Exemplo) | Token (PLY) |
| :--- | :--- | :--- |
| Comentário | `# DBPedia: obras de Chuck Berry` | Ignorado (`t_ignore`) |
| Variável | `?nome`, `?desc` | `VAR` |
| Língua | `@en` | `LANG` |
| String | `"Chuck Berry"` | `STRING` |
| Conceito | `select`, `where`, `dbo`, `foaf` | `CONCEPT` |
| Delimitador | `{`, `}`, `.` | `DELIMITER` |
| Palavra Reservada | `LIMIT` | `LIMIT` |
| Número | `1000` | `NUMBER` |
| Dois Pontos | `:` | `COLON` |

## Ficheiros

*   `tpc3.py` - programa que faz a análise léxica (contém o texto de teste embebido).

## Como usar

```bash
python tpc3.py
