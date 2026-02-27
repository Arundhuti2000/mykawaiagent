# UI for My Kawai Agent

This directory contains a React-based UI for the My Kawai Agent CLI.

## Structure

- `backend/`: A minimal Flask server that interfaces with the existing `main.py` logic.
- `frontend/`: A React + Vite application for the user interface.

## Prerequisites

- Python 3.x
- Node.js and npm

## Setup & Running

### 1. Start the Backend

Navigate to the `ui/backend` directory and install dependencies:

```bash
cd ui/backend
pip install -r requirements.txt
```

Run the server:

```bash
python server.py
```

The backend runs on `http://localhost:5000`.

### 2. Start the Frontend

Open a new terminal, navigate to the `ui/frontend` directory, and install dependencies:

```bash
cd ui/frontend
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will run on `http://localhost:5173`. Open this URL in your browser.

## key Notes

- The UI uses the same `GEMINI_API_KEY` from your root `.env` file via the backend.
- The CLI outputs and logic remain strictly unchanged as requested.
