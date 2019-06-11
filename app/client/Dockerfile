#from https://hub.docker.com/r/jcdemo/flaskapp/dockerfile
# python:alpine is 3.{latest}
FROM python:alpine 

LABEL maintainer="Jeeva S. Chelladhurai"

#instala dependencias pip
RUN pip install flask
RUN pip install flask_restful
RUN pip install requests
RUN pip install docker 

#copia o arquivo do servidor p/ o container
COPY AppClient.py /src/

#flag -u proporciona saída no docker log
CMD [ "python", "-u", "/src/AppClient.py" ]