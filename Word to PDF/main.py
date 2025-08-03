from docx2pdf import convert
from tkinter import Tk, filedialog

def convert_docx_to_pdf():
    root = Tk()
    root.withdraw()
    docx_file_path = filedialog.askopenfilename(
        title="Select a Word file (.docx)",
        filetypes=[("Word Documents", "*.docx")]
    )
    if not docx_file_path:
        print("No file selected. Exiting.")
        return
    pdf_file_path = docx_file_path.replace(".docx", ".pdf")

    print(f"Converting '{docx_file_path}' to PDF...")
    try:
        convert(docx_file_path, pdf_file_path)
        print(f"Conversion successful! PDF saved to: '{pdf_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    convert_docx_to_pdf()