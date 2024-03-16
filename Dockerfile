# Use Ubuntu as the base image
FROM ubuntu:latest

# Update package lists and install necessary packages
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip git

# Update pip to the latest version
RUN python3 -m pip install --upgrade pip

# Print Python and pip versions for verification
RUN python3 --version && pip --version

RUN pip install git+https://bitbucket.org/taucgl/cgal-python-bindings/src/master/