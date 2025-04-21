from docling.document_converter import DocumentConverter

# Carregamento e conversão do PDF
source = "relatorios pdf/ProjetoFinal_Rel_PlataformaOrganizcaoDeEstudos.pdf"
converter = DocumentConverter()
result = converter.convert(source)
markdown = result.document.export_to_markdown()

# Salvar markdown com utf-8
with open("markdown/ProjetoFinal_Rel_PlataformaOrganizcaoDeEstudos.md", "w", encoding="utf-8") as f:
    f.write(markdown)