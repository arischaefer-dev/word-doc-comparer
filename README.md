# 📄 Word Document Comparer

An intelligent web application that compares Word documents with comments against revised versions to validate whether changes were correctly applied.

## ✨ Features

- **Smart Comment Extraction**: Automatically extracts comments from Word documents
- **User Scope Control**: Specify whether changes should be local or global
- **AI-Powered Analysis**: Uses Claude/OpenAI for intelligent comment interpretation
- **Visual Diff Highlighting**: Side-by-side comparison with missed instance highlighting
- **Precise Global Validation**: Counts all instances for global changes
- **Enhanced Local Validation**: Context-aware analysis for local changes

## 🚀 Quick Start

### Local Development
```bash
git clone <your-repo-url>
cd word-doc-comparer
pip install -r requirements.txt
python app.py
```

### Environment Variables
```bash
ANTHROPIC_API_KEY=your_key_here    # Optional: For AI analysis
OPENAI_API_KEY=your_key_here       # Optional: For AI analysis
FLASK_SECRET_KEY=your_secret_key   # Required for production
```

## 📖 How to Use

1. **Upload Documents**: Upload original document (with comments) and revised document
2. **Review Scope**: Specify whether each comment should be applied locally or globally
3. **Analyze**: View intelligent analysis of whether changes were correctly applied
4. **Visual Diff**: See side-by-side comparison with highlighted missed instances

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Document Processing**: python-docx
- **AI Integration**: Anthropic Claude, OpenAI GPT
- **Frontend**: HTML/CSS/JavaScript
- **Deployment**: Railway-ready

## 📋 Example Use Cases

- **Content Editing**: Validate that editor comments were properly addressed
- **Document Review**: Ensure all requested changes were implemented
- **Quality Assurance**: Catch missed edits before final publication
- **Educational**: Check if student revisions match instructor feedback

## 🎯 Key Improvements

- **Global Change Detection**: Precisely counts instances (e.g., "12 of 13 name changes")
- **Visual Missed Instance Highlighting**: Red highlighting shows exactly what was missed
- **No False Positives**: User scope selection prevents incorrect "success" messages
- **Context-Aware Analysis**: Smart validation based on surrounding text

## 🔧 Development

The app gracefully handles missing AI API keys by falling back to pattern-based analysis while maintaining accuracy for user-scoped changes.

## 📝 License

MIT License - Feel free to use and modify!