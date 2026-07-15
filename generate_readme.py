import os

# Resolve paths dynamically relative to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
readme_path = os.path.join(script_dir, "README.md")

# Load WALI ASCII art
ascii_wali_path = os.path.join(script_dir, "ascii_wali.txt")
if os.path.exists(ascii_wali_path):
    with open(ascii_wali_path, "r", encoding="utf-8") as f:
        wali_ascii = f.read().rstrip()
else:
    wali_ascii = ""

# Helper function to frame text inside a terminal border of width 104 (interior 102)
def frame_block(title, lines):
    # title can be empty
    if title:
        header = f"┌───[ {title} ]"
        header += "─" * (102 - len(header) + 1) + "┐"
    else:
        header = "┌" + "─" * 102 + "┐"
        
    framed = [header]
    for line in lines:
        # Check actual length of string
        content = line.rstrip()
        # Handle trailing space if it was empty, but keep left spacing
        rem = 102 - len(content)
        if rem < 0:
            # truncate if somehow too long, though we design them to fit
            content = content[:102]
            rem = 0
        framed.append(f"│{content}{' ' * rem}│")
    framed.append("└" + "─" * 102 + "┘")
    return "\n".join(framed)

# 1. Header diagnostics & links block (104 chars wide)
header_box = """╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ W A L I   M E D U G U  //  S Y S T E M   I N T E R F A C E                                           ║
║ [STATUS: ACTIVE]  [PORTFOLIO: INDEX N° 001]  [IP: 9.07° N (ABUJA, NG)]                               ║
╠══════════════════════════════════════╦═══════════════════════════════════════════════════════════════╣
║  SYSTEM DIAGNOSTICS                  ║  CONNECTION PATHWAYS                                          ║
║  ├─ OS      : WALI.SYS v3.0          ║  ├─ [01] PORTFOLIO  :: https://wali-blog.vercel.app           ║
║  ├─ UPTIME  : 23,892 HR              ║  ├─ [02] BLOG       :: https://wali-blog.vercel.app/blog.html ║
║  ├─ STATUS  : ACTIVE (BUILDING)      ║  ├─ [03] GITHUB     :: https://github.com/WaliMedugu          ║
║  ├─ TEMP    : 36.8°C (NOMINAL)       ║  ├─ [04] YOUTUBE    :: https://youtube.com/@notevenwali       ║
║  ├─ CORES   : 16x HYPER-THREADS      ║  ├─ [05] INSTAGRAM  :: https://instagram.com/w_wali_i         ║
║  ├─ NETWORK : ONLINE // SECURE       ║  ├─ [06] TIKTOK     :: https://tiktok.com/@w_wali_i           ║
║  └─ LOC     : Abuja, NG              ║  └─ [07] EMAIL      :: mailto:blueparticlestudios@gmail.com   ║
╠══════════════════════════════════════╩═══════════════════════════════════════════════════════════════╣
║ [CPU LOAD] [██████████████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░] 74%              ║
║ [MEM LOAD] [██████████████████████████████████████████████████████████░░░░░░░░░░░░] 85%              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝"""

# 2. Whoami block formatted
whoami_lines = [
    "",
    " Software Engineer, Creative Director, and Activist.",
    " building across the stack — Flutter · Node.js · Supabase · Python · Firebase · D3.js.",
    " drawn to projects where design meets human psychology. building highly refined user experiences.",
    "",
    " [FOCUS]  Flutter & Mobile · Full-Stack Systems · Data Visualizations · AI Life OS",
    " [STATUS] building Arguuu & Blue Particle Studios",
    " [CLUBS]  Team Tensor — Wema Bank Hackaholics Winner",
    ""
]
whoami_box = frame_block("WHOAMI", whoami_lines)

# 3. System map (centered, double borders, highly aligned)
system_map = """                                     ╔═════════════════════╗
                                     ║      WALI.SYS       ║
                                     ║  Lead & Architect   ║
                                     ╚══════════╦══════════╝
                                                ║
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                      ▼                                      ▼
╔══════════════════════╗              ╔══════════════════════╗              ╔══════════════════════╗
║     MOBILE & WEB     ║              ║     GRAPH & DATA     ║              ║     STUDIO CORE      ║
╠══════════════════════╣              ╠══════════════════════╣              ╠══════════════════════╣
║ ├─ arguuu            ║              ║ ├─ bloodline         ║              ║ ├─ spaver            ║
║ ├─ wherearethey      ║              ║ └─ aumen             ║              ║ ├─ beacora           ║
║ └─ femn              ║              ╚══════════════════════╝              ║ ├─ vita              ║
╚══════════════════════╝                                                    ║ └─ walletpaddi       ║
         │                                                                  ╚══════════╦═══════════╝
         └──────────────────────────────────────┬──────────────────────────────────────┘
                                                ▼
                                     ╔══════════════════════════════════════╗
                                     ║ COMMUNITY & TEACHING                 ║
                                     ╠══════════════════════════════════════╣
                                     ║ ├─ blue particle (Custom App Studio) ║
                                     ║ ├─ talk about it (Mental Health Group║
                                     ║ └─ kids bootcamp (Coding Curriculum) ║
                                     ╚══════════════════════════════════════╝"""

