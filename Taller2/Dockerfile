FROM python:3.10
RUN mkdir /work
WORKDIR /work
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install feast -U -q
RUN pip install Pygments -q
RUN pip install apache-beam[interactive]==2.45.0
RUN pip install jupyter==1.0.0 -U && pip install jupyterlab==3.6.1
EXPOSE 8889
ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
