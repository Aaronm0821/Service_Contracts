from apps import create_app
from apps.config import app_config

app = create_app(app_config)

if __name__ == '__main__':
    app.run(debug=True)




