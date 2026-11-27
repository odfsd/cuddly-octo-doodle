import scratchattach as sa

# ── Config ────────────────────────────────────────────────────────────────────
USERNAME = "uOm77q9k0o"
PASSWORD = "uOm77q9k0o1"
PROJECT_ID = "1444893528"

HARDCODED_STUDIO_IDS = [
    "56", "154", "293", "3154", "6423",
    "7533", "14538", "31796", "14640", "105751", "16346", "279942", "27797704", "16409"
]

# ── Login ─────────────────────────────────────────────────────────────────────
session = sa.login(USERNAME, PASSWORD)
print(f"Logged in as {session.username}\n")

# ── Step 1: Hardcoded studios ─────────────────────────────────────────────────
print("=== Hardcoded Studios ===")
for studio_id in HARDCODED_STUDIO_IDS:
    try:
        studio = session.connect_studio(studio_id)
        studio.add_project(PROJECT_ID)
        print(f"✓ Added to studio {studio_id} — {studio.title}")
    except Exception as e:
        print(f"✗ Failed for studio {studio_id} — {e}")

# ── Step 2: Top 5 trending studios ───────────────────────────────────────────
print("\n=== Top 5 Trending Studios ===")
trending = sa.search_studios(query="add everything", mode="trending", limit=500)
for s in trending:
    if str(s.id) in HARDCODED_STUDIO_IDS:
        print(f"⟳ Skipped [{s.id}] {s.title} (already added above)")
        continue
    try:
        studio = session.connect_studio(str(s.id))
        studio.add_project(PROJECT_ID)
        print(f"✓ Added to studio {s.id} — {s.title}")
    except Exception as e:
        print(f"✗ Failed for studio {s.id} — {e}")

print("\nDone!")
