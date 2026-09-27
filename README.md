# 🎵 AI Song Arrangement Assistant

An intelligent, end-to-end system that analyzes song lyrics and recommends a complete musical arrangement — including instruments, band templates, genre, mood, dynamics, and explainable rationale — all powered by NLP and rule-based AI.

---

## Features

- **Lyric Parsing & Section Tagging** — Automatically detects verse, chorus, bridge, pre-chorus, and outro sections
- **Emotion Classification** — Multi-emotion detection (joy, sadness, anger, fear, love, etc.) per section
- **Theme Extraction** — Multi-label theme tagging (love, loss, journey, rebellion, nostalgia, etc.)
- **Valence/Arousal Mapping** — Maps lyrics to a 2D mood space (energy × positivity)
- **Genre Prediction** — Predicts primary and secondary genre with confidence scores
- **Instrument Recommendation** — Recommends instruments with roles and playing notes
- **Dynamics Prediction** — Suggests playing style (fingerpicked, strummed, arpeggiated, etc.)
- **Band Templates** — Matches to preset arrangements (Acoustic Trio, Pop Band, Lo-Fi, Cinematic, Fusion)
- **Explainability** — Explains why each instrument was chosen and highlights key lyric lines

---

## Project Structure

```
ai-song-arrangement-assistant/
├── backend/         # FastAPI Python backend
│   ├── src/         # Core NLP + prediction modules
│   ├── api/         # REST API routes
│   ├── data/        # Lexicons and datasets
│   ├── models/      # Saved model checkpoints
│   ├── tests/       # Unit tests
│   └── scripts/     # Training and data scripts
└── frontend/        # React (Vite) frontend
    └── src/         # Components, pages, hooks
```

---

## Quick Start

### Windows One-Click (Recommended)
1. Run `setup.bat` in the root folder to create the local Python virtual environment, install requirements, and install frontend dependencies.
2. Run `start.bat` to launch both backend and frontend servers simultaneously and open the web app in your browser.

---

### Manual Setup

#### Prerequisites
- Python 3.9+ (including Python 3.12 and 3.13)
- Node.js 18+

#### Backend Setup

```bash
cd backend

# Create and activate virtual environment
python -m venv env
# Windows:
.\env\Scripts\activate
# Linux/Mac:
source env/bin/activate

# Install dependencies (isolated in virtualenv)
pip install -r requirements.txt

# Run the test suite
pytest

# Run the API server
uvicorn api.main:app --reload --port 8000
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies (installed locally into ./node_modules)
npm install

# Start the dev server
npm run dev
```

The frontend runs at `http://localhost:5173` and proxies API requests to `http://localhost:8000`.

### Docker (optional)

```bash
docker-compose up --build
```

---

## API Reference

### `POST /arrange`

**Request:**
```json
{
  "lyrics": "string (required)",
  "title": "string (optional)",
  "key": "string (optional, e.g. 'C major')",
  "tempo_hint": "number (optional, BPM)"
}
```

**Response:** Full arrangement JSON with mood, genre, instruments, dynamics, template, rationale, and highlighted lyrics.

---

## Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | FastAPI, Pydantic, NLTK, TextBlob   |
| ML        | scikit-learn, NumPy, rule-based NLP |
| Frontend  | React 18, Vite, Vanilla CSS         |
| DevOps    | Docker, Docker Compose              |

---

## License

MIT License. See [LICENSE](LICENSE).
