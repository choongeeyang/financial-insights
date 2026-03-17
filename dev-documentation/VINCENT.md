## Create documentation site
- using Cursor, create the documentations .md files 
- created mkdocs.yml and deploy-docs-on-main.yml 
- install dependencies: pip install mkdocs-material mkdocs-minify-plugin
- serve locally from root: mkdocs serve 
- build the site locallt: mkdocs build

## Create MVP main page
- using Cursor, create MVP landing page
- added VERCEL_TOKEN to github secrets
- npm install -g vercel
- vercel link -> create .vercel

## Deploy backend on render 
- look at src/backend/render.yml
- auto redeploy when code pushed changes certain files: refer render.yml
- deployed live on render: 
- link to swagger UI: https://financial-insights-grit.onrender.com
