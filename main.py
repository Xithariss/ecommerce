from app import app
from livereload import Server

if __name__ == '__main__':
  # server = Server(app.wsgi_app)
  # server.serve()
  # server.watch('/app/*')
  app.run('0.0.0.0')