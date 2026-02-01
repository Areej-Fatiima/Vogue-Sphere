
from supabase import create_client
import json

SUPABASE_URL = "https://apuzxvwyfdjzmzxveaib.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFwdXp4dnd5ZmRqem16eHZlYWliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUxNDMwNzgsImV4cCI6MjA2MDcxOTA3OH0.eGJjsanuHEqaG4F3IhI8g2vSEwN-29aVGsRy5paxg7o"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

res = supabase.storage.from_("scrape-data").list()
for f in res:
    if f['name'].endswith('.json'):
        print(f['name'])
