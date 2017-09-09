FROM python:3-alpine
RUN apk update && apk add bash && apk add curl
WORKDIR /usr/src/
COPY . .
RUN pip install -r ./app/requirements.txt
EXPOSE 5000
CMD ["python", "app/sqs.py"]
