FROM nginx:latest
COPY ./nginx.conf /etc/nginx
COPY ./ssl /etc/nginx/ssl/
RUN openssl dhparam -out /etc/nginx/dhparam.pem 2048
