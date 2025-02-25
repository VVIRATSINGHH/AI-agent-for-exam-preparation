from exam_prep_ai import ExamPrepAI
import os

def validate_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    ext = file_path.split('.')[-1].lower()
    if ext not in ['pdf', 'jpg', 'jpeg', 'png']:
        raise ValueError("Unsupported file format")

def main():
    try:
        exam_ai = ExamPrepAI()
        exam_ai.download_models()

        file_path = input("Enter study material path (PDF/Image): ")
        validate_file(file_path)
        days_until_exam = int(input("Enter days until exam: "))
        text = exam_ai.process_document(file_path)
        analysis = {
            'summary': exam_ai.generate_summary(text),
            'questions': exam_ai.extract_important_questions(text),
            'study_plan': exam_ai.create_study_plan(...)
        }

        print("\n=== Analysis ===")
        for key, value in analysis.items():
            print(f"\n{key.upper()}:")
            if isinstance(value, list):
                for i, item in enumerate(value, 1):
                    print(f"{i}. {item}")
            else:
                print(value)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
