FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev libmysqlclient-dev git

# Clone the Flask app code from git
# RUN git clone https://github.com/var-co-jp/hackathon-begginers-sample.git /app
COPY ./hackathon-begginers-sample /app

# Set the working directory to the app directory
WORKDIR /app

# Install the required Python packages
# COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Set environment variables for MySQL
ENV MYSQL_DATABASE=chatapp
ENV MYSQL_USER=testuser
ENV MYSQL_PASSWORD=testuser
ENV MYSQL_HOST=localhost

# Copy the MySQL configuration file to the container
# COPY my.cnf /etc/mysql/conf.d/

# Expose the port on which the app will run
EXPOSE 5000

# Start the Flask app
CMD ["python3", "app.py"]

