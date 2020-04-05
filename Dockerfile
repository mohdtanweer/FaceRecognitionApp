FROM python:3.6.3

# install Python modules needed by the Python app
COPY . /face_match
WORKDIR /face_match

RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "main.py"]