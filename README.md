

# 📄 LexiGuardAI v2.0 — AI-Powered Contract Risk Analyzer

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange?style=for-the-badge&logo=streamlit)
![Gemini](https://img.shields.io/badge/Powered%20By-Google%20Gemini-blue?style=for-the-badge&logo=google)
![LegalDocs](https://img.shields.io/badge/Legal%20Parsing-PyMuPDF%20%26%20python-docx-green?style=for-the-badge)

> **Submitted for**: Google Solution Challenge 2025  
> **UN SDG Focus**: [Decent Work and Economic Growth (SDG 8)](https://sdgs.un.org/goals/goal8), [Reduced Inequalities (SDG 10)](https://sdgs.un.org/goals/goal10)

---

## 🌟 Overview

**LexiGuardAI v2.0** is a GenAI-powered legal assistant that simplifies and secures OTT content licensing by analyzing contracts for potential risks. By combining document parsing tools with Google’s Gemini models, LexiGuardAI enables startups and legal teams to quickly identify risky clauses and make informed decisions.

---

## 🎯 Problem Statement

Content and licensing agreements are lengthy, complex, and filled with legal jargon. Startups and OTT platforms face:

- Lack of affordable legal expertise  
- Difficulty detecting risk in contracts  
- Time-consuming manual reviews  

**LexiGuardAI** solves these problems by providing:  
- AI-based clause identification and explanation  
- Risk evaluation with reasoning  
- Interactive visual summaries and exportable audit trails  

---

## 🧠 Key Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 📄 **Contract Upload**         | Upload `.pdf`, `.docx`, or `.txt` files for instant parsing and review     |
| 🧩 **Clause Detection**        | Identifies key legal sections like IP rights, termination, indemnity       |
| ⚠️ **Risk Evaluation**         | Labels clauses as Low / Medium / High risk using Gemini with explanations  |
| 📊 **Visual Insights**         | View risks by category using heatmaps, bar graphs, and summary tables      |
| 📁 **Audit Trail Export**      | Download clause-by-clause analysis in CSV or JSON                          |

---

## 🚀 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)  
- **LLM API**: Google Gemini 1.5 Flash  
- **Document Parsing**: PyMuPDF (PDF), python-docx (DOCX)  
- **Visualization**: Seaborn, Matplotlib  
- **Language**: Python 3.11+

---

## 📷 UI Preview

> _Add screenshots or GIFs of your app interface here._

---

## 🛠️ Installation & Usage

1. **Clone the repository**
```bash
git clone https://github.com/your-username/sami-codeai-lexiguardai.git
cd sami-codeai-lexiguardai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run LexiGuardAi.py
```

4. **Interact with the app**
- Upload your contract document  
- Analyze for clause categorization and risk  
- Download audit reports for review  

---

## 🔐 API Configuration

Add your API key in `LexiGuardAi.py`:

```python
GEMINI_API_KEY = "your-gemini-api-key"
```

---

## 🌍 Impact Alignment: UN SDGs

✅ **SDG 8** — Enables safe, fair digital content agreements that promote economic participation  
✅ **SDG 10** — Reduces legal inequalities through free and AI-driven contract analysis  

---

## 📚 Future Enhancements

- ✅ Support for regional legal formats (India, EU, US)  
- ✅ Firebase Auth for personalized clause history  
- ✅ Clause comparison across multiple contracts  
- ✅ Integrated legal chatbot assistant  
- ✅ Export summaries in legal-friendly PDF format  

---

## 🤝 Contributing

Pull requests are welcome! For major updates, please open an issue to discuss.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 📬 Contact

For queries, contributions, or collaborations:  
📧 **your.email@example.com**  
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile) • [GitHub](https://github.com/your-username)

---

> Made with ❤️ for the Google Solution Challenge 2025
