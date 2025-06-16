### 🔔 Vazifa nomi: `Task Manager CLI Project`

### 🎯 Maqsad:

Siz mustaqil ravishda terminalda ishlaydigan "Vazifalar boshqaruvchisi" (Task Manager) dasturini yaratishingiz kerak. Bu loyiha orqali siz quyidagilarni amalda qo‘llaysiz:

* Python funksiyalarini yaratish va ulardan foydalanish
* `list` bilan ishlash
* `input`, `if-elif`, `while`
* Oddiy CLI (Command Line Interface) dastur yaratish

---

## 📌 Topshiriq tavsifi

Siz quyidagilarni qila oladigan dastur yozishingiz kerak:

### 🔹 Menu:

```
========= Menu =========
1. Task qo'shish
2. Tasklarni ko'rish
3. Taskni o'chirish
4. Taskni yangilash
5. Chiqish
```

### 🔹 Funksiyalar:

* `add_task()` – foydalanuvchidan yangi task nomi so‘raydi va ro‘yxatga qo‘shadi.
* `print_todos()` – mavjud tasklarni ko‘rsatadi.
* `delete_task()` – raqam orqali taskni o‘chiradi.
* `update_task()` – task nomini yangilaydi.
* `main()` – barcha harakatlarni boshqaruvchi bosh funksiya.

---

## ✅ Talablar:

1. **Kod modular bo‘lishi kerak** – har bir funksiya alohida yozilsin.
2. **Foydalanuvchi bilan muloqot aniq bo‘lsin** – har bir harakatdan so‘ng tushunarli xabarlar chiqarilsin.
3. **Xatoliklar nazorat qilinsin** – noto‘g‘ri raqam kiritsachi? Bo‘sh ro‘yxat bo‘lsa-chi?
4. **Kodni chiroyli formatlang** – o‘qilishi oson bo‘lishi kerak.
5. **Izohlar yozing** – har bir funksiya oldida `docstring` bo‘lsin.

---

## 📁 Tashkiliy tuzilma

Quyidagi fayllarni topshirish talab qilinadi:

```
task-manager/
├── task_manager.py  ✅ Asosiy kod
└── README.md        📄 Loyiha haqida hujjat
```

---

## 🧠 Bonus topshiriqlar (bajarilsa +ball):

### ✅ Bonus 1: Har bir taskni tartib bilan qo‘shish

> Foydalanuvchi har gal task qo‘shganda, ro‘yxat oxiriga emas, **alfavit tartibida** joylashtiring.

💡 Maslahat: `todos.sort()` ishlating.

---

### ✅ Bonus 2: O‘chirayotganda “Tasdiqlash” qo‘shish

> Foydalanuvchi taskni o‘chirishdan oldin `ha/yo‘q` deb tasdiqlasin.

---

### ✅ Bonus 3: Barcha tasklarni bir vaqtning o‘zida o‘chirish

> 3-bo‘limdan tashqari, alohida menyu bandi sifatida “Barcha tasklarni tozalash” funksiyasini yozing.

---

### ✅ Bonus 4: Task nomi 20 belgidan oshsa, ogohlantirish

> Task nomi juda uzun bo‘lsa, foydalanuvchini ogohlantiring.

---

### ✅ Bonus 5: Bo‘sh task nomiga ruxsat bermaslik

> Foydalanuvchi faqat `Enter` bosib yuborsa, task qo‘shilmasin.

---

## ✅ Baholash mezonlari:

| Ko‘rsatkich                   | Ball |
| ----------------------------- | ---- |
| Funksiyalar to‘liq ishlaydi   | 40    |
| Xatoliklar nazorat qilingan   | 20    |
| Kod toza, o‘qilishi qulay     | 20    |
| docstring to‘g‘ri yozilgan    | 10    |
| Bonus funksiyalar (ixtiyoriy) | +10   |

> Maksimal ball: 90 (bonus bilan 100)

---
