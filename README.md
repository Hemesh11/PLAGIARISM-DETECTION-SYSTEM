# 🏗️ Plagiarism Detection System - Architecture Overview

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT TIER (Frontend)                             │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐            │
│  │   Login.jsx     │    │   Upload.jsx    │    │   App.jsx       │            │
│  │                 │    │                 │    │                 │            │
│  │ • User Auth     │    │ • File Upload   │    │ • Routing       │            │
│  │ • Form Submit   │    │ • Results       │    │ • State Mgmt    │            │
│  │ • Navigation    │    │ • Visualization │    │ • Components    │            │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘            │
│           │                       │                       │                     │
│           └───────────────────────┼───────────────────────┘                     │
│                                   │                                             │
│  ┌─────────────────────────────────┼─────────────────────────────────┐          │
│  │                React Router     │                                 │          │
│  │  Routes: "/" → Login           │                                 │          │
│  │         "/upload" → Upload     │                                 │          │
│  └─────────────────────────────────┼─────────────────────────────────┘          │
│                                   │                                             │
│  ┌─────────────────────────────────┼─────────────────────────────────┐          │
│  │                Axios HTTP Client │                                │          │
│  │  • POST /login                 │                                 │          │
│  │  • POST /upload                │                                 │          │
│  │  • withCredentials: true       │                                 │          │
│  └─────────────────────────────────┼─────────────────────────────────┘          │
│                                   │                                             │
└───────────────────────────────────┼─────────────────────────────────────────────┘
                                    │
                          ┌─────────┴─────────┐
                          │   CORS HEADERS    │
                          │ Access-Control-   │
                          │ Allow-Origin      │
                          │ Allow-Credentials │
                          └─────────┬─────────┘
                                    │
┌───────────────────────────────────┼─────────────────────────────────────────────┐
│                              SERVER TIER (Backend)                             │
├───────────────────────────────────┼─────────────────────────────────────────────┤
│                                   │                                             │
│  ┌─────────────────────────────────┼─────────────────────────────────┐          │
│  │                Flask Application │                                │          │
│  │                                │                                 │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │          │
│  │  │   app.py    │  │ database.py │  │similarity.py│               │          │
│  │  │             │  │             │  │             │               │          │
│  │  │• Routes     │  │• DB Setup   │  │• Text Ext.  │               │          │
│  │  │• Auth Logic │  │• User Mgmt  │  │• TF-IDF     │               │          │
│  │  │• Sessions   │  │• Connection │  │• Cosine Sim │               │          │
│  │  └─────────────┘  └─────────────┘  └─────────────┘               │          │
│  │                                │                                 │          │
│  └─────────────────────────────────┼─────────────────────────────────┘          │
│                                   │                                             │
│  ┌─────────────────────────────────┼─────────────────────────────────┐          │
│  │              Session Management │                                 │          │
│  │  • Flask-Session               │                                 │          │
│  │  • Server-side storage         │                                 │          │
│  │  • Cookie-based auth           │                                 │          │
│  └─────────────────────────────────┼─────────────────────────────────┘          │
│                                   │                                             │
│  ┌─────────────────────────────────┼─────────────────────────────────┐          │
│  │              File Processing    │                                 │          │
│  │                                │                                 │          │
│  │  1. PDF Upload → uploads/      │                                 │          │
│  │  2. Text Extract (PyMuPDF)     │                                 │          │
│  │  3. TF-IDF Vectorization       │                                 │          │
│  │  4. Similarity Matrix          │                                 │          │
│  │  5. JSON Response              │                                 │          │
│  └─────────────────────────────────┼─────────────────────────────────┘          │
│                                   │                                             │
└───────────────────────────────────┼─────────────────────────────────────────────┘
                                    │
