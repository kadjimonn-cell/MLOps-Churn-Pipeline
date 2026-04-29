# training script for school project
# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Train model (VERY IMPORTANT)
RUN python src/train.py

# Run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
docker build -t churn-app .
docker run -p 8000:8000 churn-app
