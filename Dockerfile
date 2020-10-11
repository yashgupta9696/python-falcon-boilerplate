#FROM python:alpine
FROM python:3.8
EXPOSE 8000

# Add demo app
RUN mkdir /cloud_api
COPY . /cloud_api
WORKDIR /cloud_api

# Install gunicorn & falcon
RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "etc/cloud_api/gunicorn.conf", "cloud_api.main:app"]
