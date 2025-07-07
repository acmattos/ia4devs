from utils.architecture_detection_service import ArchitectureDetectionService
from utils.config import DEFAULT_SOURCE_FILE_PATH

if __name__ == '__main__':
    # Initialize detection service with default parameters
    architecture_detection_service = ArchitectureDetectionService()
    
    # Process the image (detect architecture components and generate report)
    results, report_json = architecture_detection_service.process_image(DEFAULT_SOURCE_FILE_PATH)
    
    print(f"✅ Architecture detection completed with {len(results)} detections")
    print(f"✅ Report generated successfully")
