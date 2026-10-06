# TP2 - Conversor de XTML para HTML (listas ordenadas)

**Autor:** João Pinheiro (Axxxxx)
**UC:** Processamento de Linguagens e Compiladores (PLC2026)

## Descrição

Pequeno conversor que lê um ficheiro de texto (`.xtml`) e gera um ficheiro HTML.
Neste trabalho trata-se apenas de **listas ordenadas**: linhas no formato
`1. texto` são convertidas em `<ol><li>texto</li></ol>`. As restantes linhas
não vazias são convertidas em parágrafos `<p>`.

## Ficheiros

- `conversor.py` - programa que faz a conversão.
- `entrada.xtml` - exemplo de ficheiro de entrada.
- `saida.html` - resultado da conversão do exemplo.

## Como usar

```
python conversor.py [entrada] [saida]
```

Por omissão lê `entrada.xtml` e escreve `saida.html`.

## Exemplo

Entrada:

```
Os meus passos:
1. Acordar
2. Estudar
3. Dormir
```

Saída:

```html
<p>Os meus passos:</p>
<ol>
  <li>Acordar</li>
  <li>Estudar</li>
  <li>Dormir</li>
</ol>
```
