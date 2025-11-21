# Vulnerable Hello World App (for Security Testing)

⚠️ This app is intentionally insecure. Use ONLY for security tool testing.

## Run Locally
docker build -t vuln-app .
docker run -p 80:80 vuln-app

## Endpoints
GET / → XSS test
GET /user?name=test → SQL Injection test
