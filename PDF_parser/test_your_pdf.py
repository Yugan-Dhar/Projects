#!/usr/bin/env python3
"""
Quick test script for your specific PDF file.
This will automatically test all features with your Offer Letter PDF.
"""

from pipeline import PDFProcessingPipeline
import traceback

def test_pdf():
    """Test the PDF processing with your offer letter."""
    
    pdf_path = "Offer-Letter-655771747072978.pdf"
    
    print("🚀 Testing PDF Processing Pipeline")
    print("=" * 50)
    print(f"📄 PDF File: {pdf_path}")
    print()
    
    # Initialize pipeline with good settings for documents
    config = {
        "preserve_layout": False,
        "remove_headers_footers": True,
        "extract_images": True,
        "min_text_length": 10
    }
    
    pipeline = PDFProcessingPipeline(config)
    
    try:
        # Test 1: Extract plain text
        print("1️⃣ EXTRACTING PLAIN TEXT")
        print("-" * 30)
        text = pipeline.process_single_pdf(pdf_path, output_format="text")
        print(f"✅ Successfully extracted {len(text)} characters")
        print(f"📝 First 500 characters:")
        print(text[:500])
        print("..." if len(text) > 500 else "")
        print()
        
        # Test 2: Get raw data with metadata
        print("2️⃣ GETTING RAW DATA & METADATA")
        print("-" * 35)
        raw_data = pipeline.process_single_pdf(pdf_path, output_format="raw")
        
        print(f"✅ Processed {raw_data['processed_pages']}/{raw_data['total_pages']} pages")
        print(f"📊 Total words: {raw_data['total_words']}")
        print(f"📄 File size: {raw_data['document_metadata'].get('file_size', 'N/A')} bytes")
        
        # Show document metadata
        print("\n📋 Document Metadata:")
        for key, value in raw_data['document_metadata'].items():
            if value:  # Only show non-empty values
                print(f"   {key}: {value}")
        
        # Show first page info
        if raw_data['pages']:
            first_page = raw_data['pages'][0]
            print(f"\n📄 First page info:")
            print(f"   Word count: {first_page['word_count']}")
            print(f"   Text preview: {first_page['text'][:200]}...")
        print()
        
        # Test 3: LangChain documents without chunking
        print("3️⃣ LANGCHAIN DOCUMENTS (NO CHUNKING)")
        print("-" * 40)
        docs = pipeline.process_single_pdf(pdf_path, output_format="langchain", chunk_documents=False)
        print(f"✅ Created {len(docs)} LangChain documents")
        
        if docs:
            print(f"📝 First document length: {len(docs[0].page_content)} characters")
            print(f"🏷️  Metadata keys: {list(docs[0].metadata.keys())}")
            print(f"📄 Page number: {docs[0].metadata.get('page_number', 'N/A')}")
        print()
        
        # Test 4: LangChain documents with chunking
        print("4️⃣ LANGCHAIN DOCUMENTS (WITH CHUNKING)")
        print("-" * 40)
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
            print(f"📝 First chunk preview:")
            print(f"   {chunked_docs[0].page_content[:200]}...")
        print()
        
        # Test 5: Check for images
        print("5️⃣ IMAGE METADATA CHECK")
        print("-" * 25)
        found_images = False
        for i, page in enumerate(raw_data['pages']):
            images = page['metadata'].get('images', [])
            if images:
                found_images = True
                print(f"📷 Page {i+1} has {len(images)} images")
                for img in images:
                    print(f"   - {img}")
        
        if not found_images:
            print("📷 No images found in the document")
        print()
        
        print("=" * 50)
        print("🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
        print("✅ Your PDF processing pipeline is working correctly")
        
    except Exception as e:
        print(f"❌ Error processing PDF: {e}")
        print("\n🔍 Full error details:")
        traceback.print_exc()

if __name__ == "__main__":
    test_pdf()
