# SotonHack 2026


## Setup and Running It Yourself

### Project Setup


To set up the backend:
1. `cd backend`
2. `uv sync`

To set up the frontend:
1. `cd frontend`
2. `npm install`

### Running the App
You need 2 terminals, one for the fastapi server and one for the frontend.

1. Backend terminal (from project root directory):
  ```uv run --project backend uvicorn backend.main:app --reload```

2. Frontend terminal (from `frontend` directory):
  ```npm run dev```

3. Go to [localhost port 5173](http://localhost:5173/) on a browser to see the web app
