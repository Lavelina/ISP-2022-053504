FROM python:3.8.2-alpine

WORKDIR ../ISP-1

COPY . .

CMD ["python", "main.py"]