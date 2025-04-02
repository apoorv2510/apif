# Sports Players API

This is a Flask-based RESTful API for managing and retrieving information about popular sports players. The API is deployed using AWS Elastic Beanstalk and supports Docker-based deployment for scalable hosting.

## 🚀 API Overview

The API provides a single endpoint:

### `GET /players`

Returns a list of famous football players including their name, team, nationality, position, and age.

### Example Response
```json
[
  {
    "id": 1,
    "name": "Lionel Messi",
    "team": "Inter Miami",
    "nationality": "Argentina",
    "position": "Forward",
    "age": 36
  },
  ...
]
```

## 🧰 Technologies Used

- Python 3.11
- Flask
- Docker
- AWS Elastic Beanstalk
- GitHub Actions (CI/CD)

## 📦 Project Structure

```
.
├── apiap.py              # Flask Blueprint with player data
├── application.py        # Main application entry point
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
├── .github/workflows/    # GitHub Actions CI/CD configuration
```

## 🔄 CI/CD Pipeline

The deployment is handled automatically through GitHub Actions:
- Verifies the application content and versions.
- Zips the app and creates a new version with a timestamp.
- Uploads to AWS S3 and triggers deployment on Elastic Beanstalk.
- Ensures consistent versioning and avoids mismatched versions.

## 📝 Deployment Notes

- The API is designed to run on port `8080` within the Docker container.
- JSON data is embedded directly in the `apiap.py` file for quick testing.
- Swagger integration (`flasgger`) supports API documentation.

## 📈 Usage

You can test the deployed API at:
```
GET https://<your-eb-endpoint>/api/players
```

## ✨ Future Enhancements

- Add filtering or searching of players by nationality or position.
- Add POST/PUT methods for extending player list via API.
- Integrate with DynamoDB for dynamic data storage.
