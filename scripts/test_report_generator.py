from ml.vlm.report_generator import generate_radiology_report

def main():
    # Sample test case
    prediction = "glioma"
    confidence_score = 92.5

    report = generate_radiology_report(prediction, confidence_score)
    
    print("\n Generated Radiology Report:\n")
    print(report)

if __name__ == "__main__":
    main()