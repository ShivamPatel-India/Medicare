# Medicare

Medicare, a Python 3.7.2 and Django-powered e-commerce platform, provides a seamless online experience for purchasing medicines and healthcare products. Offering features real-time order tracking, an efficient admin panel, and doctor information by city, Medicare ensures a user-friendly and comprehensive healthcare shopping experience

## Quick Demo

You can watch a quick demo of the Medicare project by clicking [here](https://drive.google.com/file/d/1175mBN9126ZxmeeY5tgefyg8VuYGAh1H/view?usp=sharing).

## Project Functionality

- **E-Commerce Platform**: Medicare serves as an online marketplace for medicines and healthcare products, allowing users to browse and purchase items conveniently.

- **Order Management**: Users can place orders, complete payments securely, and track the status of their orders in real-time.

- **Admin Panel**: The project leverages the Django admin panel for administrative tasks, making it easy to manage products, inventory, and user data.

- **Doctor Information**: Users can access information about doctors based on their respective cities, helping them find healthcare professionals more easily.

## Running this Project Locally

To run this project on your local machine, follow these steps:

### Prerequisites

- Python (3.7.2 or later) installed on your computer.
- [virtualenv](https://pypi.org/project/virtualenv/) for creating a virtual environment.

### Installation Steps

1. Install Django:

   ```bash
   pip install django
   ```

2. Create a virtual environment:

   ```bash
   pip install virtualenv
   virtualenv venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

4. Clone or download this repository and navigate to the project's root directory.

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account, including username, email (optional), and password.

8. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

   The project will be accessible in your web browser at `http://localhost:8000/`.

### Accessing the Admin Panel

To access the Django admin panel, follow these steps:

1. Start the Django development server as described above.

2. Open your web browser and go to `http://localhost:8000/admin/`.

3. Log in with the superuser credentials you created earlier.

**Note**: To enable payment functionality, you'll need to enter your own Merchant ID and Merchant Key in the payment method configuration.


