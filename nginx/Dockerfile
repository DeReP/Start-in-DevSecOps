FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY ./templates/nginx.conf.template /etc/nginx/templates/default.conf.template