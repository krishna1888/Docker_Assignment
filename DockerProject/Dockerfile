# Use Python as base image
FROM python:3.9-slim

# Create directories
RUN mkdir -p /home/data/output /home/app/scripts

# Copy script and data files into the container
COPY scripts/script.py /home/app/scripts/script.py
COPY data/IF-1.txt /home/data/IF-1.txt
COPY data/AlwaysRememberUsThisWay-1.txt /home/data/AlwaysRememberUsThisWay-1.txt

# Set working directory
WORKDIR /home/app/scripts

# Run script
CMD ["python", "script.py"]
