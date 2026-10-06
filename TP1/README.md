# TPC1: Strings Binárias sem "011"

## Autor
- <img width="176" height="180" alt="image" src="https://github.com/user-attachments/assets/3819922b-6d5a-4bd9-a2a2-3a591171f460" />
- **Nome:** João Afonso Peixoto Pinheiro
- **ID:** A100089

---

# O objetivo deste trabalho prático consistiu na especificação de uma expressão regular capaz de identificar e aceitar cadeias binárias que não contenham a sequência `"011"`.
A expressão desenvolvida foi:
`^1*(0+1)*0*$`

# Explicação:
- Colocamos ^ para garantir que a validação começa no início
- Podemos ou nao ter no inicio vários ou nenhum 1 logo 1*
- Podemos de seguida ter 0's porém depois desses 0's só podemos ter exclusivamente um 1, podemos ter isso quantas vezes quisermos logo (0+1)*
- No final podemos ou nao ter 0's logo 0*
- Colocamos $ para garantir que a validação vai ate ao ultimo dígito
  
## Lista de resultados
**Exemplos dados pelo professor na aula verificados a olho e verificados no regex**
  
- `011011` -> Rejeitada (contém "011")
- `101111` -> Rejeitada (contém "011")
- `1101`   -> Aceite (válida)
- `101010` -> Aceite (válida)

<img width="800" height="391" alt="image" src="https://github.com/user-attachments/assets/f9cd6d02-a3b7-4124-9d2c-fa9b484edade" />

* [README.md](README.md) - Manifesto e especificação da expressão regular
