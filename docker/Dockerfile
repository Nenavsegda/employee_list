FROM python:3.10-bullseye

RUN mkdir -p var/www/employee_list
COPY . var/www/employee_list/
RUN cd var/www/employee_list && pip install --no-cache-dir -r requirements.txt

WORKDIR var/www/employee_list
RUN apt-get update && apt-get install -y curl
RUN curl -O https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x wait-for-it.sh

RUN chmod +x docker/docker-entrypoint.sh

ENTRYPOINT ["docker/docker-entrypoint.sh"]
