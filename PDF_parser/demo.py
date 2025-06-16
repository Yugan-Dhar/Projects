#!/usr/bin/env python3
"""
Demo script showing how to use the PDF Processing Pipeline programmatically.
This script demonstrates various features without requiring user interaction.
"""

from pathlib import Path
from pipeline import PDFProcessingPipeline

def demo_pipeline_usage():
    """Demonstrate how to use the pipeline with different configurations."""
    
    print("🚀 PDF Processing Pipeline Demo")
    print("=" * 50)
    
    # Check if we have any PDF files to work with
    pdf_files = list(Path(".").glob("*.pdf"))
    
    if not pdf_files:
        print("📄 No PDF files found in the current directory.")
        print("To test with a real PDF file:")
        print("1. Place a PDF file in this directory")
        print("2. Run this demo script again")
        print("\n🔧 For now, showing configuration examples...")
        demo_configurations()
        return
    
    # Use the first PDF file found
    pdf_path = str(pdf_files[0])
    print(f"📄 Using PDF file: {pdf_path}")
    
    # Demo 1: Basic text extraction
    print("\n1️⃣ Basic Text Extraction")
    print("-" * 30)
    
    pipeline = PDFProcessingPipeline()
    try:
        text = pipeline.process_single_pdf(pdf_path, output_format="text")
        print(f"✅ Extracted {len(text)} characters of text")
        print(f"📝 Preview (first 200 chars): {text[:200]}...")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Demo 2: Raw data extraction with custom config
    print("\n2️⃣ Raw Data with Custom Configuration")
    print("-" * 40)
    
    config = {
        "preserve_layout": False,
        "remove_headers_footers": True,
        "extract_images": True,
        "min_text_length": 20
    }
    
    pipeline = PDFProcessingPipeline(config)
    try:
        raw_data = pipeline.process_single_pdf(pdf_path, output_format="raw")
        print(f"✅ Processed {raw_data['processed_pages']}/{raw_data['total_pages']} pages")
        print(f"📊 Total words: {raw_data['total_words']}")
        print(f"📄 Document title: {raw_data['document_metadata'].get('title', 'N/A')}")
        print(f"👤 Author: {raw_data['document_metadata'].get('author', 'N/A')}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Demo 3: LangChain documents without chunking
    print("\n3️⃣ LangChain Documents (No Chunking)")
    print("-" * 40)
    
    try:
        docs = pipeline.process_single_pdf(pdf_path, output_format="langchain", chunk_documents=False)
        print(f"✅ Created {len(docs)} LangChain documents")
        if docs:
            print(f"📝 First document preview: {docs[0].page_content[:200]}...")
            print(f"🏷️  Metadata keys: {list(docs[0].metadata.keys())}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Demo 4: LangChain documents with chunking
    print("\n4️⃣ LangChain Documents (With Chunking)")
    print("-" * 40)
    
    try:
        chunked_docs = pipeline.process_single_pdf(
            pdf_path, 
            output_format="langchain", 
            chunk_documents=True,
            chunk_size=300,
            chunk_overlap=50
        )
        print(f"✅ Created {len(chunked_docs)} chunks")
        if chunked_docs:
            avg_length = sum(len(doc.page_content) for doc in chunked_docs) / len(chunked_docs)
            print(f"📏 Average chunk length: {avg_length:.0f} characters")
            print(f"📝 First chunk preview: {chunked_docs[0].page_content[:150]}...")
    except Exception as e:
        print(f"❌ Error: {e}")

def demo_configurations():
    """Show different configuration options."""
    
    print("\n⚙️  Configuration Options Demo")
    print("-" * 35)
    
    configs = [
        {
            "name": "Default Configuration",
            "config": {}
        },
        {
            "name": "Layout Preserving",
            "config": {
                "preserve_layout": True,
                "remove_headers_footers": False,
                "extract_images": False,
                "min_text_length": 10
            }
        },
        {
            "name": "Clean Text Extraction",
            "config": {
                "preserve_layout": False,
                "remove_headers_footers": True,
                "extract_images": False,
                "min_text_length": 50
            }
        },
        {
            "name": "Full Feature Extraction",
            "config": {
                "preserve_layout": True,
                "remove_headers_footers": True,
                "extract_images": True,
                "min_text_length": 20
            }
        }
    ]
    
    for i, config_info in enumerate(configs, 1):
        print(f"\n{i}. {config_info['name']}")
        PDFProcessingPipeline(config_info['config'])  # Test initialization
        print(f"   ✅ Pipeline initialized successfully")
        for key, value in config_info['config'].items():
            print(f"   - {key}: {value}")

def main():
    """Run the demo."""
    try:
        demo_pipeline_usage()
        
        print("\n" + "=" * 50)
        print("🎉 Demo completed successfully!")
        print("\n📚 Next steps:")
        print("1. Run 'python example.py' for interactive interface")
        print("2. Place PDF files in this directory to test with real data")
        print("3. Check README.md for detailed usage instructions")
        
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
