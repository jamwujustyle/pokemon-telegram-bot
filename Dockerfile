FROM python

WORKDIR /container
COPY . /container

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "bot.py"]