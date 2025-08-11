import sys
from pathlib import Path
from src.database import Session
from src.agents.cv_processor import CVProcessor

def debug_parsing(pdf_path):
    print(f"\nDebugging: {pdf_path}")
    session = Session()
    processor = CVProcessor(session)
    
    # Step 1: Check PDF text extraction
    raw_text = processor.extract_text(pdf_path)
    print("\n=== RAW TEXT ===")
    print(raw_text[:500] + "...")  # First 500 chars
    
    # Step 2: Test field extraction
    test_fields = [
        ('name', r'Name: (.+?)(?:\n|$)'),
        ('email', r'Email: (.+?)(?:\n|$)'),
        ('tech_stack', r'Tech Stack\n(.+?)(?:\n##|\Z)', re.DOTALL)
    ]
    
    for field, pattern in test_fields:
        match = re.search(pattern, raw_text)
        print(f"\n{field.upper()} EXTRACTION:")
        print("Pattern:", pattern)
        print("Match:", match.group(1) if match else "NO MATCH")
    
    # Step 3: Full parse
    print("\n=== FULL PARSE ===")
    candidate_id = processor.parse_resume(pdf_path)
    candidate = session.get(Candidate, candidate_id)
    
    print("\nFINAL RESULT:")
    print(f"Name: {candidate.name}")
    print(f"Email: {candidate.email}")
    print(f"Tech Stack: {candidate.tech_stack}")

if __name__ == "__main__":
    pdf_path = sys.argv[1] if len(sys.argv) > 1 else "data/resumes/C1236.pdf"
    debug_parsing(pdf_path)