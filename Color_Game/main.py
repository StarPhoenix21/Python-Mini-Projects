import logging
import os

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def read_file(filename):
    """ Reads content from a file """
    try:
        with open(filename, "r") as file:
            content = file.read()
            logging.info(f"Successfully read file: {filename}")
            return content
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        return "Error: File not found."
    except Exception as e:
        logging.error(f"Unexpected error while reading file: {e}")
        return "Error: Unable to read file."

def process_data(data):
    """ Processes the data (dummy function) """
    try:
        if not data:
            raise ValueError("No data provided for processing")
        processed = data.upper()
        logging.info("Data successfully processed")
        return processed
    except ValueError as ve:
        logging.error(f"Processing error: {ve}")
        return "Error: No valid data to process."
    except Exception as e:
        logging.error(f"Unexpected error in processing: {e}")
        return "Error: Data processing failed."

def main():
    """ Main function that runs the program """
    logging.info("Program started")

    filename = "sample.txt"
    
    # Read file content
    file_content = read_file(filename)
    if "Error" in file_content:
        print(file_content)
        return

    # Process file content
    result = process_data(file_content)
    print(result)

    logging.info("Program completed successfully")

if __name__ == "__main__":
    main()
