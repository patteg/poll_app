FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN apt-get update && apt-get install -y
ADD ./app/requirements.txt .
RUN pip install -r requirements.txt
COPY ./app /app
EXPOSE 3035