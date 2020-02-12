FROM python:3.7

RUN mkdir /server3
COPY . /server3
WORKDIR /server3

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "server3.py" ]