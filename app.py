from flask import Flask, render_template, session, redirect, url_for
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecretkey"  # required for sessions if needed
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})


    @app.route('/MentalHealthToolKit') 
    def mental_health_toolkit():
        return render_template('MentalHealthToolKit.html')


    @app.route('/ExecutiveFunctuoningToolKit')
    def executive_functioning_toolkit():
        return render_template('ExecutiveFunctioningToolKit.html')
    
    @app.route('/')
    def home():
        return render_template('index.html')


    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)