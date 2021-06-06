from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    Popen(
        [
            "streamlit",
            "06_dashboards_are_fun/test.py",
            "--browser.serverAddress=0.0.0.0",
            "--server.enableCORS=False",
        ]
    )
