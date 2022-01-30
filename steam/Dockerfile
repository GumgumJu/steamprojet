FROM python:3.8

RUN mkdir /app/

WORKDIR /app/

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt

CMD ["scrapy","runspider","steam.py","-o","data5.json"]