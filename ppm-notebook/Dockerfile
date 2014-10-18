FROM ubuntu:latest

MAINTAINER Samuel Jones

# scikits.audiolab needs dev stuff
# clean-up unecessary packages once installed.

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get --no-install-recommends install --yes \
    ipython-notebook python-pip \
    python-numpy python-scipy python-matplotlib python-pandas python-sympy \
    python-sklearn hdf5-tools libhdf5-serial-dev python-h5py python-tk \
    build-essential python-dev libsndfile1-dev libsndfile1 git wget \
    pandoc && \
  pip install scikits.audiolab && \
  pip install pygments && \
  apt-get remove --yes libsndfile-dev python-dev build-essential && \
  apt-get autoremove --yes && \
  apt-get autoclean --yes && \
  pip install nugridpy vos && \
  pip install https://github.com/jakevdp/JSAnimation/archive/master.zip

# set the lang to avoid issues
RUN apt-get install -y language-pack-en
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

EXPOSE 8080
RUN useradd -d /home/ppm -m -c "PPM User" ppm
ADD ./run-ipython-notebook.bash /home/ppm/
RUN  chmod +x /home/ppm/run-ipython-notebook.bash && \ 
     mkdir -p /home/ppm/CADC/NuGrid && \
     chown -R ppm:ppm /home/ppm
USER ppm
ENV HOME /home/ppm
RUN ipython profile create nbserver
ADD startup.ipy /home/ppm/.ipython/profile_nbserver/startup/startup.ipy
ADD nb_tools.py /home/ppm/.ipython/profile_nbserver/startup/nb_tools.py
ADD ppm.py /home/ppm/ppm.py
WORKDIR /home/ppm
CMD /home/ppm/run-ipython-notebook.bash
