
# 📱🤖 AI Social Media Manager

An AI-powered application that helps users generate high-quality social media content, improve engagement, and plan content strategies using Google Gemini.

---

## 🚀 Features

- ✍️ **AI Post Generator**
  - Generate platform-specific posts (Instagram, LinkedIn, Twitter)
  - Includes hooks, main content, CTA, and hashtags

- 📅 **Content Calendar Generator**
  - 7-day or 30-day content planning
  - Structured daily posting ideas

- 🔥 **Caption Improver**
  - Enhances engagement
  - Adds hooks and call-to-actions

- 🎯 **Audience-Focused Content**
  - Tailored tone and platform optimization

- 💾 **Post History**
  - Save and review previously generated posts

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- Session State (for storing posts)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-social-media-manager.git
cd ai-social-media-manager
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Get your API key from:
[https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. Enter a **topic**
2. Choose:

   * Platform (Instagram / LinkedIn / Twitter)
   * Tone (Professional, Casual, etc.)
3. Generate:

   * Full post
   * Hashtags
   * CTA

Additional tools:

* Generate content calendar
* Improve captions
* Save posts

---

## 💡 Example

**Input:**
Topic: "AI in education"
Platform: LinkedIn
Tone: Professional

**Output:**
A structured post with:

* Hook
* Insightful content
* CTA
* Relevant hashtags

---

