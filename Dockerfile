FROM python:3.12-slim

COPY . .

RUN pip instal -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "61000"]