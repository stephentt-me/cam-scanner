FROM python:3.7-stretch

# Install preview poetry
RUN wget https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py
RUN python get-poetry.py --preview --yes

# Application Environment
WORKDIR /app
ADD pyproject.toml poetry.lock ./
RUN $HOME/.poetry/bin/poetry export -f requirements.txt --dev --without-hashes
RUN pip install -r requirements.txt

ADD . .
EXPOSE 5000
CMD make run