FROM python:3.9.12

<<<<<<< Updated upstream
WORKDIR /app

COPY ./Login.py ./requirements.txt  /app/

COPY pages /app/pages

COPY sql_utils/sql_credentials.py ./sql_goes.py ./sql_nexrad.py ./utils_goes_API.py ./utils_nexrad_API.py /app/

COPY ./lat_long.py ./meta.db ./nexrad.csv /app/
=======
#RUN chmod -R a+w /usr/local/lib/python3.7/site-packages
#WORKDIR /app
#
#COPY ./Login.py ./requirements.txt  /app/
#
#COPY pages /app/pages
#
#COPY ./sql_credentials.py ./sql_goes.py ./sql_nexrad.py ./utils_goes_API.py ./utils_nexrad_API.py /app/
#
#COPY ./lat_long.py ./meta.db ./nexrad.csv /app/
>>>>>>> Stashed changes

RUN pip install -r requirements.txt
#
#EXPOSE 8091
#
#CMD ["streamlit", "run", "Login.py","--server.port","8091"]