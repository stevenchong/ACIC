FROM ubuntu:latest
MAINTAINER Steven Chong <stevenchong@email.arizona.edu>
RUN apt-get update
RUN apt-get -y install sudo
RUN apt-get -y install python
RUN sudo apt-get -y install libhdf5-serial-dev
RUN sudo apt-get -y install netcdf-bin
RUN sudo apt-get -y install libnetcdf-dev
RUN sudo apt-get install -y python-pip python-dev build-essential
RUN sudo pip install --upgrade pip
RUN sudo pip install h5py
RUN HDF5_DIR=/usr/local/hdf5
RUN sudo pip install netcdf4
RUN sudo pip install plotly
ADD hw8.py hw8.py
VOLUME /data  
