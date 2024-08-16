# MarkdowntoHTMLConverter.py

# pip install markdown
import markdown

def convertMarkdownToHTML(markdownFile, htmlFile):
    """Convert a Markdown file to HTML."""
    with open(markdownFile, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)
    with open(htmlFile, 'w') as f:
        f.write(html)
    print(f"Converted {markdownFile} to {htmlFile}")

convertMarkdownToHTML('README.md', 'README.html')
