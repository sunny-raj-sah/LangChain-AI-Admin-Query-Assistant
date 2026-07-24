# 🎓 # AI-Powered Admin Panel with Natural Language Processing

AI-powered admin panel with natural language querying and role-based access control.

## 🎯 Features

- Natural language query processing using LangChain + OpenAI
- Role-based access control (grade, class, region filtering)
- Interactive Streamlit interface
- Query history and example queries
- Modular architecture for easy database integration

## 🛠️ Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.env` file with your OpenAI API key:
   OPENAI_API_KEY=your_key_here
6. Run: `streamlit run src/app.py`

## 💡 Example Queries

1. **"Which students haven't submitted their homework yet?"**

   - Returns list of students with `homework_submitted = false`

2. **"Show me performance data for Grade 8 from last week"**

   - Filters by grade 8 and recent quiz dates

3. **"List all upcoming quizzes scheduled for next week"**
   - Shows quizzes with dates after November 12, 2025

## 🔐 Access Control

Admins can only view data for their assigned:

- Grades (e.g., Grade 8 only)
- Classes (e.g., 8A, 8B)
- Regions (e.g., North, South)

## 📁 Project Structure

ai-assignment/
├── data/ # JSON datasets
├── src/ # Python modules
├── requirements.txt # Dependencies
├── .env # API keys (gitignored)
└── README.md # This file

## 🎥 Demo
 (https://![Demo](<Screenshot 2025-11-20 125016-1.png>)) 

## 🔮 Future Enhancements

- Connect to real database (PostgreSQL/MongoDB)
- Add authentication system
- Support for more complex queries
- Export results to CSV/PDF
  ✅ Testing Your Application
  Test with these queries:
  "Which students haven't submitted their homework yet?"
  "Show me students who scored above 80 in quizzes"
  "List all quizzes scheduled after November 10"
  "What is the average quiz score for my students?"
  "Show me all students in class 8A"
  🎯 Key Features Demonstrated
  ✅ Natural language processing with LangChain
  ✅ OpenAI integration for query understanding
  ✅ Role-based access control (filters by grade/class/region)
  ✅ Streamlit UI with example queries
  ✅ Modular code structure (easy to swap CSV → Database)
  ✅ Query history and context handling
  ✅ Clean, documented code
  📤 Submission Checklist
  Before submitting:
  ✅ Test all example queries
  ✅ Verify access control works (switch between admins)
  ✅ Add your OpenAI API key to .env
  ✅ Take screenshots of the working app
  ✅ Record a short Loom demo (optional but recommended)
  ✅ Push to GitHub with clear README
  ✅ Add .gitignore to exclude .env and venv/
