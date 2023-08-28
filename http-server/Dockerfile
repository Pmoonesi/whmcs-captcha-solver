FROM tensorflow/tensorflow

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY code /app/code

CMD ["python3", "/app/code/main.py"]
