# PrroCoders — CS50W Capstone Project

## Overview

PrroCoders is a full-stack web application built as the final Capstone project for Harvard’s **CS50’s Web Programming with Python and JavaScript**. It leverages **Django** on the back-end and **Vanilla JavaScript** on the front-end to deliver a unified platform for:

- **Courses**: Browse, view, and enroll in free or paid courses with embedded video lessons and quizzes.  
- **WebMaker**: Submit custom website requests by selecting domain, database, dynamic features, and coupon codes.  
- **Portfolio**: Showcase past projects via an external portfolio link.  
- **Blog**: Read, search, and filter posts; admin can create/edit/delete posts and categories.  
- **Products**: Browse digital goods, filter by category, use stripe,
- **Admin Panel**: Manage employees, HRs, jobs, tasks, completed projects, coupons, courses, blog posts, web requests, and email communications.

---

## Distinctiveness and Complexity

PrroCoders stands apart from typical CS50W projects through its **multi-module architecture**, extensive **data relationships**, and **dynamic user workflows**:

1. **Multi-Domain Platform**  
   Rather than focusing on a single feature set (e.g., a social network or an e-commerce storefront), PrroCoders integrates **education**, **service requests**, **content management**, and **digital commerce** into one cohesive application. This breadth ensures distinctiveness from all prior Project 1–4 templates.

2. **Complex Data Models & Relationships**  
   The application defines multiple Django models with **foreign key** and **many-to-many** relationships. For example, each `Course` links to multiple `Lesson` objects and an `Exam`, while `WebRequest` entries record user-selected features. Advanced querysets and serializers power both server-rendered pages and AJAX endpoints.

3. **Dynamic Front-End Interactivity**  
   Using JavaScript and the Fetch API, PrroCoders implements real-time filtering, live search, modal forms, and partial page updates—allowing users to interact without full page reloads. These capabilities exceed the basic DOM manipulations covered earlier in the course.

4. **Responsive & Accessible UI**  
   The layout employs utility classes alongside custom CSS to ensure readability and usability across desktop, tablet, and mobile devices. Attention to semantic HTML and ARIA attributes enhances accessibility.

5. **Extensible Payment Flow**  
   While payment integration is not fully activated, the codebase includes a **placeholder “Buy Now”** route and initial Stripe configuration in `views.py` and `settings.py`. This design anticipates future extension without compromising current functionality.
6. **Multi User Experiences**
    There are Three types of users (normaluser, staffuser, superuser)
    the **normal user** is the client he can't edit or add. **staff user** is like a employee he can edit and add and remove but he can't add another employee or superuser. **superuser** is can edit and add and remove ,....  and add employee and add superuser.

Collectively, these elements demonstrate a level of planning, engineering, and user-centric design that goes well beyond the scope of individual CS50W homework projects.


- **`requirements.txt`** — Lists Python packages: Django, djangorestframework, python-dotenv, etc.  
- **`core/models.py`** — Defines `UserProfile`, `Course`, `Lesson`, `Exam`, `WebRequest`, `Product`, `BlogPost`, and related models.  
- **`core/views.py`** — Contains RESTful endpoints and page rendering views.  
- **`frontend/*.js`** — Vanilla JS for AJAX, filtering, form validation, and UI enhancements.  
- **`templates/`** — Django HTML templates using the template engine and Bootstrap components.  
- **`static/`** — CSS, images.

---

## How to Run

1. **Clone & Checkout**  
   ```bash
   git clone https://github.com/harvard2025/https://github.com/harvard2025/CS50W-Capstone.git
   cd CS50W-Capstone
   git checkout web50/projects/2020/x/capstone
   ```
2. Virtual Environment

python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Database Migrations

python manage.py migrate

5. Create Superuser (Optional)

python manage.py createsuperuser

6. Run Development Server

python manage.py runserver

7. Visit in Browser
Navigate to http://127.0.0.1:8000/

---

Additional Information

Python Packages: All dependencies are pinned in requirements.txt.

Admin Panel: Accessible at /admin/ for managing all models.

Video Demonstration: A 5-minute unlisted YouTube screencast showcasing core workflows is available at:
https://youtu.be/your-video-id

Submission Branch: This README resides on web50/projects/2020/x/capstone as required.

Future Work: Enable full Stripe integration, add pagination, and implement email notifications via Django’s email backend.

---

## Author

**Abdelrhman Ahmed Mazen**  
GitHub: [harvard2025](https://github.com/harvard2025)  
Email: **prro.code@gmail.com**

I am a passionate web developer and programmer, currently completing CS50’s Web Programming with Python and JavaScript. This project represents my final capstone, showcasing my skills in Django, JavaScript, and full-stack web development.

Feel free to reach out for questions or collaboration.
---

Thank you for reviewing PrroCoders. Please contact me via **prro.code@gmail.com** for any questions
