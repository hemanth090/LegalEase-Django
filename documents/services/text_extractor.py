"""
Text extraction services for different file types.
Supports PDF, DOCX, and image files with OCR.
"""

import logging
from io import BytesIO
from PIL import Image
import pytesseract
from docx import Document as DocxDocument
import PyPDF2

logger = logging.getLogger(__name__)


def extract_text_from_docx(file_content):
    """
    Extract text from Word document (.docx).
    
    Args:
        file_content: Binary content of DOCX file
        
    Returns:
        str: Extracted text
    """
    try:
        logger.info("Extracting text from DOCX file")
        
        file_stream = BytesIO(file_content)
        doc = DocxDocument(file_stream)
        
        text_parts = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text_parts.append(paragraph.text.strip())
        
        extracted_text = '\n'.join(text_parts)
        logger.info(f"DOCX extraction successful: {len(extracted_text)} characters")
        return extracted_text
        
    except Exception as e:
        logger.error(f"DOCX extraction error: {str(e)}")
        raise Exception(f"Failed to extract text from DOCX: {str(e)}")


def extract_text_from_pdf(file_content):
    """
    Extract text from PDF file.
    
    Args:
        file_content: Binary content of PDF file
        
    Returns:
        str: Extracted text
    """
    try:
        logger.info("Extracting text from PDF file")
        
        file_stream = BytesIO(file_content)
        pdf_reader = PyPDF2.PdfReader(file_stream)
        
        text_parts = []
        for page_num, page in enumerate(pdf_reader.pages):
            try:
                page_text = page.extract_text()
                if page_text.strip():
                    text_parts.append(page_text.strip())
            except Exception as page_error:
                logger.warning(f"Could not extract text from page {page_num + 1}: {page_error}")
                continue
        
        extracted_text = '\n\n--- Page Break ---\n\n'.join(text_parts)
        
        if not extracted_text.strip():
            return "This PDF appears to contain images or scanned content. OCR processing may be needed."
        
        logger.info(f"PDF extraction successful: {len(extracted_text)} characters")
        return extracted_text
        
    except Exception as e:
        logger.error(f"PDF extraction error: {str(e)}")
        raise Exception(f"Failed to extract text from PDF: {str(e)}")


def extract_text_from_image(file_content):
    """
    Extract text from image using OCR.
    
    Args:
        file_content: Binary content of image file
        
    Returns:
        str: Extracted text
    """
    try:
        logger.info("Extracting text from image using OCR")
        
        file_stream = BytesIO(file_content)
        image = Image.open(file_stream)
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        extracted_text = pytesseract.image_to_string(image, lang='eng')
        extracted_text = extracted_text.strip()
        
        if not extracted_text:
            return "No readable text found in this image."
        
        logger.info(f"Image OCR successful: {len(extracted_text)} characters")
        return extracted_text
        
    except Exception as e:
        logger.error(f"Image extraction error: {str(e)}")
        raise Exception(f"Failed to extract text from image: {str(e)}")


def determine_file_type(filename, content_type):
    """
    Determine file type from filename and content type.
    
    Args:
        filename: Name of the file
        content_type: MIME type
        
    Returns:
        str: File type ('pdf', 'docx', 'image', or 'unknown')
    """
    # Check by content type
    if content_type == 'application/pdf':
        return 'pdf'
    elif content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return 'docx'
    elif content_type.startswith('image/'):
        return 'image'
    
    # Check by file extension
    filename_lower = filename.lower()
    if filename_lower.endswith('.pdf'):
        return 'pdf'
    elif filename_lower.endswith('.docx'):
        return 'docx'
    elif filename_lower.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
        return 'image'
    
    return 'unknown'


def extract_text_from_file(file_content, file_type):
    """
    Extract text from file based on type.
    
    Args:
        file_content: Binary content of file
        file_type: Type of file ('pdf', 'docx', or 'image')
        
    Returns:
        str: Extracted text
    """
    logger.info(f"Extracting text from {file_type} file")
    
    if file_type == 'pdf':
        return extract_text_from_pdf(file_content)
    elif file_type == 'docx':
        return extract_text_from_docx(file_content)
    elif file_type == 'image':
        return extract_text_from_image(file_content)
    else:
        raise Exception(f"Unsupported file type: {file_type}")