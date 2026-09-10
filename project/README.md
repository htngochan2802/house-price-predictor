# House Price Predictor — FastAPI + HTML

## Cấu trúc

```
project/
├── backend/
│   ├── main.py           # FastAPI app: predict_price() + /predict endpoint + static mount
│   └── requirements.txt
└── frontend/
    └── house_form.html   # Form + JS gọi /predict bằng URL tương đối
```

## Cách chạy

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Server chạy tại: http://127.0.0.1:8000

## Cách kiểm tra

1. **Tài liệu API (Swagger UI):**
   http://127.0.0.1:8000/docs
   → mở `/predict`, bấm "Try it out", nhập `area=80`, `bedrooms=3`, `location=hanoi`, bấm Execute.

2. **Gọi trực tiếp qua URL bar:**
   http://127.0.0.1:8000/predict?area=80&bedrooms=3&location=hanoi

3. **Trang form (đã kết nối sẵn với API):**
   http://127.0.0.1:8000/static/house_form.html
   → điền form, bấm "Predict price" → kết quả hiện ngay trên trang.
   → nhìn vào terminal đang chạy `uvicorn`, mỗi lần submit sẽ có thêm 1 dòng log
     `GET /predict?area=...&bedrooms=...&location=... 200 OK`.

## Ghi chú quan trọng

- `frontend/` và `backend/` phải nằm **ngang hàng nhau** (sibling folders) — không đổi tên
  hay di chuyển, vì `main.py` dùng đường dẫn tương đối `"../frontend"` để mount static files.
- KHÔNG mở `house_form.html` bằng Live Server hay double-click trực tiếp — làm vậy sẽ chạy
  ở một port khác (vd :5500) và gây lỗi CORS khi gọi `/predict`. Luôn mở qua
  `http://127.0.0.1:8000/static/house_form.html` để cùng origin với API.
