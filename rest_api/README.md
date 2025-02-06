# Personal Info API

## 📋 **Project Overview**
The Personal Info API provides a simple and secure way to manage user information, including the ability to create, update, retrieve, and delete user records. The project uses **FastAPI**, **SQLAlchemy**, and **SQLite** for database management and is fully containerized with **Docker** and **Docker Compose** for deployment.

---

## 📂 **Folder Structure**
```
.
├── app
│   ├── __init__.py
│   ├── main.py         # FastAPI entry point for API routes
│   ├── models.py        # SQLAlchemy models for database tables
│   ├── crud.py          # CRUD operations for the User model
│   ├── schemas.py       # Pydantic models for request/response validation
│   ├── auth.py          # API key authentication logic
│   └── database.py      # Database setup and session management
├── docker-compose.yml  # Docker Compose configuration
├── Dockerfile          # Docker configuration for the application
├── requirements.txt    # Python package dependencies
├── docker-start.sh     # Import data and start server
└── README.md           
```

---

## ⚙️ **Workflow**
1. **Database Initialization:**  
   Table is automatically created at the startup.

2. **API Request Flow:**  
   - Request validation is handled by Pydantic models (`schemas.py`).
   - CRUD operations interact with the SQLite database through `crud.py`.
   - Exception and Errors are handled via custom exception handlers in FAST API `main.py`.

## 🚀 **Deploying the Application**
To deploy the application using Docker Compose, run:
```bash
docker-compose up --build
```
This command will:
- Build the Docker image
- Start the API service
- Mount the SQLite database as a volume to persist data

---

## 📡 **Using the API Endpoints**
After deployment, the API will be accessible at `http://localhost:8000`.

### **Endpoints**
| Method | Endpoint      | Description                        | Request Body  |
|--------|---------------|------------------------------------|---------------|
| GET    | `/user/{id}`   | Get a user by ID                   | None         |
| POST   | `/user`        | Create or update a user by ID      | JSON         |
| DELETE | `/user/{id}`   | Delete a user by ID                | None         |

### **Example Request**
#### Create or Update a User
```http
POST http://localhost:8000/user
Content-Type: application/json
API-Key: your-api-key
```
**Request Body:**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "gender": "Male",
  "ip_address": "192.168.1.1",
  "country_code": "US"
}
```

---

## 📄 **API Documentation**
Swagger UI is automatically available at:
```
http://localhost:8000/docs
```
Alternative OpenAPI documentation is available at:
```
http://localhost:8000/redoc
```

---

## 🛡️ **Security**
API key authentication is required for all routes. Provide the key in the request header:
```
API-Key: hackmeifyoucan
```