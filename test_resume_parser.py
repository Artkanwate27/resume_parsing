import sys
from pathlib import Path
from src.database import Session, Candidate
from src.agents.cv_processor import CVProcessor

def test_parser(pdf_path):
    print(f"\nTesting with: {pdf_path}")
    
    session = Session()
    processor = CVProcessor(session)
    
    try:
        # Process resume
        candidate_id = processor.parse_resume(pdf_path)
        candidate = session.query(Candidate).get(candidate_id)
        
        # Display results
        print("\n✅ Successfully parsed:")
        print(f"Name: {candidate.name}")
        print(f"Email: {candidate.email}")
        print(f"Phone: {candidate.phone}")
        print("\nEducation:")
        print(candidate.education)
        print("\nSkills:")
        print(candidate.skills)
        print("\nTech Stack:")
        print(candidate.tech_stack)
        
        return True
    except Exception as e:
        print(f"\n❌ Failed to parse: {str(e)}")
        return False
    finally:
        session.close()

if __name__ == "__main__":
    # Example usage (change path to your test PDF)
    test_pdf = "data/resumes/C1236.pdf"
    
    # Verify file exists
    if not Path(test_pdf).exists():
        print(f"Error: Test file not found at {test_pdf}")
        print("Please ensure:")
        print("1. The PDF exists at that path")
        print("2. The 'data/resumes/' directory exists")
        sys.exit(1)
    
    test_parser(test_pdf)