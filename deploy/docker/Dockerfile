FROM python:3.7.6
MAINTAINER franplk
LABEL version=1.0 description=PhraseSimilarity

# Install Python Packages
WORKDIR /root
ADD requirements-web.txt requirements.txt
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
