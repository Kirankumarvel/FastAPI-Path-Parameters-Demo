# FastAPI Path Parameters Demo

A FastAPI application demonstrating basic path parameters and route ordering concepts.

---

## 🚀 Features

- **FastAPI** framework with automatic OpenAPI documentation
- Demonstrates path parameters with dynamic routing
- Shows the importance of route ordering in FastAPI
- Interactive API documentation at `/docs` and `/redoc`
- Python 3.7+ compatibility
- Virtual environment setup for isolation

---

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kirankumarvel/fastapi-path-parameters-demo.git
   cd fastapi-path-parameters-demo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Dependencies

- `fastapi` - The web framework for building APIs
- `uvicorn` - ASGI server for running FastAPI applications

To generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## 🚀 Running the Application

1. **Start the development server**
   ```bash
   uvicorn main:app --reload --reload-exclude venv
   ```

2. **Access the application**
   - API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 API Endpoints

### GET `/users/me`
Returns information about the current user.

**Response:**
```json
{
  "user_id": "The current awesome user"
}
```

---

### GET `/users/{user_id}`
Returns information about a specific user by ID.

**Path Parameters:**
- `user_id` (string): The ID of the user to retrieve

**Example:**
```bash
curl http://127.0.0.1:8000/users/42
```

**Response:**
```json
{
  "user_id": "42"
}
```

---

## 🎯 Key Concept: Route Ordering

FastAPI matches routes in the order they are defined. This is crucial when you have:

1. **Fixed paths** (like `/users/me`)
2. **Parameterized paths** (like `/users/{user_id}`)

**Correct order:**
```python
@app.get("/users/me")        # Fixed path first
@app.get("/users/{user_id}") # Parameterized path second
```

**Why this matters:**
- `/users/me` → matches the fixed route
- `/users/42` → falls through to the parameterized route
- If reversed, `/users/me` would be treated as a user_id parameter

---

## 🧪 Testing the API

Test the different endpoints:

1. **Current user endpoint:**
   ```bash
   curl http://127.0.0.1:8000/users/me
   ```

2. **Specific user endpoint:**
   ```bash
   curl http://127.0.0.1:8000/users/42
   curl http://127.0.0.1:8000/users/Kumar
   ```

3. **Interactive testing:** Use the Swagger UI at `/docs` to test both endpoints.

---

## 📁 Project Structure

```
fastapi-path-parameters-demo/
├── main.py          # Main application file
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
└── venv/            # Virtual environment (gitignored)
```

---

## 🔧 Code Explanation

### `main.py`
```python
from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Fixed route - must come first!
@app.get("/users/me")
async def read_current_user():
    return {"user_id": "The current awesome user"}

# Parameterized route - comes after fixed routes
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

---

## 🎓 Learning Points

1. **Path Parameters**: Use `{parameter_name}` in route paths
2. **Type Hints**: FastAPI uses them for validation and documentation
3. **Route Order**: Fixed routes must come before parameterized routes
4. **Automatic Docs**: FastAPI generates interactive documentation automatically

---

## 🔧 Troubleshooting

### Common Issues:

1. **Route ordering problems**
   - Ensure fixed routes (`/users/me`) come before parameterized routes (`/users/{user_id}`)

2. **Module not found error**
   - Ensure you're in the correct directory
   - Check that virtual environment is activated

3. **Reload issues**
   ```bash
   uvicorn main:app --reload --reload-exclude venv
   ```

---

## 📚 Learning Resources

- [FastAPI Path Parameters Documentation](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI Route Ordering](https://fastapi.tiangolo.com/tutorial/path-params/#order-matters)
- [Uvicorn Documentation](https://www.uvicorn.org/)

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- Uvicorn team for the ASGI server
- Python community for ongoing support
