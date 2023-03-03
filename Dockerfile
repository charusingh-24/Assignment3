FROM python:3.9.12


# RUN pip install --upgrade pip

# WORKDIR /app
# ADD requirements.txt /app/

# RUN pip install -r requirements.txt

# ADD airflow /app/

# RUN pip install -r requirements.txt
#
#COPY ./Login.py ./requirements.txt  /app/
#
#COPY pages /app/pages
#
#COPY sql_utils/sql_credentials.py ./sql_goes.py ./sql_nexrad.py ./utils_goes_API.py ./utils_nexrad_API.py /app/
#
#COPY ./lat_long.py ./meta.db ./nexrad.csv /app/
#WORKDIR /app
#
#COPY ./Login.py ./requirements.txt  /app/
#
#COPY pages /app/pages
#
#COPY ./sql_credentials.py ./sql_goes.py ./sql_nexrad.py ./utils_goes_API.py ./utils_nexrad_API.py /app/
#
#COPY ./lat_long.py ./meta.db ./nexrad.csv /app/

#CMD ["streamlit", "run", "Login.py","--server.port","8091"]
# Install Airflow and its dependencies
# RUN pip install apache-airflow

# # Initialize the Airflow database
# EXPOSE 8000

# # Start the Airflow web server
# CMD exec gunicorn --bind :$8000 --workers 1 --threads 8 --timeout 0 main:app