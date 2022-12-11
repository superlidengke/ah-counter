# cd <Current_Dir>
# docker build -t python_ffmpge .   build a docker image with this Dockerfile
# docker run -it python_ffmpge bash  run bash command of the image
# docker tag b56dfd5c33e5 Karl998800/python_ffmpeg  replace the id with real image id
# docker push karl998800/python_ffmpeg
FROM python:3.11
LABEL description="An image with python3.11 and ffmpeg for unit test"
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg