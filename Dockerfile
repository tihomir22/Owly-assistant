FROM python:3.9

# Create and activate the virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install -U g4f
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script to the container
COPY app.py .

# # Expose port 5000
EXPOSE 5001

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5001","--timeout","240"]