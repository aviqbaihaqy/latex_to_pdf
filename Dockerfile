FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . /app
RUN apt-get update -y && apt install -y \
    texlive-latex-base
    
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["python", "app.py"]
