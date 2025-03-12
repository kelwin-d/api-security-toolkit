# api-security-toolkit
API Security Toolkit

This project is a lightweight **FastAPI-based API Security Toolkit** designed to secure APIs using:

- **Rate Limiting** to protect against abuse
- **JWT Authentication** for secure token-based access
- **Input Validation** for enhanced data integrity

## 🚀 Features
✅ Secure Endpoints with JWT Authentication  
✅ Rate Limiting to prevent DDoS attacks  
✅ Input Validation using Pydantic  
✅ Token Generation for controlled API access  

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kelwin-d/api-security-toolkit.git
   cd api-security-toolkit

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn python-jose

3. Run the application:
   ```bash
   uvicorn security_toolkit:app --reload

## 🔐 Endpoints

POST /token - Generate a secure JWT token

GET /secure-data - Access secured data (requires token)

POST /submit - Submit validated user data

## 📄 License

This project is licensed under the MIT License.
