import sqlite3
import base64
import os

DB_PATH = "instance/your_database.db"  # ajuste conforme o seu projeto
EXPORT_DIR = "exported_audio"          # pasta para salvar os áudios

os.makedirs(EXPORT_DIR, exist_ok=True)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# mostra as tabelas disponíveis (opcional para exploração)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tabelas disponíveis:", cursor.fetchall())

# seleciona todos os registros da tabela (ajuste o nome se necessário)
cursor.execute("SELECT phrase, audio FROM recordings")
rows = cursor.fetchall()

print(f"Encontradas {len(rows)} gravações.")

# sxporta os dados
for i, (phrase, audio_b64) in enumerate(rows, 1):
    filename = f"{phrase}_{i:03}.ogg"
    filepath = os.path.join(EXPORT_DIR, filename)

    # Extrai apenas a parte após o cabeçalho data:audio/...
    if ',' in audio_b64:
        audio_b64 = audio_b64.split(',')[1]

    audio_data = base64.b64decode(audio_b64)

    with open(filepath, 'wb') as f:
        f.write(audio_data)

    print(f"Salvo: {filename}")

# Fecha conexão
conn.close()
