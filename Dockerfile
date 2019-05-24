FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN wget https://builds.wkhtmltopdf.org/0.12.1.4/wkhtmltox_0.12.1.4-1.xenial_amd64.deb
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]