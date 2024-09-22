# IoT-based Smart Home Dashboard

## Overview
This project is a dashboard for monitoring and controlling smart home devices such as lights and thermostats. It showcases practical use cases for IoT and cloud integration using FastAPI for the backend and React for the frontend.

## Tech Stack
- **Backend:** FastAPI
- **Frontend:** React

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js and npm
- Docker (optional, for containerization)

### Installation

#### Backend
1. Navigate to the backend folder:
   ```bash
   cd backend
    ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate # Linux
   venv\Scripts\activate # Windows
   ```

3. Install the dependencies:
   ```bash
    pip install -r requirements.txt
    ```

#### Frontend
1. Navigate to the frontend folder:
   ```bash
   cd frontend
    ```
2. Install the dependencies:
    ```bash
    npm install
    ```

### Usage
1. Start the backend server:
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

2. Start the frontend server:
   ```bash
    cd frontend
    npm start
    ```

3. Access the Application:
    - Open your browser and go to http://localhost:3000 for the frontend.
    - Access the API documentation at http://127.0.0.1:8000/docs for the FastAPI backend.

### Running with Docker
1. Running application with docker-compose
    ```bash
    docker-compose up
    ```
2. Access the Application:
   - Open your browser and go to http://localhost:3000 for the frontend.
   - Access the API documentation at http://127.0.0.1:8000/docs for the FastAPI backend.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.