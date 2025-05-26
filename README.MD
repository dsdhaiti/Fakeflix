# Fakeflix

Fakeflix is a Flask-based web application that mimics a movie streaming platform. Users can register, log in, search for movies (using the OMDb API), and view movie information. The project uses Bootstrap 4 for frontend styling.

## Features

- User registration and login
- Forgot password page
- Movie search with results from the OMDb API
- Responsive UI with Bootstrap 4
- Example pages: Home, About, Pricing, Admin, etc.

## Languages & Technologies Used

- **Python**: The main backend language, using the Flask framework to handle routing, server logic, and API requests.
- **HTML**: For structuring the web pages, using Jinja2 templating with Flask.
- **CSS**: For styling the application, including custom styles and Bootstrap 4 for responsive design.
- **JavaScript**: For client-side interactivity (in static JS files).
- **SQL**: For database schema and user data management (see `userDatabase/`).
- **Bootstrap 4**: For frontend components and layout.

These technologies work together to provide a full-stack web application experience.

## Setup & Installation

1. **Clone the repository**

   ```sh
   git clone <your-repo-url>
   cd Fakeflix
   ```

2. **Install dependencies**

   Make sure you have Python 3 and pip installed.

   ```sh
   pip install flask requests
   ```

3. **Run the application**

   ```sh
   python fake.py
   ```

   The app will be available at `http://127.0.0.1:5000/`.

## Usage

- Visit `/` or `/login` to access the login/registration page.
- Use `/home`, `/about`, `/pricing`, `/admin`, etc. for other pages.
- After logging in, search for movies using the search form.
- The app fetches movie data from the [OMDb API](http://www.omdbapi.com/).

## Customization

- Edit HTML templates in `templates/`
- Change styles in `static/`
- Update the OMDb API key in `fake.py`

## OMDb API Key

You can get a free API key from [OMDb API](http://www.omdbapi.com/apikey.aspx). Replace the `key` variable in `fake.py` with your key.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is for educational purposes and is not affiliated with Netflix. Bootstrap is used under the MIT license.

---

**Note:** You need an OMDb API key for movie search functionality. Replace the `key` variable in [`fake.py`](fake.py) with your own if needed.
