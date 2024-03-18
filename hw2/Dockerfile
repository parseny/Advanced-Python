FROM python:3.10

RUN apt-get update && \
    apt-get install -y --no-install-recommends texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra && \
    rm -rf /var/lib/apt/lists/*

RUN pip install latexgen==0.3

WORKDIR /app

COPY run.sh /app/
COPY task2.py /app/
COPY artefacts/Lenna.png /app/artefacts

RUN chmod +x /app/run.sh