# Overview

This is a Smart Research Assistant application that uses AI to generate comprehensive research documents and find relevant images. The app provides a multilingual interface supporting Arabic, English, and French, with AI-powered content generation through OpenAI's API and image search capabilities via DuckDuckGo.

# User Preferences

Preferred communication style: Simple, everyday language.

## Recent User Requests (July 31, 2025)
- Always attempt to fetch 20 images in gallery, get available quantity if less than 20
- Minimize side margins in PDF output for better space utilization  
- Reduce top spacing above title and center title in PDF format
- Reduce blue frame padding around images without affecting image content
- **UPDATED**: Complete interface adaptation based on selected language
- Both interface language AND content generation language change based on language selection
- Text direction adapts automatically (RTL for Arabic, LTR for English/French)
- Maintain consistent content structure across all languages (Arabic, English, French)
- Image placeholders and UI elements translate based on selected language
- **NEW (July 31, 2025)**: Force translation of ALL Arabic titles to selected language (English/French) regardless of topic, ensuring no Arabic titles remain untranslated in the preview interface
- **UPDATED (July 31, 2025)**: Added translate button next to search input field with language icon that translates user input before research generation
- **ENHANCED (July 31, 2025)**: Improved translation system with Gemini AI integration and comprehensive fallback dictionary for names and topics

# System Architecture

## Frontend Architecture
- **Technology**: Vanilla JavaScript with TailwindCSS for styling
- **Structure**: Single-page application with dynamic content rendering
- **UI Components**: Control panel, content display area, and image gallery sidebar
- **Animation**: Custom canvas-based particle animation for visual appeal
- **Responsive Design**: Mobile-first approach with RTL (right-to-left) support for Arabic

## Backend Architecture
- **Framework**: Flask (Python web framework)
- **Structure**: Simple REST API with service-oriented architecture
- **Services**: Modular design with separate services for research generation and image search
- **Error Handling**: Comprehensive logging and graceful error responses

# Key Components

## Research Generation Service (`services/research_generator.py`)
- **Purpose**: Generates comprehensive research content using OpenAI's GPT models
- **Features**: 
  - Multi-language support (Arabic, English, French)
  - Structured research format with introduction, main sections, and conclusion
  - Markdown formatting for proper document structure
  - Image placeholder integration for visual content
  - **Enhanced Translation System**: Gemini AI-powered topic translation with comprehensive fallback dictionary
  - **Name Recognition**: Smart detection and transliteration of Arabic names (e.g., "أسماء بوجيبار" → "Asma Boujibar")

## Image Search Service (`services/image_search.py`)
- **Purpose**: Searches and retrieves relevant images for research topics
- **Technology**: DuckDuckGo Search API for image retrieval
- **Features**:
  - Image accessibility verification
  - Metadata extraction (dimensions, source, title)
  - Safe search filtering
  - Result processing and optimization
  - **Enhanced Feature**: Always attempts to fetch 20 images using multiple search strategies
  - **Smart Retry**: Uses different image sizes (medium/large/small) across attempts
  - **Duplicate Prevention**: Automatically filters out duplicate image URLs

## Frontend Components
- **Main Interface**: Dynamic content rendering with language switching
- **Background Animation**: Canvas-based particle system for visual enhancement
- **PDF Export**: Client-side PDF generation using html2pdf.js
- **Image Integration**: Drag-and-drop image placement into research content
- **Translate Button**: In-field translation button that translates user input to selected language before research generation

# Data Flow

1. **User Input**: User enters research topic and selects language
2. **Research Generation**: 
   - Frontend sends topic and language to `/api/generate-research`
   - Backend calls OpenAI API with language-specific prompts
   - Generated content is returned and rendered as Markdown
3. **Image Search**:
   - System automatically searches for relevant images
   - Images are fetched via `/api/search-images` endpoint
   - Results are displayed in sidebar gallery
4. **Content Assembly**: Users can insert images into research placeholders
5. **Export**: Final document can be exported as PDF

# External Dependencies

## APIs and Services
- **OpenAI API**: Content generation using GPT models
- **DuckDuckGo Search**: Image search and retrieval
- **Required Environment Variables**:
  - `OPENAI_API_KEY`: OpenAI API authentication
  - `SESSION_SECRET`: Flask session security (optional, has default)

## Frontend Libraries
- **TailwindCSS**: Utility-first CSS framework
- **Marked.js**: Markdown to HTML conversion
- **html2pdf.js**: Client-side PDF generation
- **Font Awesome**: Icon library
- **Google Fonts**: Cairo and Rajdhani font families

## Python Dependencies
- **Flask**: Web framework
- **OpenAI**: Official OpenAI Python client
- **duckduckgo-search**: DuckDuckGo search API wrapper
- **requests**: HTTP client for API calls

# Deployment Strategy

## Development Setup
- **Entry Point**: `main.py` starts the Flask development server
- **Configuration**: Environment-based configuration for API keys
- **Debug Mode**: Enabled for development with detailed error logging

## Production Considerations
- **Security**: Session secret configuration required
- **Logging**: Structured logging for monitoring and debugging
- **Error Handling**: Graceful degradation with user-friendly error messages
- **Rate Limiting**: Should be implemented for API endpoints in production

## File Structure
```
├── app.py                 # Main Flask application
├── main.py               # Application entry point
├── services/             # Business logic services
│   ├── research_generator.py
│   └── image_search.py
├── templates/            # HTML templates
│   └── index.html
├── static/              # Static assets
│   └── js/
│       ├── app.js       # Main application logic
│       └── background.js # Canvas animation
└── attached_assets/     # Additional resources
```

The application follows a clean separation of concerns with dedicated services for external API interactions, a simple Flask backend for API endpoints, and a dynamic frontend that handles user interactions and content rendering.