from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Предположим, что у нас есть переменная, показывающая, зарегистрирован ли пользователь
is_registered = False

# Маршрут для главной страницы (перенаправление на /home)
@app.route('/')
def index():
    return redirect(url_for('home'))

# Маршрут для страницы Home
@app.route('/home')
def home():
    return render_template('home.html')

# Маршрут для страницы About
@app.route('/about')
def about():
    return render_template('about.html')

# Маршрут для страницы Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Маршрут для страницы Main Page
@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

# Маршрут для страницы Login (Вход)
@app.route('/login')
def login():  
    return render_template('login.html')

# Маршрут для страницы Registration (Регистрация)
@app.route('/register')
def registration():
    return render_template('register.html')

# Маршрут для страницы Dashboard (Панель управления)
@app.route('/dashboard')
def dashboard():
    global is_registered
    # Если пользователь не зарегистрирован, перенаправляем его на страницу регистрации
    if not is_registered:
        return redirect(url_for('registration'))
    # Иначе показываем страницу панели управления
    user_info = {"username": "example_user", "email": "example@example.com"}  # Пример данных о пользователе
    return render_template('dashboard.html', user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True, port=4200)
