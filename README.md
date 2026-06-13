========================================================================================
███████╗ █████╗ ██╗     ██╗███████╗     █████╗ ██╗
██╔════╝██╔══██╗██║     ██║╚══███╔╝    ██╔══██╗██║
█████╗  ███████║██║     ██║  ███╔╝     ███████║██║
██╔══╝  ██╔══██║██║     ██║ ███╔╝      ██╔══██║██║
██║     ██║  ██║███████╗██║███████╗    ██║  ██║██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝
========================================================================================
 [ SYSTEM ]: FALIZ AI PLATFORM                            [ ENVIRONMENT ]: TERMINAL UI
 [ MATRIX ]: v3.2_STABLE_RELEASE                          [ DEVELOPER   ]: FAHAD
========================================================================================
  >> INITIALIZING INTEGRATED COGNITIVE NETWORK...
  >> CONNECTING TO AUTONOMOUS REASONING LAYER... SUCCESS
  +---------------------------------[ SYSTEM ARCHITECTURE ]----------------------------+
  |                                                                                    |

| [ FALIZ AI ] ------> ( Agent_01: Orchestrator ) ----> [ Neural Net ] |
| :--- | :--- |
| +------------> ( Agent_02: Memory Matrix ) ---> [ Knowledge Base ] |
| :--- | :--- |
| +------------> ( Agent_03: Execution Hub ) ---> [ Vision & Code UI ] |
| :--- |

  +------------------------------------------------------------------------------------+
  [STATUS]: ACTIVE MULTI-AGENT SWARM // STANDBY FOR COMMAND...



# FALIZ AI — Your Life, Intelligently Orchestrated

**Version:** 1.0.0-production  
**Codename:** ORACLE  
**Status:** Production-Ready

## Table of Contents

