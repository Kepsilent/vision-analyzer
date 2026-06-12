#!/usr/bin/env python3
"""Local Vision Analyzer — sends images to local llama-server for analysis.

Usage:
    python vision.py <image_path>
    python vision.py <image_path> --prompt "What is in this image?"

Requirements:
    - llama-server running at http://127.0.0.1:8080
    - Model loaded with --mmproj for vision support
"""

import argparse
import base64
import json
import urllib.error
import urllib.request
from pathlib import Path

SERVER_URL = "http://127.0.0.1:8080/v1/chat/completions"
SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"}
MIME_MAP = {
    "jpg": "jpeg", "jpeg": "jpeg", "png": "png",
    "webp": "webp", "gif": "gif", "bmp": "bmp",
}
MAX_FILE_SIZE_MB = 20
IMAGE_SIZE_LIMIT_BYTES = MAX_FILE_SIZE_MB * 1_000_000
REQUEST_TIMEOUT = 120


def analyze_image(image_path: str, prompt: str = "Describe this image in detail.") -> str:
    """Send image to local llama-server for vision analysis."""
    path = Path(image_path).resolve()

    # Security: only allow image files
    ext = path.suffix.lower()
    if ext not in SUPPORTED_EXTS:
        return (f"Error: Unsupported file type '{ext}'. "
                f"Supported: {', '.join(sorted(SUPPORTED_EXTS))}")

    if not path.is_file():
        return f"Error: File not found: {path}"

    # Security: reject symlinks pointing outside reasonable bounds
    if path.is_symlink():
        return "Error: Symbolic links are not allowed."

    file_size = path.stat().st_size
    if file_size > IMAGE_SIZE_LIMIT_BYTES:
        return (f"Error: Image too large ({file_size / 1_000_000:.1f} MB). "
                f"Max {MAX_FILE_SIZE_MB} MB.")

    try:
        with open(path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
    except PermissionError:
        return "Error: Permission denied — cannot read the file."
    except OSError as e:
        return f"Error reading file: {e}"

    mime = MIME_MAP.get(ext.lstrip("."), "jpeg")

    payload = {
        "model": "local-vision",
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/{mime};base64,{img_b64}"}},
            ],
        }],
        "max_tokens": 1024,
    }

    try:
        req = urllib.request.Request(
            SERVER_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        resp = json.loads(urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT).read())
    except urllib.error.URLError as e:
        if hasattr(e, 'reason') and isinstance(e.reason, TimeoutError):
            return (f"Error: Request timed out after {REQUEST_TIMEOUT} seconds. "
                    "The image may be too large or the model is overloaded.")
        return "Error: Cannot reach llama-server at http://127.0.0.1:8080. Is it running?"
    except urllib.error.HTTPError as e:
        return f"Error: llama-server returned HTTP {e.code}: {e.reason}"
    except json.JSONDecodeError:
        return "Error: Invalid response from llama-server."
    except Exception as e:
        return f"Error: {e}"

    msg = resp.get("choices", [{}])[0].get("message", {})
    content = msg.get("content", "") or msg.get("reasoning_content", "")

    if not content:
        return "Error: Empty response from model. Try a different image or prompt."

    return content


def main():
    parser = argparse.ArgumentParser(description="Local Vision Analyzer")
    parser.add_argument("image", help="Path to image file")
    parser.add_argument("--prompt", default="Describe this image in detail.",
                        help="Custom prompt for analysis")
    args = parser.parse_args()

    result = analyze_image(args.image, args.prompt)
    print(result)


if __name__ == "__main__":
    main()
