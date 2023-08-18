FROM python:3.8-buster as base
WORKDIR /data
COPY . .
RUN python /data/setup.py install
RUN pip install -r requirements.txt
RUN pip install .