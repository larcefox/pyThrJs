from flask import Flask, redirect, url_for, render_template
from lib.reload_canvas import Worker


app = Flask(__name__)
reloader = Worker()
entity_dict = reloader.run_reload()

@app.route('/')
def home():
    return render_template(
            'modeller.html',
            title='title',
            body='body',
            light=entity_dict['lights'], 
            camera=entity_dict['camera'], 
            entity=entity_dict['shape']
            )


if __name__ == '__main__':
    app.run(debug=True, host='192.168.31.6')
