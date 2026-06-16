"""
Document processing utilities for extracting and parsing Nepali legal PDFs.
Use this to prepare legal documents after downloading them from lawcommission.gov.np
"""

import pdfplumber
import json
from pathlib import Path
from typing import List, Dict

class DocumentProcessor:
    """Extract and process legal documents from PDFs"""

    def __init__(self, data_dir: str = "data/pdfs"):
        self.data_dir = Path(data_dir)
        self.documents = []

    def extract_from_pdf(self, pdf_path: str) -> Dict:
        """
        Extract text from a Nepali PDF.

        Returns dict with:
        - title: Act name
        - sections: List of sections with text
        - raw_text: Full PDF text
        """
        try:
            with pdfplumber.open(pdf_path) as pdf:
                full_text = ""
                sections = []

                for page_num, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        full_text += text + "\n"

                # TODO: Parse sections based on Nepali legal structure
                # Example: "Section 45", "धारा ४५", "Part 2", etc.

                return {
                    "source_file": Path(pdf_path).name,
                    "raw_text": full_text,
                    "sections": sections,
                    "page_count": len(pdf.pages)
                }

        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
            return None

    def process_all_pdfs(self) -> List[Dict]:
        """
        Process all PDFs in the data directory.
        Returns list of processed documents.
        """
        if not self.data_dir.exists():
            print(f"Create {self.data_dir} and add your PDFs there")
            return []

        pdf_files = list(self.data_dir.glob("*.pdf"))
        print(f"Found {len(pdf_files)} PDFs")

        for pdf_file in pdf_files:
            doc = self.extract_from_pdf(str(pdf_file))
            if doc:
                self.documents.append(doc)
                print(f"✓ Processed: {pdf_file.name}")

        return self.documents

    def save_processed_docs(self, output_file: str = "data/documents.json"):
        """
        Save processed documents as JSON for later use.
        """
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.documents, f, ensure_ascii=False, indent=2)

        print(f"Saved {len(self.documents)} documents to {output_file}")

    @staticmethod
    def load_documents(doc_file: str = "data/documents.json") -> List[Dict]:
        """Load previously processed documents from JSON."""
        try:
            with open(doc_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Document file not found: {doc_file}")
            return []


# Usage example:
if __name__ == "__main__":
    processor = DocumentProcessor("data/pdfs")

    # Process all PDFs
    docs = processor.process_all_pdfs()

    # Save to JSON for use in app
    if docs:
        processor.save_processed_docs("data/documents.json")
        print(f"\nProcessed {len(docs)} documents")
    else:
        print("No documents processed. Add PDFs to data/pdfs/")
