from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter,
)

texto = open("Preguntas_frecuentes_FAQ.md").read()
 
# Fixed-size
fixed = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks_fixed = fixed.split_text(texto)
 

# Recursive (recomendado por defecto)
recursive = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""],
)
chunks_rec = recursive.split_text(texto)
 

# Document-aware para Markdown
md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")]
)
chunks_md = md_splitter.split_text(texto)


chunks = [("fixed", chunks_fixed), ("rec", chunks_rec), ("md", chunks_md)]
for name, c in chunks:
    longitud_media = sum(len(str(x)) for x in c)//len(c)
    print(f"{name}: {len(c)} chunks, longitud media {longitud_media}")

