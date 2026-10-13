import re
import sys


def converter(texto):
    # Cabeçalhos: "# texto", "## texto", "### texto"
    def cabecalho(m):
        n = len(m.group("marcas"))
        return f"<h{n}>{m.group('texto').strip()}</h{n}>"

    texto = re.sub(r"^(?P<marcas>#{1,3})[ \t]+(?P<texto>.+)$", cabecalho, texto, flags=re.M)

    # Bold: **texto**
    texto = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", texto)

    # Itálico: *texto*
    texto = re.sub(r"\*(.+?)\*", r"<i>\1</i>", texto)

    # Imagem: ![texto alternativo](path)  (antes do link, por causa do "!")
    texto = re.sub(r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]*)\)",
                   r'<img src="\g<src>" alt="\g<alt>"/>', texto)

    # Link: [texto](url)
    texto = re.sub(r"\[(?P<txt>[^\]]*)\]\((?P<url>[^)]*)\)",
                   r'<a href="\g<url>">\g<txt></a>', texto)

    # Lista numerada: blocos de linhas "1. item"
    def lista(m):
        itens = re.findall(r"^\d+\.[ \t]+(.*)$", m.group(0), flags=re.M)
        return "<ol>\n" + "\n".join(f"<li>{i.strip()}</li>" for i in itens) + "\n</ol>"

    texto = re.sub(r"(?:^\d+\.[ \t]+.*(?:\n|$))+", lambda m: lista(m) + "\n", texto, flags=re.M)

    return texto


if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else "entrada.md"
    destino = sys.argv[2] if len(sys.argv) > 2 else "saida.html"

    with open(entrada, encoding="utf-8") as f:
        html = converter(f.read())

    with open(destino, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Gerado {destino}")
