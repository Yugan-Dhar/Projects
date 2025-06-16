# PDF Processing Pipeline

A comprehensive PDF parsing and processing pipeline built with Python, featuring custom text extraction, header/footer removal, image metadata extraction, and LangChain integration for document processing workflows.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test with your PDF:**
   ```bash
   python test_your_pdf.py
   ```

3. **Interactive interface:**
   ```bash
   python example.py
   ```

## Features

- **Custom PDF Parsing**: Extract text with layout preservation options
- **Header/Footer Removal**: Automatically detect and remove repeated headers/footers
- **Image Metadata Extraction**: Extract basic image information from PDF pages
- **LangChain Integration**: Convert parsed content to LangChain Documents
- **Text Chunking**: Split large documents into smaller chunks for processing
- **Flexible Output Formats**: Raw data, plain text, or LangChain Documents
- **Interactive Interface**: Easy-to-use command-line interface

## Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install pypdf langchain
   ```

2. **Verify Installation**:
   ```bash
   python test_pipeline.py
   ```

## Usage

### Quick Testing

**Test with your PDF file:**
```bash
python test_your_pdf.py
```
This automatically tests all features with your PDF file and shows comprehensive results.

**General testing and verification:**
```bash
python test_pipeline.py
```
This verifies that all components are working correctly.

**Demo with configuration examples:**
```bash
python demo.py
```
This shows different configuration options and usage patterns.

### Interactive Interface

Run the main example script for an interactive experience:

```bash
python example.py
```

This will present you with options to:
1. View full parsed raw data
2. Extract full plain text
3. Get LangChain documents (no chunking)
4. Get LangChain documents (with chunking)
5. Show document metadata
6. Show per-page metadata
7. Show cleaned page text (header/footer removed)
8. Show extracted image metadata

**When prompted for the PDF path, enter:**
```
Offer-Letter-655771747072978.pdf
```
(or the full path to your PDF file)

### Programmatic Usage

```python
from pipeline import PDFProcessingPipeline

# Initialize pipeline with custom configuration
config = {
    "preserve_layout": False,
    "remove_headers_footers": True,
    "extract_images": True,
    "min_text_length": 20
}
pipeline = PDFProcessingPipeline(config)

# Process PDF and get raw data
raw_data = pipeline.process_single_pdf("path/to/your/file.pdf", output_format="raw")

# Get LangChain documents with chunking
documents = pipeline.process_single_pdf(
    "path/to/your/file.pdf", 
    output_format="langchain", 
    chunk_documents=True,
    chunk_size=500,
    chunk_overlap=50
)

# Get plain text only
text = pipeline.process_single_pdf("path/to/your/file.pdf", output_format="text")
```

## Configuration Options

- **preserve_layout**: Keep layout spacing in text extraction (default: True)
- **remove_headers_footers**: Detect and remove repeated headers/footers (default: True)
- **extract_images**: Extract image metadata from pages (default: False)
- **min_text_length**: Minimum text length for valid pages (default: 10)

## Output Formats

### Raw Format
Returns a dictionary with:
- `full_text`: Combined text from all pages
- `pages`: List of page data with text and metadata
- `document_metadata`: File and PDF metadata
- `total_pages`: Total pages in PDF
- `processed_pages`: Pages kept after filtering
- `total_words`: Total word count

### LangChain Format
Returns a list of LangChain Document objects with:
- `page_content`: Extracted text content
- `metadata`: Combined document and page metadata

### Text Format
Returns a simple string with all extracted text combined.

## File Structure

### Core Components
- `pipeline.py`: Main processing pipeline class
- `parser.py`: Custom PDF parser with advanced features
- `langchain_loader.py`: LangChain integration and document loading

### User Interface & Testing
- `example.py`: Interactive command-line interface
- `test_your_pdf.py`: Comprehensive test script for your specific PDF
- `test_pipeline.py`: System verification and component testing
- `demo.py`: Configuration examples and programmatic usage demos

### Documentation & Configuration
- `README.md`: This documentation file
- `requirements.txt`: Python dependencies
- `Offer-Letter-655771747072978.pdf`: Sample PDF file for testing

## Testing

### Comprehensive Testing Options

**1. Test with your specific PDF file:**
```bash
python test_your_pdf.py
```
- Automatically processes your PDF with all features
- Shows extracted text, metadata, and document structure
- Tests LangChain integration and chunking
- Displays comprehensive results

**2. Verify system components:**
```bash
python test_pipeline.py
```
- Tests all imports are working correctly
- Verifies pipeline initialization with different configurations
- Confirms parser initialization with custom settings

**3. Interactive testing:**
```bash
python example.py
```
- Choose from 8 different processing options
- Test specific features interactively
- Perfect for exploring different output formats

**4. Configuration examples:**
```bash
python demo.py
```
- Shows different configuration patterns
- Demonstrates programmatic usage
- Tests pipeline initialization with various settings

## Troubleshooting

### Common Issues

1. **Import Errors**:
   - Run `pip install -r requirements.txt` to install all dependencies
   - Verify installation with `python test_pipeline.py`

2. **PDF Not Found**:
   - Ensure the PDF file path is correct and the file exists
   - For the sample PDF, use: `Offer-Letter-655771747072978.pdf`
   - Use full path if the file is in a different directory

3. **Empty Output**:
   - Check if the PDF has extractable text (some PDFs are image-only)
   - Try different `preserve_layout` settings
   - Reduce `min_text_length` parameter

4. **Memory Issues**:
   - For large PDFs, use chunking: `chunk_documents=True`
   - Reduce `chunk_size` parameter (default: 500)
   - Process page by page instead of full document

5. **Permission Errors**:
   - Ensure the PDF file is not open in another application
   - Check file permissions for read access

### Getting Help

- Run `python test_your_pdf.py` for comprehensive diagnostics
- Check the terminal output for specific error messages
- Verify all components work with `python test_pipeline.py`

## Requirements

- Python 3.7+
- pypdf >= 3.0.0
- langchain >= 0.0.350
- Additional dependencies listed in requirements.txt
