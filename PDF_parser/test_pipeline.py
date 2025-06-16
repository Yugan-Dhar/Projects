#!/usr/bin/env python3
"""
Simple test script to verify the PDF processing pipeline works correctly.
This script tests the imports and basic functionality without requiring a PDF file.
"""

import sys
import traceback

def test_imports():
    """Test that all required modules can be imported."""
    print("🔍 Testing imports...")
    
    try:
        from pipeline import PDFProcessingPipeline
        print("✅ PDFProcessingPipeline imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import PDFProcessingPipeline: {e}")
        return False
    
    try:
        from parser import CustomPDFParser
        print("✅ CustomPDFParser imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import CustomPDFParser: {e}")
        return False
    
    try:
        from langchain_loader import LangChainPDFLoader
        print("✅ LangChainPDFLoader imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import LangChainPDFLoader: {e}")
        return False
    
    try:
        import pypdf
        print("✅ pypdf imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import pypdf: {e}")
        return False
    
    try:
        from langchain.schema import Document
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        print("✅ LangChain components imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import LangChain components: {e}")
        return False
    
    return True

def test_pipeline_initialization():
    """Test that the pipeline can be initialized with different configurations."""
    print("\n🔧 Testing pipeline initialization...")
    
    try:
        from pipeline import PDFProcessingPipeline
        
        # Test default initialization
        pipeline1 = PDFProcessingPipeline()
        print("✅ Default pipeline initialization successful")
        
        # Test with custom config
        config = {
            "preserve_layout": False,
            "remove_headers_footers": True,
            "extract_images": True,
            "min_text_length": 20
        }
        pipeline2 = PDFProcessingPipeline(config)
        print("✅ Custom pipeline initialization successful")
        
        return True
    except Exception as e:
        print(f"❌ Pipeline initialization failed: {e}")
        traceback.print_exc()
        return False

def test_parser_initialization():
    """Test that the parser can be initialized with different configurations."""
    print("\n🔧 Testing parser initialization...")
    
    try:
        from parser import CustomPDFParser
        
        # Test default initialization
        parser1 = CustomPDFParser()
        print("✅ Default parser initialization successful")
        
        # Test with custom config
        parser2 = CustomPDFParser(
            extract_images=True,
            preserve_layout=False,
            remove_headers_footers=True,
            min_text_length=20
        )
        print("✅ Custom parser initialization successful")
        
        return True
    except Exception as e:
        print(f"❌ Parser initialization failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("🚀 Starting PDF Processing Pipeline Tests\n")
    
    tests = [
        test_imports,
        test_pipeline_initialization,
        test_parser_initialization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            print(f"❌ Test {test.__name__} failed")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The pipeline is ready to use.")
        print("\n📝 To use the pipeline:")
        print("1. Run 'python example.py' to start the interactive interface")
        print("2. Choose an option from the menu")
        print("3. Provide the path to a PDF file when prompted")
    else:
        print("❌ Some tests failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