┌───────────────────────────────────┼─────────────────────────────────────────────┐
│                              DATA TIER                                         │
├───────────────────────────────────┼─────────────────────────────────────────────┤
│                                   │                                             │
│  ┌─────────────────────────────────┼─────────────────────────────────┐          │
│  │              SQLite Database    │                                 │          │
│  │                                │                                 │          │
│  │  ┌─────────────────────────────┐│                                 │          │
│  │  │         users table         ││                                 │          │
│  │  │  ┌─────┬──────────┬────────┐││                                 │          │
│  │  │  │ id  │ username │password│││                                 │          │
│  │  │  ├─────┼──────────┼────────┤││                                 │          │
│  │  │  │ 1   │  admin   │password│││                                 │          │
│  │  │  └─────┴──────────┴────────┘││                                 │          │
│  │  └─────────────────────────────┘│                                 │          │
│  └─────────────────────────────────┼─────────────────────────────────┘          │
│                                   │                                             │
│  ┌─────────────────────────────────┼─────────────────────────────────┐          │
│  │              File System        │                                 │          │
│  │                                │                                 │          │
│  │  uploads/                      │                                 │          │
│  │  ├── document1.pdf             │                                 │          │
│  │  ├── document2.pdf             │                                 │          │
│  │  └── document3.pdf             │                                 │          │
│  │                                │                                 │          │
│  │  flask_session/                │                                 │          │
│  │  ├── session_id_1              │                                 │          │
│  │  └── session_id_2              │                                 │          │
│  └─────────────────────────────────┼─────────────────────────────────┘          │
│                                   │                                             │
└───────────────────────────────────┴─────────────────────────────────────────────┘
```

## Data Flow Architecture

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│    User      │    │   Frontend   │    │   Backend    │    │   Database   │
│   Browser    │    │   (React)    │    │   (Flask)    │    │  (SQLite)    │
└──────┬───────┘    └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
       │                   │                   │                   │
       │ 1. Navigate to /  │                   │                   │
       ├──────────────────→│                   │                   │
       │                   │                   │                   │
       │ 2. Login Form     │                   │                   │
       ├──────────────────→│                   │                   │
       │                   │                   │                   │
       │                   │ 3. POST /login    │                   │
       │                   ├──────────────────→│                   │
       │                   │                   │                   │
       │                   │                   │ 4. Validate User  │
       │                   │                   ├──────────────────→│
       │                   │                   │                   │
       │                   │                   │ 5. User Found     │
       │                   │                   │←──────────────────┤
       │                   │                   │                   │
       │                   │ 6. Session Cookie │                   │
       │                   │←──────────────────┤                   │
       │                   │                   │                   │
       │ 7. Redirect /upload│                  │                   │
       │←──────────────────┤                   │                   │
       │                   │                   │                   │
       │ 8. Select Files   │                   │                   │
       ├──────────────────→│                   │                   │
       │                   │                   │                   │
       │                   │ 9. POST /upload   │                   │
       │                   │   FormData        │                   │
       │                   ├──────────────────→│                   │
       │                   │                   │                   │
       │                   │                   │ 10. Save Files    │
       │                   │                   │ uploads/ folder   │
       │                   │                   │                   │
       │                   │                   │ 11. Extract Text  │
       │                   │                   │ (PyMuPDF)         │
       │                   │                   │                   │
       │                   │                   │ 12. TF-IDF        │
       │                   │                   │ Vectorization     │
       │                   │                   │                   │
       │                   │                   │ 13. Calculate     │
       │                   │                   │ Similarity Matrix │
       │                   │                   │                   │
       │                   │ 14. JSON Report   │                   │
       │                   │←──────────────────┤                   │
       │                   │                   │                   │
       │ 15. Display Results│                  │                   │
       │    & Visualization │                  │                   │
       │←──────────────────┤                   │                   │
       │                   │                   │                   │
```

## Component Architecture

### Frontend Component Hierarchy
```
App.jsx (Root Component)
├── Router
    ├── Route "/" → Login.jsx
    │   ├── useState (username, password)
    │   ├── axios.post('/login')
    │   └── navigate('/upload')
    │
    └── Route "/upload" → Upload.jsx
        ├── useState (files, report)
        ├── handleFileChange()
        ├── handleUpload()
        ├── axios.post('/upload')
        └── ResponsiveContainer
            └── ComposedChart (Recharts)
```

### Backend Module Architecture
```
app.py (Main Flask Application)
├── Flask Configuration
│   ├── CORS Setup
│   ├── Session Configuration
│   └── Secret Key
│
├── Routes
│   ├── /login (POST)
│   │   ├── User Validation
│   │   ├── Session Creation
│   │   └── JSON Response
│   │
│   ├── /upload (POST)
│   │   ├── File Reception
│   │   ├── Text Processing
│   │   ├── Similarity Calculation
│   │   └── Report Generation
│   │
│   └── /logout (GET)
│       └── Session Destruction
│
├── database.py
│   ├── SQLite Connection
│   ├── User Table Creation
│   └── Default User Insert
│
└── similarity.py
    ├── extract_text_from_pdf()
    ├── calculate_similarity()
    └── generate_similarity_report()
```

## Technology Stack Integration

