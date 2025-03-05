# Use the official Ubuntu base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /data

# Install system dependencies (Python, pip, and build essentials)
RUN apt-get update && apt-get install -y \
    wget \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    && apt-get clean

# Install the wacz library using pip with --break-system-packages
RUN pip3 install wacz --break-system-packages

# Set the default command to bash
CMD ["bash"]
