FROM python:2
WORKDIR /app
COPY package.json /app
COPY . /app
RUN pip install flask
RUN pip install configparser
CMD python server.py
EXPOSE 3000