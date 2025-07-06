from flask import Flask, request, jsonify
import os
import sys
from PIL import Image
import tempfile

# Add the parent directory to the path so we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_predict import predict
from report_generator import generate_report

app = Flask(__name__)

@app.route('/mcp/face-detect', methods=['POST'])
def face_detect():
    if 'image' not in request.files:
        return jsonify({'error': 'An image is required'}), 400
    
    # Get the uploaded image
    image_file = request.files['image']
    
    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
        image_file.save(temp_file.name)
        temp_image_path = temp_file.name
    
    try:
        # Configuration for face detection (same as in report.py)
        trained_dir_name: str = "yolo11n_custom_100"
        trained_model_best_path = f"./data/model/trained/{trained_dir_name}/weights/best.pt"
        conf = 0.7

        # Run face detection using the uploaded image
        results, report_json = predict(
            trained_dir_name,
            trained_model_best_path,
            temp_image_path,  # Use the uploaded image
            conf
        )
        
        # Generate report
        reports_path: str = f"data/reports/{trained_dir_name}"
        stride_yaml_path = "data/stride/stride_map.yaml"
        controls_yaml = "data/stride/controls_by_threat.yaml"
        
        generate_report(
            reports_json_path=report_json,
            stride_yaml_path=stride_yaml_path,
            controls_yaml=controls_yaml,
            conf_threshold=0.2,
            reports_path=reports_path
        )
        
        return jsonify({
            'success': 'Face detection completed successfully!',
            'detections': len(results),
            'report_generated': True
        }), 201
        
    except Exception as face_detection_error:
        return jsonify({'error': f'Face detection failed: {str(face_detection_error)}'}), 500
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_image_path):
            os.unlink(temp_image_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
