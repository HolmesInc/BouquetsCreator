FROM python:3.7

WORKDIR /usr/src/app

COPY . .

# run the command
CMD ["python", "./run.py"]
