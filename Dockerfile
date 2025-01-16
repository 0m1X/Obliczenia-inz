FROM python:3.9

RUN apt-get update
RUN apt-get install vim -y
RUN mkdir -p /home/integrals_zal

RUN pip install sympy 

COPY main.py /home/integrals_zal/main.py
COPY monte_carlo_integration.py /home/integrals_zal/monte_carlo_integration.py
COPY simpson_integration.py /home/integrals_zal/simpson_integration.py
COPY trapezoidal_integration.py /home/integrals_zal/trapezoidal_integration.py

WORKDIR /home/integrals_zal

CMD ["python","/home/integrals_zal/main.py"]



