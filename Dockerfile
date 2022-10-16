FROM python:3

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /team_assessment_comparison_backend
COPY . /team_assessment_comparison_backend
COPY requirements.txt /team_assessment_comparison_backend
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "team_assessment_comparison_backend.wsgi:application"]