from flask import Flask, request, jsonify
import sys
import os

# Add the current directory to the path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.temp_file_handler import TempFileHandler
from utils.architecture_detection_service import ArchitectureDetectionService

app = Flask(__name__)

@app.route('/mcp/architecture-detect', methods=['POST'])
def architecture_detect():
    if 'image' not in request.files:
        return jsonify({'error': 'An image is required'}), 400
    
    # Get the uploaded image
    image_file = request.files['image']
    
    # Save the uploaded image to a temporary file
    temp_image_path = TempFileHandler.save_uploaded_file(image_file)
    
    try:
        # Initialize architecture detection service
        architecture_detection_service = ArchitectureDetectionService()
        
        # Process the image (detect architecture components and generate report)
        results, report_json = architecture_detection_service.process_image(temp_image_path)
        
        return jsonify({
            'success': 'Architecture detection completed successfully!',
            'detections': len(results),
            'report_generated': True
        }), 201
        
    except Exception as detection_error:
        return jsonify({'error': f'Architecture detection failed: {str(detection_error)}'}), 500
    
    finally:
        # Clean up the temporary file
        TempFileHandler.cleanup_temp_file(temp_image_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
