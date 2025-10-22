# FastAPI-Production-Level-CRUD-Application
# ==================== HOW TO RUN ====================
"""
1. Install dependencies:
   pip install fastapi uvicorn sqlalchemy pydantic slowapi

2. Run the server:
   uvicorn main:app --reload

3. Open API docs:
   http://localhost:8000/docs

4. Test the endpoints:
   - POST /items/ - Create item
   - GET /items/{item_id} - Get item
   - PUT /items/{item_id} - Update item
   - DELETE /items/{item_id} - Delete item
   - GET /items/{item_id}/automations - Get item's automations
   - POST /automations - Create automation
   - GET /automations/{id} - Get automation
   - PUT /automations/{id} - Update automation
   - DELETE /automations/{id} - Delete automation
"""

