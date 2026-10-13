# TPC2 - Conversor de MarkDown para HTML

- <img width="176" height="180" alt="image" src="https://github.com/user-attachments/assets/3819922b-6d5a-4bd9-a2a2-3a591171f460" />
- **Nome:** João Afonso Peixoto Pinheiro
- **ID:** A100089

## Descrição

Pequeno conversor em Python de MarkDown para HTML, feito com expressões
regulares (`re`), para os elementos da "Basic Syntax" da Cheat Sheet:

| Elemento | MarkDown | HTML |
|---|---|---|
| Cabeçalhos | `# texto`, `## texto`, `### texto` | `<h1>`, `<h2>`, `<h3>` |
| Bold | `**texto**` | `<b>texto</b>` |
| Itálico | `*texto*` | `<i>texto</i>` |
| Lista numerada | `1. item` | `<ol><li>item</li></ol>` |
| Link | `[texto](url)` | `<a href="url">texto</a>` |
| Imagem | `![alt](path)` | `<img src="path" alt="alt"/>` |

## Ficheiros

- `conversor.py` - programa que faz a conversão.
- `entrada.md` - exemplo de ficheiro de entrada.
- `saida.html` - resultado da conversão do exemplo.

## Como usar

```
python conversor.py [entrada] [saida]
```

Por omissão lê `entrada.md` e escreve `saida.html`.
