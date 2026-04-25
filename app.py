from flask import Flask


def create_app():
    """
    Application factory function for creating the Flask app instance.
    """
    app = Flask(__name__)

    @app.route("/")
    def home():
        """
        Render a simple placeholder homepage.
        """
        return "FitTrack Pro is starting up."

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)