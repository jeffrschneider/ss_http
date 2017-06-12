FROM brombach/py23

WORKDIR /app
ADD nltk_data /root/nltk_data
ADD . /app

RUN pip2 install cython nltk

EXPOSE 8080

CMD ["python3", "ss_http.py"]