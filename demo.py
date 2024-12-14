import nbformat

# Load the notebook
with open("notebook\exp.ipynb", "r", encoding="utf-8") as file:
    notebook = nbformat.read(file, as_version=4)

# Extract Markdown cells
with open("markdown.md", "w", encoding="utf-8") as md_file:
    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            md_file.write(cell.source + "\n\n")
