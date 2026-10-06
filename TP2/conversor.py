import sys

def converter(linhas):
    saida = []
    em_lista = False

    for linha in linhas:
        linha = linha.rstrip("\n")
        # item de lista ordenada: "1. texto"
        partes = linha.strip().split(". ", 1)
        eh_item = len(partes) == 2 and partes[0].isdigit()

        if eh_item:
            if not em_lista:
                saida.append("<ol>")
                em_lista = True
            saida.append(f"  <li>{partes[1].strip()}</li>")
        else:
            if em_lista:
                saida.append("</ol>")
                em_lista = False
            if linha.strip():
                saida.append(f"<p>{linha.strip()}</p>")

    if em_lista:
        saida.append("</ol>")

    return "\n".join(saida)

if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else "entrada.xtml"
    destino = sys.argv[2] if len(sys.argv) > 2 else "saida.html"

    with open(entrada, encoding="utf-8") as f:
        html = converter(f.readlines())

    with open(destino, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Gerado {destino}")