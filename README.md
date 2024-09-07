# Resume Analyzer

Resume Analyzer is a web application that provides insights for data science careers by analyzing resumes. It uses advanced natural language processing to evaluate resumes and provide feedback to help users improve their job applications.

![Resume Analyzer Upload Interface](https://saibaba9758140479.blob.core.windows.net/testimages/resume_analyzer.PNG)

## Features

- Upload resume in PDF, DOC, or DOCX format (max 10MB)
- Analyze resume content using AI
- Provide overall score and detailed feedback
- Highlight strengths and areas for improvement
- Offer actionable insights for career development

![Resume Analysis Results](https://saibaba9758140479.blob.core.windows.net/testimages/resume_analyzer_2.PNG)

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- AI Model: Gemini (for natural language processing and resume analysis)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/resume-analyzer.git
   cd resume-analyzer
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```
   flask run
   ```

6. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. On the home page, click the upload area or drag and drop your resume file (PDF, DOC, or DOCX format, max 10MB).
2. Click the "Analyze Resume" button.
3. Wait for the analysis to complete.
4. Review the analysis results, including overall score, strengths, and areas for improvement.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Gemini AI for providing the natural language processing capabilities
- Flask team for the excellent web framework
- All contributors and users of this project