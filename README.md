# TDS Virtual TA Project

This project is a FastAPI-based virtual teaching assistant that performs web scraping, semantic search, and provides API endpoints for interaction. The application is deployed on Vercel.

## Project Structure

- `app.py`: Main FastAPI application with API endpoints.
- `Python_Scraper.py`: Script to scrape data from web sources.
- `semantic_search.py`: Implements semantic search functionality.
- `preprocess.py`: Preprocessing script to prepare data for search.
- `requirements.txt`: Python dependencies including FastAPI and Uvicorn.
- `vercel.json`: Configuration file for Vercel deployment.
- `LICENSE`: MIT License file.
- `Postman_TDS_Virtual_TA_Collection.json`: Postman collection for API testing.
- `knowledge_base.db`: Database file created after preprocessing.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/jainamay/TDS_Project_1.git
   cd TDS_Project_1
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the scraper to collect data:
   ```
   python Python_Scraper.py
   ```

4. Run the preprocessing script to create the knowledge base:
   ```
   python preprocess.py
   ```

5. Run the FastAPI app locally (optional):
   ```
   uvicorn app:app --reload
   ```

## Deployment

The app is deployed on Vercel. The root endpoint returns a welcome message, and the `/search` endpoint accepts POST requests for semantic search queries.

## API Testing

Use the provided Postman collection `Postman_TDS_Virtual_TA_Collection.json` to test the API endpoints.

- Import the collection into Postman.
- Set the `base_url` variable to your deployed app URL.
- Test the root endpoint and semantic search endpoint.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
