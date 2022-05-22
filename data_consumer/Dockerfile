FROM python:3.10.4

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "web_socket.py" ]