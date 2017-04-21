# narenm/dev-env is based on ubuntu:16.04
# Git location of dev-env
#   - https://github.com/naren-m/Dockerfiles/tree/master/dev-env
FROM narenm/py3
MAINTAINER Naren Mudivarthy <narenuday595@gmail.com>

WORKDIR /webapp 

# Add requirements.txt
ADD requirements.txt /webapp
 
# Install uwsgi Python web server
RUN pip install uwsgi

# Install app requirements
RUN pip3 install -r requirements.txt
 
# Create app directory
ADD . /webapp
 
# Set the default directory for our environment
ENV HOME /webapp
WORKDIR /webapp

ENTRYPOINT ["python"]
CMD ["app.py"]

# CMD [ "python", "./app.py" ]


