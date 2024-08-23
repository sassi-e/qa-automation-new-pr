FROM python:3.11-alpine

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt

 

RUN apk update \
&& apk add --no-cache curl build-base unzip python3-dev libaio-dev xvfb zip libaio libx11 vim rpm2cpio cpio dos2unix wget postgresql-client postgresql-dev gcc libc-dev linux-headers musl-dev zlib zlib-dev openldap-dev openssl screen \
&& pip install --upgrade pip \
&& pip cache purge \
&& pip install --prefix=/install --no-warn-script-location -r /requirements.txt \
&& find /install \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
&& runDeps="$( \
        scanelf --needed --nobanner --recursive /install \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
&& apk add --virtual .rundeps $runDeps

 

RUN apk add --no-cache openssl

RUN apk add --no-cache screen

 

FROM python:3.11-alpine

# Copy python and alpine dependencies

COPY --from=0 /install /usr/local

 

RUN apk add --no-cache curl libpq libldap openssh-client

RUN curl https://bootstrap.pypa.io/get-pip.py | python

 

RUN pip install --upgrade pip

RUN pip install pyvirtualdisplay

RUN pip install openpyxl allure_behave

RUN apk add --no-cache screen

RUN apk --no-cache add openjdk11

RUN pip uninstall --yes oscrypto && pip install oscrypto


RUN mkdir /code

COPY . /code/

WORKDIR /code

 

ENV LANG C.UTF-8

ENV LC_ALL C.UTF-8

ENV PYTHONPATH=/code/

 

CMD ["sh", "-c", "tail -f /dev/null"]