# 4. Project Archive block (15 projects)
project_list = [
    ("ARGUUU", "Mobile & Web", [
        "     - A real-time, 1v1 competitive structured debate mobile and web app.",
        "     - Tech: FLUTTER · SUPABASE · DART · CHESS CLOCK · GAMIFICATION",
        "     - Info: Turn-based chess clock, live audience voting, Elo-based ratings."
    ]),
    ("BLOODLINE", "Graph & Data", [
        "     - Software supply chain contagion mapper modeling vulnerability propagation.",
        "     - Tech: NODE.JS · D3.JS · DIRECTED GRAPHS · BFS / DFS · VULNERABILITY MODELING",
        "     - Info: Models velocities through directed graph network visualizations."
    ]),
    ("BLUE PARTICLE STUDIOS", "Studio Core", [
        "     - Founder & Lead Coordinator running client app commission pipelines.",
        "     - Tech: MOBILE APPS · WEB CLIENTS · COMMISSIONS · DEV OPERATIONS",
        "     - Info: Manages delivery operations across Core/Foundation/Signature tiers."
    ]),
    ("WALLETPADDI", "Studio Core", [
        "     - Team Lead of Team Tensor; won first place at Hackaholics 6.0 regional.",
        "     - Tech: FLUTTER · DART · FINTECH · HACKAHOLICS 6.0 · AWARD WINNING",
        "     - Info: Engineered secure payment transacting and banking workflows."
    ]),
    ("WHEREARETHEY", "Mobile & Web", [
        "     - Live, crowdsourced missing persons digital directory for Nigeria.",
        "     - Tech: FLUTTER WEB · SUPABASE · GEOSPATIAL · SOCIAL IMPACT · REAL-TIME",
        "     - Info: Engineered for quick spatial lookups with robust database layer."
    ]),
    ("FEMN", "Mobile & Web", [
        "     - Politically neutral, civic social activism mobile app for advocacy.",
        "     - Tech: FLUTTER · DART · FIREBASE · SOCIAL ACTIVISM · CODE OPTIMIZATION",
        "     - Info: Converted React version to a optimized ~2,100-line single file."
    ]),
    ("AUMEN", "Graph & Data", [
        "     - AI-powered productivity application designed as a personalized Life OS.",
        "     - Tech: PRODUCTIVITY · PITCH DECK · LIFE OS · STARTUP PITCH · PROTOTYPING",
        "     - Info: Presented prototype at Nile University Startup Competition 6.0."
    ]),
    ("SPAVER", "Studio Core", [
        "     - Financial expense-tracker with automated local UBA SMS transaction parsing.",
        "     - Tech: FLUTTER · DART · SQLITE · SMS PARSING · LOCAL STORAGE",
        "     - Info: SQLite storage backend with custom Android dynamic shortcuts."
    ]),
    ("BEACORA", "Studio Core", [
        "     - Location-based safety app designed with offline Bluetooth & SMS alerts.",
        "     - Tech: FLUTTER · OFFLINE CONNECTIVITY · BLUETOOTH LE · SMS ALERTS",
        "     - Info: Distributed directly via personal site for offline resilience."
    ]),
    ("VITA", "Studio Core", [
        "     - NFC-based health identity combining funding and SMS bot interface.",
        "     - Tech: FLUTTER · NFC · OPAY HACKATHON · GOOGLE CLOUD · SMS BOT",
        "     - Info: Built and delivered complete UI prototype for Google/OPay."
    ]),
    ("CLASSROOM ALLOCATION SYSTEM", "Full-Stack", [
        "     - Automated academic examination seating database and allocation system.",
        "     - Tech: SQL · DATABASE DESIGN · EXAMINATION SCHEDULING · TEAM LEAD",
        "     - Info: Served as Team Lead organizing examinee seating distributions."
    ]),
    ("LEGUIDE", "Mobile & Web", [
        "     - Tutoring marketplace user interface connecting tutors with students.",
        "     - Tech: FLUTTER · DART · MARKETPLACE · UI DESIGN",
        "     - Info: Implemented search profiles, rating views, scheduling interfaces."
    ]),
    ("OCEAN BASKET NIGERIA", "Mobile & Web", [
        "     - 3D promotional web interface using advanced graphics libraries.",
        "     - Tech: VITE · THREE.JS · GSAP · WebGL · 3D WEB",
        "     - Info: Engineered with custom shaders for high-performance 3D rendering."
    ]),
    ("HARBOR HAVEN FOUNDATION", "Mobile & Web", [
        "     - Complete 7-page responsive web platform built for nonprofit.",
        "     - Tech: HTML · CSS · JAVASCRIPT · NONPROFIT · WEB DESIGN",
        "     - Info: Features donation integrations, content pages, media galleries."
    ]),
    ("KIDS CODING BOOTCAMP", "Community/Teach", [
        "     - Designed curriculum for 1-month coding bootcamp for ages 6-12.",
        "     - Tech: CURRICULUM DESIGN · DARTPAD · FLUTLAB · MOBILE DEV",
        "     - Info: Led 60 training hours; students built functional mobile apps."
    ])
]

