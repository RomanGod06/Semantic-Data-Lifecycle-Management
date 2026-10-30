# Semantic Data Lifecycle Management 🧠💾

**Context-Aware Local Storage Optimization Using Edge NLP**

This repository contains the prototype for a Zero-Trust, AI-driven local data management system. It replaces static, timer-based file deletion (e.g., "delete files older than 30 days") with intelligent, on-device semantic classification to identify dormant data, hidden caches, and stale session tokens without compromising user privacy.

## 🚀 The Core Problem
Operating systems currently manage local storage using rigid heuristics (file age, extension, size). They lack semantic understanding, leading to the aggressive deletion of important, rarely used files, or the dangerous hoarding of vulnerable, forgotten web session debris. Cloud-based AI solutions to this problem introduce severe data privacy risks.

## 💡 The Solution
This project leverages **TinyML and Edge NLP** to embed and classify files locally. By generating mathematical vector representations of file contents and metadata on the device, the system clusters and categorizes data by its actual utility and meaning, completely offline.

## 🛠️ Tech Stack (Prototype)
*   **Language:** Python 3.10+
*   **NLP Model:** `all-MiniLM-L6-v2` (via `sentence-transformers`) - A lightweight, quantized embedding model running entirely on the CPU.
*   **Vector Database:** `ChromaDB` - For local, offline storage of document embeddings.
*   **User Interface:** `Streamlit` - For the interactive dashboard and user-in-the-loop feedback.

## 📅 Sprint Roadmap

### Day 1: The Core Engine (AI & Storage)
- [x] Repository initialization and environment setup.
- [ ] Generate synthetic local data (simulated AppData, session tokens, critical documents).
- [ ] Implement the `sentence-transformers` embedding script.
- [ ] Initialize local `ChromaDB` and execute semantic vector searches.

### Day 2: The Interface & Integration (UI)
- [ ] Build the `Streamlit` web interface.
- [ ] Connect the UI to the ChromaDB backend.
- [ ] Implement the "Archive/Delete" action workflows.
- [ ] Record the final demonstration for the seminar presentation.

## ⚙️ Setup & Installation
*(Instructions to be updated as the environment is configured)*

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/semantic-data-lifecycle.git
   cd semantic-data-lifecycle
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   ```
3. Install dependencies (coming soon):
   ```bash
   pip install -r requirements.txt
   ```