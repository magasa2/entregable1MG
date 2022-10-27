FROM python:3.9.7
RUN apt-get update

COPY requirements.txt /lisa
COPY entregable2.py /lisa


RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python" , "entregable2.py"]