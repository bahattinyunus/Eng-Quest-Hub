import json
import os
from datetime import datetime

def load_events():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'events.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)['events']

def generate_markdown_table(events):
    # Sort events by date
    events.sort(key=lambda x: x['date'])
    
    table = "| 📅 Tarih | Etkinlik Adı | Tür | Durum | Link |\n"
    table += "|---|---|---|---|---|\n"
    
    for event in events:
        date_str = event['date']
        name = event['name']
        e_type = event['type']
        status = event['status']
        url = event['url']
        
        # Add emoji based on status
        status_icon = "🟢" if status == "Open" else "🟡" if status == "Confirmed" else "⚪"
        
        table += f"| {date_str} | {name} | {e_type} | {status_icon} {status} | [🔗 Link]({url}) |\n"
        
    return table

if __name__ == "__main__":
    try:
        events = load_events()
        md_table = generate_markdown_table(events)
        print("### 📅 Güncel Etkinlik Takvimi")
        print(md_table)
        print("\n*Bu tablo `scripts/update_events.py` ile otomatik oluşturulmuştur.*")
    except Exception as e:
        print(f"Error: {e}")
