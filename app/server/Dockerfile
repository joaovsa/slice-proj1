#from https://hub.docker.com/r/jcdemo/flaskapp/dockerfile
# python:alpine is 3.{latest}
FROM python:alpine 

LABEL maintainer="Jeeva S. Chelladhurai"

#instala dependencias pip
RUN pip install flask
RUN pip install flask_restful

#copia o arquivo do servidor p/ o container
COPY AppServer.py /src/

EXPOSE 5000

#executa a arquivo copiado
ENTRYPOINT ["python", "/src/AppServer.py"]