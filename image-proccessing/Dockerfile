FROM python:3.6-jessie

# Install preview poetry
RUN wget https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py
RUN python get-poetry.py --preview --yes

WORKDIR /app

# Application Environment
ADD pyproject.toml poetry.lock ./
RUN $HOME/.poetry/bin/poetry export -f requirements.txt --dev --without-hashes
RUN pip install -r requirements.txt

ADD . .
EXPOSE 50051
CMD make run