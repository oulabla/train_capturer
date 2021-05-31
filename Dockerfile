FROM tiangolo/uwsgi-nginx-flask:python3.8
ADD ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python main.py
