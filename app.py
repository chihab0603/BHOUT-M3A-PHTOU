import os
import logging
from flask import Flask, render_template, request, jsonify
from services.research_generator import ResearchGenerator
from services.image_search import ImageSearchService
import requests
import base64

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Initialize services
research_generator = ResearchGenerator()
image_search_service = ImageSearchService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-research', methods=['POST'])
def generate_research():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        language = data.get('language', 'ar')
        
        if not topic:
            return jsonify({'success': False, 'error': 'Topic is required'})
        
        content = research_generator.generate_research(topic, language)
        
        return jsonify({
            'success': True,
            'content': content
        })
        
    except Exception as e:
        logging.error(f"Error generating research: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/translate-topic', methods=['POST'])
def translate_topic():
    """Translate topic to target language using AI"""
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        target_language = data.get('target_language', 'en')
        
        if not topic:
            return jsonify({'success': False, 'error': 'Topic is required'})
        
        # Use research generator to translate the topic
        translated_topic = research_generator.translate_topic(topic, target_language)
        
        return jsonify({
            'success': True,
            'translated_topic': translated_topic,
            'original_topic': topic,
            'target_language': target_language
        })
        
    except Exception as e:
        logging.error(f"Error translating topic: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/search-images', methods=['POST'])
def search_images():
    try:
        data = request.get_json()
        query = data.get('query', '')
        language = data.get('language', 'ar')
        
        if not query:
            return jsonify({'success': False, 'error': 'Query is required'})
        
        images = image_search_service.search_images(query, language)
        
        return jsonify({
            'success': True,
            'images': images
        })
        
    except Exception as e:
        logging.error(f"Error searching images: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/proxy-image')
def proxy_image():
    """Proxy images to avoid CORS issues"""
    try:
        url = request.args.get('url')
        if not url:
            return '', 400
            
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }, timeout=10)
        
        if response.status_code == 200:
            # Convert to base64 for PDF compatibility
            image_data = base64.b64encode(response.content).decode('utf-8')
            content_type = response.headers.get('content-type', 'image/jpeg')
            
            return jsonify({
                'success': True,
                'data': f"data:{content_type};base64,{image_data}"
            })
        else:
            return jsonify({'success': False, 'error': 'Failed to fetch image'}), 400
            
    except Exception as e:
        logging.error(f"Error proxying image: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
