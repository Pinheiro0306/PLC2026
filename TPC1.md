### TPC1
# Expressão regular para apanhar Strings Binárias que nao contenham a substring "011"
`^1*(0+1)*0*$`

Explicação:
Colocamos ^ para garantir que a validação começa no início
Podemos ou nao ter no inicio vários ou nenhum 1 logo 1*
Podemos de seguida ter 0's porém depois desses 0's só podemos ter exclusivamente um 1, podemos ter isso quantas vezes quisermos logo (0+1)*
No final podemos ou nao ter 0's logo 0*
Colocamos $ para garantir que a validação vai ate ao ultimo dígito

# Exemplos de Teste:
- `011011` -> Rejeitada (contém "011")
- `101111` -> Rejeitada (contém "011")
- `1101`   -> Aceite (válida)
- `101010` -> Aceite (válida)
