FROM python:3.7
RUN mkdir -p /app
WORKDIR /app
RUN pip install pipenv
COPY Pipfile* .
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
COPY ./app.py .
CMD python app.py
