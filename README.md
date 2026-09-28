# Gen-AI-Chatbot-Karachi-Urban-Real-Estate-Advisor

An intelligent, multi-module AI assistant and automated data analytics engine specifically engineered for Karachi's real estate ecosystem, urban planning insights, and custom dataset exploration.

---

## 🎯 Core Capabilities

* **Karachi Real Estate Domain Intelligence:** Provides contextual guidance on locality pricing, land-lease types, SBCA/KDA legal documentation checks, and municipal infrastructure factors.
* **General AI Reasoning:** Open-domain conversational AI powered by ultra-low-latency Groq inference (`gpt-oss-120b` / `20b` models).
* **Automated Data Analytics:** Inbuilt Pandas & Plotly engine that accepts user CSV uploads, calculates summary statistics, and generates dynamic visual charts automatically.
* **Modular Architecture:** Isolated session states and module switching for real estate domain queries, general tasks, and analytical workloads.

---

## 🛠️ Tech Stack

* **Framework:** Streamlit
* **LLM Orchestration:** LangChain Core & LangChain Groq
* **Inference Provider:** Groq Cloud API
* **Data & Analytics:** Pandas, Plotly Express
* **Version Control & Hosting:** GitHub & Streamlit Community Cloud

---

## 📂 Repository Structure

```text
├── app.py              # Main application logic & UI orchestration
├── requirements.txt    # Python dependencies
├── .gitignore          # Git exclusion rules (Secures API keys)
└── README.md           # Documentation
