### Epic 3: Frontend MVP (Next.js) & Deployment

**Description:** Build the user-facing platform mirroring the basic functionality of Alpha Vantage and deploy it live.

- **Task 3.1: Next.js Foundation**
    - **Subtask:** Initialize a Next.js application with TailwindCSS (`npx create-next-app@latest`).
    - **Subtask:** Set up the GitHub repository and commit the initial structure.
- **Task 3.2: Build the Landing Page & UI**
    - **Subtask:** Design a clean, developer-focused landing page explaining the platform's value proposition.
    - **Subtask:** Create a search input component allowing users to query specific company tickers.
- **Task 3.3: Data Visualization Dashboard**
    - **Subtask:** Install a charting library (like Recharts or Chart.js).
    - **Subtask:** Create a dashboard component that fetches the mock JSON data from your FastAPI backend and renders it into a line or bar chart.
- **Task 3.4: Vercel Deployment**
    - **Subtask:** Connect the GitHub repository directly to Vercel.
    - **Subtask:** Configure any necessary environment variables and trigger the production deployment.
    - **Subtask:** Test the live URL to ensure the frontend successfully renders the mock data from the backend.