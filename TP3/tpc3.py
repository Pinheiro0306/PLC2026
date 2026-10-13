import ply.lex as lex

tokens = (
    "VAR", "LANG", "STRING", "NUMBER", "CONCEPT", "LIMIT",
    "LBRACE", "RBRACE", "DOT",
)

def t_comentario(t):
    r"\#.*"
    pass

def t_VAR(t):
    r"\?[A-Za-z0-9]+"
    return t

def t_LANG(t):
    r"@[A-Za-z]{2}"
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_CONCEPT(t):
    r"[A-Za-z_][A-Za-z0-9_]*(:[A-Za-z0-9_]+)?"
    if t.value == "LIMIT":
        t.type = "LIMIT"
    return t

t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_DOT = r"\."
t_ignore = " \t\r"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Linha {t.lexer.lineno}: carater ilegal {t.value[0]!r}")
    t.lexer.skip(1)

lexer = lex.lex()

## Para fazer Teste

data = '''# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
'''

lexer.input(data)
for tok in lexer:
    print(f"{tok.lineno:>3}  {tok.type:<8} {tok.value!r}")