- [What is FALIZ?](#what-is-faliz)
- [Architecture at a Glance](#architecture-at-a-glance)
- [Quick Start](#quick-start)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Plugin Modules](#plugin-modules-16-total)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Design System](#design-system)
- [Security](#security)
- [Development](#development)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Support](#support)

## What is FALIZ?

FALIZ is an ultra-intelligent personal AI operating system for desktop. It combines:

- **Voice-first interface** with always-on wake word detection
- **Proactive intelligence** that anticipates needs before you ask
- **Seamless integrations** with 100+ services (Google, Slack, Spotify, Home Assistant, etc.)
- **Multi-step task orchestration** powered by GPT-4o reasoning
- **Long-term memory** with vector-based semantic search
- **Beautiful desktop shell** (Electron) with cinematic design

## Architecture at a Glance

```
┌─────────────────────────────────────────────────────────────┐
│                     FALIZ Desktop Shell                      │
│                    (Electron + React)                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────┐     ┌──────────────┐      ┌──────────────┐   │
│  │ Sidebar  │────▶│  Orb Sphere  │◀────│ Right Panel  │   │
│  │ Nav      │     │  Conversation│     │ Widgets      │   │
│  └──────────┘     └──────────────┘     └──────────────┘   │
│                                                               │
├─────────────────────────────────────────────────────────────┤
│              Voice Input / Text Input Bar                     │
└─────────────────────────────────────────────────────────────┘
             ↕ WebSocket + REST + SSE
┌─────────────────────────────────────────────────────────────┐
│              FastAPI Backend (Python 3.12)                  │
├──────────┬──────────┬──────────┬──────────┬────────────────┤
│ AI Brain │ Voice    │ Calendar │ Tasks    │ 12+ Plugins    │
│ (Brain)  │ (Voice)  │ (Events) │ (Org)    │ (Integrated)   │
└──────────┴──────────┴──────────┴──────────┴────────────────┘
        ↕ Async ORM ↕ Vector Store ↕ Pub/Sub
┌────────────────┬────────────────┬────────────────┐
│  PostgreSQL    │     Redis      │    ChromaDB    │
│  (Primary DB)  │  (Cache/Queue) │  (Embeddings)  │
└────────────────┴────────────────┴────────────────┘
```

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 20+
- Python 3.12+
- OpenAI API key

### Development Environment

```bash
# Clone and setup
git clone https://github.com/FALIZ-AI/FALIZ-AI.git
cd FALIZ-AI

# Copy environment template
cp .env.example .env
# Edit .env with your API keys

# Start full stack
make dev

# In another terminal, start Electron desktop shell
cd apps/desktop
npm install
npm run dev
```

The app will be available at `http://localhost:5173` and the Electron window will auto-connect.

### Production Build

```bash
make build
make test
make docker-build
```

## Tech Stack

### Frontend
- **React 18** + TypeScript (strict mode)
- **Vite 5** build tool
- **TailwindCSS 3.4** + shadcn/ui
- **Framer Motion 11** for animations
- **Redux Toolkit 2** + RTK Query
- **Socket.io** real-time sync

### Desktop Shell
- **Electron 31** (cross-platform)
- **electron-builder** packaging
- **System tray** integration
- **Auto-updater** support

### Backend
- **FastAPI 0.111** (Python 3.12)
- **SQLAlchemy 2.0** async ORM
- **LangChain 0.2** + LangGraph agent
- **PostgreSQL 16** primary DB
- **Redis 7.2** cache + pub/sub
- **ChromaDB** vector embeddings

### AI/LLM
- **OpenAI GPT-4o** (primary reasoning + vision)
- **text-embedding-3-large** (embeddings)
- **Whisper API** (speech-to-text)
- **ElevenLabs** (text-to-speech)
- **DALL-E 3** (image generation)

## Project Structure

```
faliz-ai/
├── apps/
│   ├── desktop/          # Electron shell
│   ├── frontend/         # React UI (Vite)
│   └── backend/          # FastAPI server
├── packages/
│   ├── faliz-core/       # Shared AI logic
│   ├── faliz-plugins/    # All feature modules
│   ├── faliz-voice/      # Voice pipeline
│   ├── faliz-memory/     # Vector memory
│   └── faliz-ui/         # Shared components
├── infra/
│   ├── docker/           # Container configs
│   ├── nginx/            # Reverse proxy
│   └── scripts/          # Deployment helpers
├── tests/                # Test suites
└── docs/                 # Documentation
```

## Plugin Modules (16 Total)

1. **Voice Engine** — Always-on wake word, STT/TTS, VAD
2. **AI Brain** — LangGraph orchestration, reasoning, memory
3. **Calendar & Time** — Google Calendar, scheduling, briefings
4. **Tasks & Productivity** — GTD, time tracking, Pomodoro
5. **Communications** — Gmail triage, SMS, Slack/Teams
6. **Weather & News** — OpenWeather, NewsAPI, RSS
7. **System Control** — App launch, metrics, processes, clipboard
8. **Smart Home** — Home Assistant integration, automation
9. **Computer Vision** — Webcam analysis, facial recognition
10. **Content Creation** — DALL-E, PowerPoint, blog drafts
11. **Knowledge & Documents** — PDF Q&A, notes, meetings
12. **Career & Professional** — Resume analyzer, interview coach
13. **Entertainment** — Spotify, YouTube, games, story mode
14. **Navigation & Location** — Google Maps, traffic, travel
15. **Security** — Face auth, encryption vault, audit logs
16. **Analytics Dashboard** — Productivity scoring, KPIs

## API Endpoints

### Core
- `POST /api/v1/auth/google` — OAuth2 login
- `POST /api/v1/chat/message` — Send message (streaming)
- `GET /api/v1/chat/history` — Conversation history
- `WebSocket /api/v1/voice/stream` — Real-time voice I/O

### Tasks
- `GET /api/v1/tasks` — List tasks
- `POST /api/v1/tasks` — Create task
- `PATCH /api/v1/tasks/{id}` — Update task

### Calendar
- `GET /api/v1/calendar/events` — List events
- `POST /api/v1/calendar/events` — Create event (NL)
- `GET /api/v1/calendar/free-slots` — Find meeting time

### System
- `GET /api/v1/system/metrics` — CPU/RAM/disk/network
- `POST /api/v1/system/screenshot` — Capture + OCR
- `GET /health` — Service health check

Full API docs at `http://localhost:8000/docs` (Swagger)

## Configuration

All secrets and settings via environment variables (`.env`):

```bash
# Core
APP_ENV=development
SECRET_KEY=<64-char-random-hex>
JWT_SECRET=<64-char-random-hex>

# Databases
DATABASE_URL=postgresql+asyncpg://faliz:password@db:5432/faliz
REDIS_URL=redis://redis:6379/0

# AI/LLM
OPENAI_API_KEY=<your-key>
OPENAI_MODEL=gpt-4o

# Voice
ELEVENLABS_API_KEY=<your-key>
PICOVOICE_ACCESS_KEY=<your-key>

# Google Services
GOOGLE_CLIENT_ID=<from-console>
GOOGLE_CLIENT_SECRET=<from-console>

# Features (toggle plugins)
PLUGIN_VOICE_ENABLED=true
PLUGIN_CALENDAR_ENABLED=true
# ... more in .env.example
```

## Design System

### Theme: "DEEP ORACLE"

**Color Palette:**
- **Void**: `#080A0F` (background)
- **Surface**: `#0E1118` (panels)
- **Oracle Amber**: `#F5A623` (primary accent)
- **Cyber Cyan**: `#00D4FF` (active state)

**Typography:**
- Display: Syne (futuristic)
- Body: Inter (readable)
- Code: JetBrains Mono

**Central Orb:**
- States: IDLE, LISTENING, THINKING, SPEAKING, ERROR
- Animations: breathing pulse, amplitude rings, particle orbits
- Canvas-based for performance

## Security

✓ OAuth2 (Google + GitHub)  
✓ JWT access + refresh tokens  
✓ AES-256-GCM encryption (at-rest)  
✓ Face authentication for sensitive actions  
✓ Rate limiting (slowapi + Redis)  
✓ Audit logging (every AI action)  
✓ CORS + CSP headers  
✓ No hardcoded secrets  

## Development

### Run Tests

```bash
# Backend tests
cd apps/backend
pytest tests/ -v

# Frontend tests
cd apps/frontend
npm run test
```

### Code Quality

```bash
# Format code
make format

# Lint
make lint

# Type check
make type-check
```

### Database Migrations

```bash
# Create migration
cd apps/backend
alembic revision --autogenerate -m "Add new table"

# Apply migration
alembic upgrade head
```

## Deployment

### Docker Compose (Production)

```bash
docker-compose -f docker-compose.yml up -d
```

Includes:
- FastAPI backend
- PostgreSQL
- Redis
- ChromaDB
- Nginx reverse proxy
- Health checks on all services

### CI/CD Pipeline

GitHub Actions automatically:
1. Runs tests on PR
2. Builds Docker images
3. Pushes to registry
4. Deploys to staging
5. Manual approval for production

See `.github/workflows/` for details.

## Troubleshooting

### Backend won't start
```bash
# Check logs
docker-compose logs backend

# Verify database connection
psql -h localhost -U faliz -d faliz

# Check Redis
redis-cli ping
```

### Voice not working
```bash
# Check microphone access
pactl list sources

# Test Whisper API
curl -X POST https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "file=@audio.wav" \
  -F "model=whisper-1"
```

### Frontend can't reach backend
```bash
# Verify backend is running
curl http://localhost:8000/health

# Check CORS headers
curl -I http://localhost:8000/api/v1/chat/history
```

## Contributing

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes
3. Run tests and lint: `make test && make lint`
4. Commit: `git commit -am 'Add feature'`
5. Push: `git push origin feature/your-feature`
6. Open PR

## License

MIT License — See LICENSE file

## Support

- 📖 [Documentation](./docs/)
- 🐛 [Report Issues](https://github.com/FALIZ-AI/FALIZ-AI/issues)
- 💬 [Discussions](https://github.com/FALIZ-AI/FALIZ-AI/discussions)
- 📧 support@faliz.ai

---

**Made by FALIZ Team**  
*Your life, intelligently orchestrated.*
