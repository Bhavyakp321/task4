FROM python:3.9

WORKDIR /app

COPY exp.py .

RUN pip install requests

CMD ["python", "exp.py"]
