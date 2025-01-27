FROM python:3.11

RUN pip install uv

WORKDIR /workspace

COPY . /workspace
