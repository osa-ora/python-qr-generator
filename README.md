# QR Code Generator with Optional Logo

A self-contained utility to generate high-quality QR codes with an optional custom logo overlaid in the exact center. The project includes an automated Bash wrapper script (`run.sh`) that takes care of all setup prerequisites automatically—including creating a Python virtual environment, updating pip, installing dependencies, and running the code cleanly.

## Project Structure

```text
.
├── qr-generator.py      # Core Python script for QR generation
├── run.sh               # Bash wrapper script (handles auto-installation & runtime)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

```

---

## Prerequisites

Before running the project, you only need to ensure you have the following baseline tools installed on your host system:

* **Python 3**
* **Bash shell** (Standard on Linux/macOS, available via Git Bash/WSL on Windows)

No manual library installation (`pip install`) is required. The execution script automates this inside an isolated workspace.

---

## Usage via the Bash Script (`run.sh`)

The shell wrapper handles environment creation dynamically and seamlessly routes your custom inputs straight to the underlying engine.

### 1. Grant Execution Permissions

Before executing for the first time, run this command in your terminal to allow the script to run:

```bash
chmod +x run.sh

```

### 2. Execution Profiles

The script accepts parameters sequentially using standard positional configurations:
`./run.sh [URL] [LOGO_PATH] [OUTPUT_FILE]`

* **Profile A: System Default Execution**
Running the script without any parameters defaults back to the internal testing configurations (Red Hat Demo workshop URL, standard logo asset, default output name):
```bash
./run.sh

```


* **Profile B: Clean QR Code (No Logo)**
To skip embedding a logo entirely while mapping a custom destination URL and choosing your own output name, pass an empty string `""` as the second argument:
```bash
./run.sh "[https://github.com](https://github.com)" "" "github_clean.png"

```


* **Profile C: Custom URL with Center Logo**
To inject both your target link and custom logo design into a distinct output file:
```bash
./run.sh "[https://google.com](https://google.com)" "assets/google_logo.png" "google_qr.png"

```



---

## Advanced: Manual Python CLI Bypass

If you ever need to manually interface directly with the generator bypass script inside an active virtual environment:

```bash
python3 qr-generator.py -u "<URL_OR_TEXT>" [-l "<PATH_TO_LOGO>"] [-o "<OUTPUT_FILENAME>"]

```

#### Available Flags:

* `-u, --url` *(Required)*: Target string text or URL structure to generate into the canvas matrix.
* `-l, --logo` *(Optional)*: Filepath pointing to the image graphic asset to bake into the center. Leaving this flag out completely outputs a standard minimalist QR vector.
* `-o, --output` *(Optional)*: Custom target name for the finalized file. Falls back to `qr_with_logo.png` if unstated.

---

## Core Features & Fault-Tolerance

* **Fault-Tolerant Scanning:** Employs explicit `ERROR_CORRECT_H` configurations (approx 30% pixel block restoration tolerance). This explicitly keeps the code completely legible by mobile scanners even if your logo takes up substantial space in the center.
* **Auto-Scaling Layouts:** Automatically benchmarks dimensions and rescales the targeted logo asset down to exactly 20% of the overall width of the grid workspace so it never covers up critical tracking points.
* **Graceful Degradation:** If a bad file path is specified for the `--logo` property, the utility logs an explicit warning to the terminal pipeline and finishes saving a fully-functional standard QR code instead of raising an uncaught exception.

```

```
