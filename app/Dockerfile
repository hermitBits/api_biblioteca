FROM python:3.9

WORKDIR /

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN apt-get update \
  && apt-get -y install netcat gcc \
  # mysql dependencies
  && apt-get -y install default-libmysqlclient-dev build-essential \
  && apt-get clean

COPY . .

WORKDIR /usr/src/app/api_biblioteca


CMD [ "./entry_point.sh" ]