```
┌─────────────────────────────────────────────────────────────────┐
│                     DEVELOPMENT ENVIRONMENT                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Frontend Development          Backend Development              │
│  ┌─────────────────────┐      ┌─────────────────────┐          │
│  │       Vite          │      │     Python 3.x      │          │
│  │  ┌───────────────┐  │      │  ┌───────────────┐  │          │
│  │  │ Hot Reloading │  │      │  │ Flask Server  │  │          │
│  │  │ Fast Builds   │  │      │  │ Debug Mode    │  │          │
│  │  │ ES Modules    │  │      │  │ Auto Restart  │  │          │
│  │  └───────────────┘  │      │  └───────────────┘  │          │
│  └─────────────────────┘      └─────────────────────┘          │
│           │                             │                      │
│           │ npm run dev                 │ python app.py        │
│           ↓                             ↓                      │
│  ┌─────────────────────┐      ┌─────────────────────┐          │
│  │   localhost:5173    │      │   localhost:5000    │          │
│  │   (Frontend)        │      │   (Backend API)     │          │
│  └─────────────────────┘      └─────────────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Security Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        SECURITY LAYERS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 Frontend Security                       │    │
│  │  • Input Validation                                     │    │
│  │  • XSS Prevention (React's built-in protection)        │    │
│  │  • Secure HTTP Headers                                 │    │
│  │  • withCredentials for CORS                            │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                ↓                                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 Transport Security                      │    │
│  │  • HTTPS (Production)                                   │    │
│  │  • CORS Configuration                                   │    │
│  │  • Cookie Security                                      │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                ↓                                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 Backend Security                        │    │
│  │  • Session Management                                   │    │
│  │  • SQL Injection Prevention (Parameterized Queries)    │    │
│  │  • File Upload Validation                               │    │
│  │  • Secret Key Protection                                │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                ↓                                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 Database Security                       │    │
│  │  • SQLite File Permissions                              │    │
│  │  • Password Storage (Plain text - Need improvement)     │    │
│  │  • User Input Sanitization                              │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Machine Learning Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    TEXT PROCESSING PIPELINE                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PDF Files → Text Extraction → Preprocessing → Vectorization   │
│                                                                 │
│  ┌─────────┐    ┌─────────────┐    ┌─────────────┐              │
│  │Document1│    │   PyMuPDF   │    │   Raw Text  │              │
│  │Document2│ ──→│ fitz.open() │──→ │   Content   │              │
│  │Document3│    │page.get_text│    │   Strings   │              │
│  └─────────┘    └─────────────┘    └─────────────┘              │
│                                            │                    │
│                                            ↓                    │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              TF-IDF VECTORIZATION                       │    │
│  │                                                         │    │
│  │  Text₁: "The quick brown fox..."                       │    │
│  │  Text₂: "A quick brown animal..."                      │    │
│  │  Text₃: "The slow brown fox..."                        │    │
│  │                          ↓                             │    │
│  │  TfidfVectorizer().fit_transform([Text₁, Text₂, Text₃])│    │
│  │                          ↓                             │    │
│  │  Vector₁: [0.2, 0.8, 0.1, 0.9, ...]                  │    │
│  │  Vector₂: [0.1, 0.7, 0.2, 0.8, ...]                  │    │
│  │  Vector₃: [0.3, 0.6, 0.1, 0.9, ...]                  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                            │                    │
│                                            ↓                    │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              SIMILARITY CALCULATION                     │    │
│  │                                                         │    │
│  │  Cosine Similarity Matrix:                             │    │
│  │  ┌─────────────────────────────────────────────────┐   │    │
│  │  │        Doc1    Doc2    Doc3                     │   │    │
│  │  │  Doc1   1.0    0.85   0.92                     │   │    │
│  │  │  Doc2   0.85   1.0    0.73                     │   │    │
│  │  │  Doc3   0.92   0.73   1.0                     │   │    │
│  │  └─────────────────────────────────────────────────┘   │    │
│  │                                                         │    │
│  │  Pairwise Comparisons:                                 │    │
│  │  • Doc1 vs Doc2: 85% similarity                       │    │
│  │  • Doc1 vs Doc3: 92% similarity                       │    │
│  │  • Doc2 vs Doc3: 73% similarity                       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Key Architectural Decisions

### 1. **Separation of Concerns**
- **Frontend**: User interface and user experience
- **Backend**: Business logic and data processing
- **Database**: Data persistence

### 2. **Stateless API Design**
- RESTful endpoints
- JSON communication
- Session-based authentication

### 3. **Modular Backend Structure**
- `app.py`: Main application and routing
- `similarity.py`: ML algorithms and text processing
- `database.py`: Database operations

### 4. **Client-Side Routing**
- React Router for navigation
- Component-based architecture
- State management with hooks

### 5. **File Processing Strategy**
- Server-side file storage
- In-memory text processing
- Real-time similarity calculation

This architecture provides a scalable, maintainable, and efficient plagiarism detection system with clear separation between presentation, business logic, and data layers.