project_lines = [
    "",
    "  PROJECT ARCHIVE (15 ACTIVE NODES)",
    "  " + "─" * 98,
    ""
]

for idx, (name, cat, desc_list) in enumerate(project_list, 1):
    prefix = f"  [{idx:02d}] {name} "
    suffix = f" [{cat}]"
    fill_len = 98 - len(prefix) - len(suffix)
    title_line = f"  {prefix}{'─' * fill_len}{suffix}"
    project_lines.append(title_line)
    for desc in desc_list:
        project_lines.append(f"  {desc.rstrip()}")
    project_lines.append("")

projects_box = frame_block("PROJECTS", project_lines[:-1])

# 5. Development route & experience
dev_route_lines = [
    "",
    "  2026 ──●  BLUE PARTICLE STUDIOS ── [Founder & Lead Coordinator]",
    "         │  Managing customized app pipeline across Core/Foundation/Signature tiers.",
    "         │  ",
    "  2026 ──●  CODE CAMPUS (STYCLICK) ── [Full-Stack Developer Intern]",
    "         │  Specialized in Provider state management and full-stack app features.",
    "         │",
    "  2025 ──●  FIRS GOOGLE MAPS ── [Technical Trainer (Lagos)]",
    "         │  Instructed fleet drivers; optimized Lagos-wide navigation layouts.",
    "         │",
    "  2024 ──●  NILE UNIVERSITY OF NIGERIA ── [Software Engineering Track]",
    "            Team Tensor Lead; won Wema Bank Hackaholics 6.0 regional finals.",
    ""
]
dev_route_box = frame_block("DEVELOPMENT ROUTE & EXPERIENCE", dev_route_lines)

# 6. Technical Stack & Utilities
stack_lines = [
    "",
    "  [LANGUAGES] ──── Dart · JavaScript · TypeScript · Python · SQL · SQLite",
    "  [MOBILE] ─────── Flutter (Mobile & Web) · Firebase · Supabase · Provider",
    "  [WEB] ────────── Node.js · Three.js · Vite · GSAP · Express · HTML/CSS",
    "  [DATA] ───────── Supabase · PostgreSQL · Firebase Firestore · SQLite",
    "  [AI] ─────────── OpenAI API · Vosk/google_speech (Offline Voice Assistant)",
    "  [TERMINAL] ───── AutoHotkey automations · Git · CLI / Shell script pipelines",
    "  [TOOLING] ────── Figma · Git · Docker · Notion · Postman · Android Studio",
    ""
]
stack_box = frame_block("TECHNICAL STACK & UTILITIES", stack_lines)

# 7. System status (double border terminal status window)
system_status = """╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ SYSTEM STATUS INTERFACE                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ STATUS   ▸ BUILDING (Probably in an editor, past midnight)                                           ║
║ SESSION  ▸ ACTIVE LOGS // STYCLICK RUNNING                                                           ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ wali-blog.vercel.app  ·  Abuja, NG  ·  © 2026 // ALL SYSTEMS OPERATIONAL                             ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝"""

readme_content = f"""```text
{wali_ascii}
```

<div align="center">
  <img src="assets/avatar.png" width="800" alt="Wali Medugu" />
</div>

```text
{header_box}
```

## 01 // WHOAMI

```text
{whoami_box}
```

## 02 // SYSTEM MAP

```text
{system_map}
```

## 03 // PROJECTS

```text
{projects_box}
```

## 04 // DEVELOPMENT ROUTE & EXPERIENCE

```text
{dev_route_box}
```

## 05 // TECHNICAL STACK & UTILITIES

```text
{stack_box}
```

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=dart,flutter,js,ts,py,postgres,sqlite,firebase,supabase,nodejs,express,threejs,vite,html,css,figma,git,github,docker,notion,postman,androidstudio)](https://skillicons.dev)

</div>

## 06 // SYSTEM STATUS

```text
{system_status}
```

<div align="center">
  <img src="assets/main.gif" width="800" alt="Main Animation" />
</div>
"""

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"Successfully updated {readme_path}")
