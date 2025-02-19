FROM python:3
WORKDIR /workdir
COPY . .

RUN pip install --upgrade pip && pip install \
    black \
    mypy \
    pytest
