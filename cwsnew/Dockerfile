FROM python:3.9.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV WEB_PORT 8000

RUN apk update  \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

#RUN python -m pip install -U --force-reinstall pip
COPY requirments.txt .
RUN pip install -r requirments.txt

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]