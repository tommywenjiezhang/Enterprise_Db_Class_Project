FROM jupyter/datascience-notebook
WORKDIR /notebook
USER root
RUN apt-get update && \
apt-get install -y --no-install-recommends apt-utils \
curl \
gnupg \
unixodbc-dev \
freetds-dev \
freetds-bin \
tdsodbc
ADD etc_freetds_freetds.conf /etc/freetds/freetds.conf
ADD etc_odbc.ini /etc/odbc.ini
ADD etc_odbcinst.ini /etc/odbcinst.ini
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
&& curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list\
&& sudo apt-get update \
&& sudo ACCEPT_EULA=Y apt-get -y --no-install-recommends install msodbcsql17 \
&& sudo apt-get update \
&& sudo apt-get install freetds-dev \
# && sudo ACCEPT_EULA=Y install mssql-tools \
# echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
# echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
# /bin/bash -c /root/.bashrc \
&& apt-get clean


COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 8888

