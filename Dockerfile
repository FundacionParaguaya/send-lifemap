FROM ubuntu:18.10
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
RUN apt-get install -y wget
RUN wget https://builds.wkhtmltopdf.org/0.12.1.4/wkhtmltox_0.12.1.4-1.xenial_amd64.deb
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]