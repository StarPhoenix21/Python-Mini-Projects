from docx2pdf import convert
from tkinter import Tk, filedialog

def convert_docx_to_pdf():
    # Initialize and hide the main tkinter window
    root = Tk()
    root.withdraw()

    # Open a file dialog to let the user select a .docx file
    docx_file_path = filedialog.askopenfilename(
        title="Select a Word file (.docx)",
        filetypes=[("Word Documents", "*.docx")]
    )

    # If no file is selected, print a message and exit
    if not docx_file_path:
        print("No file selected. Exiting.")
        return

    # Create the output file path by replacing the extension
    pdf_file_path = docx_file_path.replace(".docx", ".pdf")

    print(f"Converting '{docx_file_path}' to PDF...")
    try:
        # Convert the .docx file to a PDF
        convert(docx_file_path, pdf_file_path)
        print(f"Conversion successful! PDF saved to: '{pdf_file_path}'")
    except Exception as e:
        # Handle any errors during the conversion process
        print(f"An error occurred during conversion: {e}")

# Run the conversion function when the script is executed
if __name__ == "__main__":
    convert_docx_to_pdf()
