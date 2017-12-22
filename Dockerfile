FROM blinkt

WORKDIR /root/
COPY rainbox.py .

CMD ["python", "rainbox.py"]