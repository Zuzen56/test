from flask import Flask,render_template,request
import os


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/relic',methods=["POST","GET"])
def relic():
    if 'image' in request.files:
        image_file = request.files['image']

        upload_folder = '/uploaded_images'

        # 创建保存文件的文件夹（如果不存在的话）
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # 将文件保存到指定路径
        image_file.save(os.path.join(upload_folder, 'uploaded_image.png'))

        return 'Image successfully uploaded'




if __name__ == '__main__':
    app.run(port=5000)