import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from app.models.appointment import Appointment
from fastapi import HTTPException

SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/compute']


def add(model: Appointment):

    credentials = service_account.Credentials.from_service_account_file(
        'credentials/google.calendar.json', scopes=SCOPES)

    # Build the Google Calendar API service
    service = build('calendar', 'v3', credentials=credentials)

    # Define the event details
    event_body = {
        'summary': "Doctor meeting " + model.user.full_name,
        'description': model.reason,
        'start': {'dateTime': model.start_time.isoformat(), 'timeZone': 'GMT'},
        'end': {'dateTime': (model.start_time + timedelta(minutes=model.duration)).isoformat(), 'timeZone': 'GMT'},
        # 'attendees': [
        #    {'email': model.user.email}
        # ],
    }

    try:
        event = service.events().insert(calendarId='primary', body=event_body).execute()
        return {"message": f'Event created: {event.get("htmlLink")}'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding event to Google Calendar: {str(e)}")

