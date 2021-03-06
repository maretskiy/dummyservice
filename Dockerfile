FROM alpine:3.5
RUN apk update
RUN apk --no-cache add python
COPY run_service.py /
CMD python /run_service.py
