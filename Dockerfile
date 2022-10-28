FROM python:3.7

MAINTAINER Asklv bbemailspider@163.com

WORKDIR /HUST

RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

WORKDIR /HUST
RUN git clone https://github.91chi.fun/https://github.com/IRONICBo/simple-timeline.git

WORKDIR /HUST/simple-timeline
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
