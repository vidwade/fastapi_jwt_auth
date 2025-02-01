# FastAPI JWT Authentication

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A robust JWT authentication system built with FastAPI, featuring both symmetric (HS256) and asymmetric (RS256) JWT signing algorithms.

## 🌟 Features

- User registration and authentication
- JWT token generation and validation
- Secure password hashing with bcrypt
- Protected routes with JWT authentication
- SQLite database integration
- Comprehensive API documentation with Swagger UI
- Both symmetric (HS256) and asymmetric (RS256) JWT implementations

## 🔍 Branch Information

- `symmetric-jwt`: Implementation using HS256 (HMAC with SHA-256)
- `asymmetric-jwt`: Implementation using RS256 (RSA Signature with SHA-256)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/vidwade/fastapi_jwt_auth.git
cd fastapi_jwt_auth
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. For asymmetric JWT (RS256), generate keys:
```bash
python generate_keys.py
```

## 🚀 Quick Start

1. Start the server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔑 API Endpoints

### Authentication
- `POST /signup` - Register a new user
- `POST /token` - Login and get access token

### Protected Routes
- `GET /users/me` - Get current user profile
- `GET /protected` - Example protected route

## 📝 Example Usage

### User Registration
```bash
curl -X POST "http://localhost:8000/signup" \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "test@example.com", "password": "secretpassword"}'
```

### Login
```bash
curl -X POST "http://localhost:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=testuser&password=secretpassword"
```

### Access Protected Route
```bash
curl -X GET "http://localhost:8000/protected" \
     -H "Authorization: Bearer your_access_token"
```

## 🔐 Security Features

### Symmetric JWT (HS256)
- Uses a single secret key for both signing and verification
- Suitable for single-server applications
- Simple to implement and manage

### Asymmetric JWT (RS256)
- Uses public/private key pair
- Private key signs tokens, public key verifies them
- Better for distributed systems and microservices
- More secure for token verification across multiple services

## 📚 Project Structure
```
fastapi_jwt_auth/
│
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   └── users.py
│   ├── core/
│   │   ├── security.py
│   │   └── deps.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── main.py
│   ├── config.py
│   └── database.py
│
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Environment Variables

Create a `.env` file in the root directory:
```env
# For symmetric JWT (HS256)
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./test.db
ACCESS_TOKEN_EXPIRE_MINUTES=30

# For asymmetric JWT (RS256)
PRIVATE_KEY_PATH=private_key.pem
PUBLIC_KEY_PATH=public_key.pem
```

## 🧪 Running Tests

```bash
pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ Support

If you found this helpful, please consider giving it a ⭐️!
