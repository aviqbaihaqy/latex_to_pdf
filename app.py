from flask import Flask, request, send_file
from io import BytesIO
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route('/download', methods=['POST'])
def generate_pdf():
    # Mendapatkan data user dari request JSON
    data = request.get_json()
    nama = data.get('nama', '')
    email = data.get('email', '')

    # Menggenerate file LaTeX
    with open('templates/template.tex', 'r') as f:
        template = f.read()
    latex_data = template.format(nama=nama, email=email)
    with open('data.tex', 'w') as f:
        f.write(latex_data)

    # Menjalankan perintah untuk meng-generate PDF
    subprocess.run(['pdflatex', 'data.tex'])

    # Membaca file PDF hasil generate dan mengirimkannya sebagai response
    pdf_file = 'data.pdf'
    with open(pdf_file, 'rb') as f:
        pdf = f.read()
    buffer = BytesIO(pdf)
    return send_file(buffer, as_attachment=True, download_name='data.pdf', mimetype='application/pdf')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
