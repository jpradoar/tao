#
# Como ejecutar: 
# 		docker run --rm -v $(pwd):/images clearbg
#
#
FROM python:3.10-slim
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY clearbg.py /app/clearbg.py
RUN pip install --no-cache-dir rembg pillow onnxruntime
VOLUME ["/images"]
# Comando por defecto: ejecutar el script en /images
CMD ["python", "clearbg.py"]