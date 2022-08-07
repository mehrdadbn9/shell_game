FROM python:3.10

WORKDIR /app
COPY . .
RUN python3 -m venv /app/venv
RUN . venv/bin/activate
ADD requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#ADD main.py /

COPY . .
CMD [ "python", "./manu.py" ]