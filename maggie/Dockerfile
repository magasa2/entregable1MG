FROM python:3.9.7
RUN apt-get update

COPY requirements.txt /app
COPY entregable1.py /app

RUN mkdir "Lisa Simpson"
RUN mkdir "Homer Simpson"

RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python" , "entregable1.py"]
