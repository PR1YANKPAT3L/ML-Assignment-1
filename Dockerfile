FROM python:2.7

RUN apt-get update
WORKDIR /root
RUN mkdir assignment_1
COPY ./ ./assignment_1/
RUN cat ./assignment_1/requirements.txt
RUN pip install -qr ./assignment_1/requirements.txt

ENTRYPOINT ["python", "./assignment_1/app.py"]
EXPOSE 5000