FROM python:3.7

RUN mkdir /server2
COPY . /server2
WORKDIR /server2

RUN pip install -r requirements.txt

EXPOSE 4567

ENTRYPOINT [ "python" ]

CMD [ "server2.py" ]