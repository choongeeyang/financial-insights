# Install Python dependencies for MkDocs
install:
	pip install --upgrade pip
	pip install mkdocs-material mkdocs-minify-plugin

# Serve docs locally (development mode)
serve:
	mkdocs serve

# Build static site for GitHub Pages
build:
	mkdocs build

# Optional: deploy to GitHub Pages (if not using GitHub Actions deploy)
deploy:
	mkdocs gh-deploy