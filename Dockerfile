FROM python:3
WORKDIR /webapp-change-bg-color
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "./app.py" ]
