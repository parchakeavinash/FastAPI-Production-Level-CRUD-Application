# FastAPI-Production-Level-CRUD-Application
## ==========HOW TO RUN ============
1. Install dependencies:
   ```
   pip install fastapi uvicorn sqlalchemy pydantic slowapi
```
3. Run the server:
```
   uvicorn main:app --reload
   ```

4. Open API docs:
```
   http://localhost:8000/docs
   ```

5. Test the endpoints:
   - POST /items/ - Create item
   - GET /items/{item_id} - Get item
   - PUT /items/{item_id} - Update item
   - DELETE /items/{item_id} - Delete item
   - GET /items/{item_id}/automations - Get item's automations
   - POST /automations - Create automation
   - GET /automations/{id} - Get automation
   - PUT /automations/{id} - Update automation
   - DELETE /automations/{id} - Delete automation

code is actually production-grade! You have:
```
✅ Clean architecture (routers, db layer separation)
✅ Dependency injection
✅ Rate limiting
✅ Proper error handling
✅ Pydantic validation

## Key Concepts:
1. PROJECT STRUCTURE
   ✅ Separate routers for organization
   ✅ Database layer separate from routes
   ✅ Shared dependencies (limiter, get_db)

2. DEPENDENCY INJECTION
   ✅ db: Session = Depends(get_db)
   ✅ Automatic resource management
   ✅ Easy testing and mocking

3. DATABASE PATTERN
   ✅ SQLAlchemy models (DBItem, DBAutomation)
   ✅ Pydantic models (Item, ItemCreate, ItemUpdate)
   ✅ CRUD functions in separate file
   ✅ Custom exceptions (NotFoundError)

4. RATE LIMITING
   ✅ SlowAPI integration
   ✅ Per-endpoint limits
   ✅ IP-based tracking
   ✅ Automatic error handling

5. ERROR HANDLING
   ✅ Custom exceptions
   ✅ HTTPException for API errors
   ✅ Try-except in routes
   ✅ Proper status codes

6. PRODUCTION FEATURES
   ✅ Lifespan events (startup/shutdown)
   ✅ API documentation (automatic)
   ✅ Type validation (Pydantic)
   ✅ Database relationships
   ✅ RESTful design

   ```
   # ==================== COMPLETE FILE STRUCTURE ====================

db/items.py should have:
├── Item (Pydantic model)
├── ItemCreate (Pydantic model)
├── ItemUpdate (Pydantic model)
├── create_db_item()
├── read_db_item()
├── get_all_db_items()        ← NEW
├── update_db_item()
└── delete_db_item()

routers/items.py should have:
├── POST   /items/              → create_item()
├── GET    /items/              → get_all_items()      ← NEW
├── GET    /items/{item_id}     → read_item()
├── PUT    /items/{item_id}     → update_item()
└── DELETE /items/{item_id}     → delete_item()


db/automations.py should have:
├── Automation (Pydantic model)
├── AutomationCreate (Pydantic model)
├── AutomationUpdate (Pydantic model)
├── create_db_automation()
├── read_db_automation()
├── get_all_db_automations()   ← NEW
├── update_db_automation()
└── delete_db_automation()

routers/automations.py should have:
├── POST   /automations         → create_automation()
├── GET    /automations         → get_all_automations()  ← NEW
├── GET    /automations/{id}    → read_automation()
├── PUT    /automations/{id}    → update_automation()
└── DELETE /automations/{id}    → delete_automation()
```
