FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
ADD https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx /root/.u2net/u2net.onnx
COPY . .
ENTRYPOINT ["python3", "app.py"]