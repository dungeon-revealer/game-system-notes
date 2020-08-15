FROM python:3

RUN mkdir data

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "validate.py", "data"]
