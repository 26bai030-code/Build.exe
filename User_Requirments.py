
def launch_streamlit_app():
    """Install required packages, then launch the Streamlit UI."""

    # Ensure all dependencies, including Streamlit, are installed
    auto_install_requirements()

    app_path = Path(__file__).resolve().parent / "app.py"

    if not app_path.is_file():
        raise FileNotFoundError(
            f"Could not find app.py at: {app_path}"
        )

    print("\nStarting AURA AI interface...\n")

    # Equivalent to: python3 -m streamlit run app.py
    subprocess.run(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(app_path),
        ],
        check=True,
    )
