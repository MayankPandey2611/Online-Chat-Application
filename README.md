💬 Online Chat Application
A real-time chat application built with Django and Django Channels, enabling instant messaging between users over WebSocket connections — no page refresh needed.
🔗 Live Demo: https://online-chat-application-3.onrender.com/

✨ Features

🔐 User Authentication — Register, log in, and log out securely
💬 Real-Time Messaging — Instant bidirectional communication via WebSockets
🏠 Chat Rooms — Join or create rooms to chat with multiple users
⚡ Async Support — Built on ASGI for non-blocking, high-performance communication
📱 Clean UI — Simple HTML-based interface for distraction-free chatting


🖥️ Tech Stack
LayerTechnologyBackendPython, DjangoReal-TimeDjango Channels (WebSockets)ProtocolASGI (Daphne / Uvicorn)FrontendHTML, CSS, JavaScriptDatabaseSQLite (dev)DeploymentRender

📁 Project Structure
Online-Chat-Application/
├── chatapp/              # Core chat app (consumers, models, views, routing)
├── chatweb/              # Django project settings & ASGI config
├── template/             # HTML templates
├── manage.py
├── requirements.txt
├── Procfile              # For Render deployment
└── db.sqlite3

⚙️ How It Works

A user opens the app and logs in.
The browser establishes a WebSocket connection to the Django Channels server.
When a message is sent, Django Channels routes it through a consumer to all connected clients in the same room — instantly and without polling.
Messages are handled asynchronously using Django's ASGI interface.


🚀 Getting Started
Prerequisites

Python 3.x
pip

Installation
bash# 1. Clone the repository
git clone https://github.com/MayankPandey2611/Online-Chat-Application.git
cd Online-Chat-Application

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

Note: Django Channels requires an ASGI server. For local dev, python manage.py runserver works. For production, use Daphne or Uvicorn.


🔗 Key Routes
URLDescription/Home / Chat room list/register/User registration/login/User login/logout/User logout/chat/<room_name>/Enter a specific chat room

☁️ Deployment
This app is deployed on Render using a Procfile.
To deploy your own instance:

Push your code to GitHub.
Create a new Web Service on Render and connect your repository.
Set the build command:

   pip install -r requirements.txt

Set the start command (using Daphne for ASGI/WebSocket support):

   daphne chatweb.asgi:application

Add required environment variables: SECRET_KEY, DEBUG=False, ALLOWED_HOSTS.


Important: Standard WSGI servers (like Gunicorn alone) do not support WebSockets. Always use an ASGI server such as Daphne or Uvicorn for Channels projects.


🛠️ Django Channels Key Concepts
ConceptRoleconsumers.pyHandles WebSocket connect, disconnect, and receive eventsrouting.pyMaps WebSocket URL patterns to consumers (like urls.py for HTTP)asgi.pyEntry point — routes HTTP and WebSocket traffic separatelyChannel LayerAllows consumers to broadcast messages to a group of users

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to open a pull request.

👤 Author
Mayank Pandey
GitHub: @MayankPandey2611
