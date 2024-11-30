FROM python:3.12

WORKDIR /container
COPY . /container
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "bot.py"]