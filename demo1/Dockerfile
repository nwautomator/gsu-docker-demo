FROM tensorflow/tensorflow:2.1.0-gpu-py3-jupyter
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -U numpy scipy jupyter jupyterlab matplotlib seaborn keras scikit-learn Pillow
VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888
CMD jupyter lab --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token= --NotebookApp.allow_origin='*'
