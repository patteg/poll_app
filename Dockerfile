FROM tiangolo/uwsgi-nginx-flask:python3.6
ADD ./app/requirements.txt .
RUN pip install -r requirements.txt
COPY ./app /app
EXPOSE 3035