FROM python:3.9

RUN apt-get update
RUN apt-get install vim -y
RUN mkdir -p /home/integrals_zal

RUN pip install sympy 
#RUN pip install random

COPY main.py /home/integrals_zal/main.py
COPY monte_carlo_integration.py /home/integrals_zal/monte_carlo_integration.py
COPY simpson_integration.py /home/integrals_zal/simpson_integration.py
COPY trapezoidal_integration.py /home/integrals_zal/trapezoidal_integration.py

WORKDIR /home/integrals_zal

# Run 
CMD ["python","/home/integrals_zal/main.py"]
#CMD ["/bin/bash"]

# docker run -it --name python39 –v C:\Users\MK\Desktop\cloud24:/home/cloud python39
