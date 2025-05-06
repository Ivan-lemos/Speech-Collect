# 🎤 Open Speech Recording Web App

A browser-based tool for collecting speech samples with randomized prompts. Users can record voice samples, review or delete them, and submit recordings to a server for further processing or machine learning dataset generation.

## 🚀 Features

- Record randomized speech phrases directly from the browser
- Automatic naming of files (`keyword_###.ogg`)
- Review and delete recordings before submitting
- Submission to a Flask backend with SQLite storage
- Multi-language support (PT/EN) toggle

## 🛠️ Tech Stack

- **Frontend:** JavaScript, HTML5, CSS, Web Audio API
- **Backend:** Python, Flask
- **Database:** SQLite

## 🗂️ File Naming Convention

Recordings are saved following the structure:


Where `keyword` is the phrase recorded and `###` is the sample index (e.g., `ola_mundo_001.ogg`).

## 📦 Usage

- Set number of samples via input field
- Press **Record** to begin the cycle (phrase shown → recording starts → file auto-saved)
- Press **Stop** to halt recording
- Press **Submit** to save all samples to the backend

## 🧪 Ideal for:

- Speech dataset collection
- TinyML model training
- Voice recognition experiments

## 🙏 Credits

This project was inspired by the amazing work of [Pete Warden](https://petewarden.com) and the [Open Speech Recording Project](https://tinyml.seas.harvard.edu/open_speech_recording/).

Original source code: [github.com/petewarden/open-speech-recording](https://github.com/petewarden/open-speech-recording)

Many thanks for providing such a helpful tool for the community.
