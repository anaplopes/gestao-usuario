# Use the Nginx image
FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

RUN echo "uwsgi_read_timeout 3600s;" > /etc/nginx/conf.d/custom_timeout.conf
# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/