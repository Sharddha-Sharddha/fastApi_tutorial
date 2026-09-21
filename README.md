# FastAPI

A small FastAPI project with an in-memory product API.

## Run locally

Activate the virtual environment and start the development server:

```powershell
.\myenv\Scripts\Activate.ps1
uvicorn main:app --reload
```

Then open <http://127.0.0.1:8000/docs> for the interactive API documentation.

## Endpoints

- `GET /` - Return a greeting.
- `GET /products` - List all products.
- `GET /products/{id}` - Get a product by ID.
- `POST /products` - Add a product.
- `PUT /products?id={id}` - Update a product.