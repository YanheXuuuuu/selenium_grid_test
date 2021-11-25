FROM ubuntu:18.04

RUN apt-get update && apt-get install firefox chromium-browser chromium-chromedriver python3 python3-pip -y && \
    pip3 install --upgrade pip && pip3 install selenium pandas numpy bs4




ENV APP_HOME /content
WORKDIR $APP_HOME
COPY . ./
CMD ["python3","/content/test.py"]
