FROM python:3.8.0-buster

# Make a dir for our application
WORKDIR /app

# Install dependecies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code
COPY /app .

# Run the application
CMD ["python3", "bot.py"]