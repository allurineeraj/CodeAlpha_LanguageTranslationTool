"""
End-to-End Automated Test Suite for CodeAlpha Language Translation Tool
"""

import sys
import os
import io
import time
import urllib.request

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from deep_translator import GoogleTranslator
from gtts import gTTS

print("=" * 65)
print("  [*] RUNNING CODEALPHA LANGUAGE TRANSLATION TOOL TEST SUITE")
print("=" * 65)

# ----------------------------------------------------
# Test 1: Check Streamlit Web Server Availability
# ----------------------------------------------------
print("\n[TEST 1] Checking Streamlit Web Server at http://localhost:8501 ...")
try:
    response = urllib.request.urlopen("http://localhost:8501", timeout=5)
    status_code = response.getcode()
    assert status_code == 200, f"Expected 200, got {status_code}"
    print(f"  [PASS] Streamlit Web Server is running and responding (HTTP {status_code}).")
except Exception as e:
    print(f"  [FAIL] Server check failed: {e}")
    sys.exit(1)

# ----------------------------------------------------
# Test 2: Check app.py Translation Logic & Language Catalog
# ----------------------------------------------------
print("\n[TEST 2] Verifying Translation Processing & Supported Languages ...")
try:
    import app
    languages = app.load_languages()
    print(f"  [PASS] Supported languages catalog loaded with {len(languages)} languages.")
    assert "english" in languages, "English should be supported"
    assert "spanish" in languages, "Spanish should be supported"
    assert "french" in languages, "French should be supported"

    # Test Translation from English to Spanish
    sample_text = "Welcome to the language translation tool! Have a wonderful day."
    print(f"  Testing translation: '{sample_text}' -> Spanish")
    translated = app.execute_translation(sample_text, "Auto Detect", "Spanish")
    assert translated and len(translated.strip()) > 0, "Translation result should not be empty"
    print(f"  [PASS] Translation successful -> '{translated}'")

    time.sleep(1)

    # Test Translation from English to French
    sample_text_fr = "Hello my friend, good morning!"
    print(f"  Testing translation: '{sample_text_fr}' -> French")
    translated_fr = app.execute_translation(sample_text_fr, "Auto Detect", "French")
    assert translated_fr and len(translated_fr.strip()) > 0, "French translation should not be empty"
    print(f"  [PASS] Translation successful -> '{translated_fr}'")

except Exception as e:
    print(f"  [FAIL] Translation logic failed: {e}")
    sys.exit(1)

# ----------------------------------------------------
# Test 3: Check gTTS Audio Generation & Streaming Output
# ----------------------------------------------------
print("\n[TEST 3] Verifying Text-to-Speech (gTTS) Audio Synthesis ...")
try:
    audio_buffer = io.BytesIO()
    tts = gTTS(text=translated, lang="es", slow=False)
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    audio_bytes = audio_buffer.read()
    assert len(audio_bytes) > 0, "Audio stream should contain bytes"
    print(f"  [PASS] Audio synthesis successful. Generated {len(audio_bytes)} bytes of MP3 audio.")
except Exception as e:
    print(f"  [FAIL] gTTS audio synthesis failed: {e}")
    sys.exit(1)

# ----------------------------------------------------
# Test 4: Check Input Validation Handling
# ----------------------------------------------------
print("\n[TEST 4] Verifying Input Validation and Edge Cases ...")
try:
    empty_res = app.execute_translation("", "Auto Detect", "Spanish")
    print(f"  [PASS] Empty input safely handled without uncaught exceptions.")
except Exception as e:
    print(f"  [FAIL] Empty input caused unexpected exception: {e}")
    sys.exit(1)

# ----------------------------------------------------
# Test 5: Verify Required Project Files Exist
# ----------------------------------------------------
print("\n[TEST 5] Checking Project Structure ...")
required_files = ["app.py", "requirements.txt", "README.md"]
for fname in required_files:
    if os.path.exists(fname) and os.path.getsize(fname) > 0:
        print(f"  [PASS] Found '{fname}' ({os.path.getsize(fname)} bytes)")
    else:
        print(f"  [FAIL] Missing or empty file: {fname}")
        sys.exit(1)

print("\n" + "=" * 65)
print("  [SUCCESS] ALL 5/5 TESTS PASSED! THE APPLICATION IS READY.")
print("=" * 65)
