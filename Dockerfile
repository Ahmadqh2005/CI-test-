# 1. Base image with lightweight Python 3.10 runtime
FROM python:3.10-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy dependencies list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code
COPY . .

# 5. Default command to run when the container starts
CMD ["python", "calculator.py"]
