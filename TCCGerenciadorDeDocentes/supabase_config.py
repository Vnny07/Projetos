from supabase import create_client, Client

url = "https://omzsrcuelhhbdbyowvmp.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9tenNyY3VlbGhoYmRieW93dm1wIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUzNDg3NzQsImV4cCI6MjA2MDkyNDc3NH0.hBVq89sDzRdQSuNilo9j-yNQJqOg_ZuDT0bNl9q6Njo"

supabase: Client = create_client(url, key)