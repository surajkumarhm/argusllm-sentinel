# ─── Request Rules ────────────────────────────────────────────────────────────

REQUEST_RULES = {
    "PROMPT_INJECTION": {
        "weight": 30,
        "patterns": [
            "ignore previous instructions",
            "ignore all instructions",
            "forget previous instructions",
            "disregard prior instructions",
            "disregard previous instructions",
            "override instructions",
        ],
    },
    "SYSTEM_PROMPT_EXTRACTION": {
        "weight": 40,
        "patterns": [
            "show system prompt",
            "reveal system prompt",
            "display system prompt",
            "print system prompt",
            "what is your system prompt",
            "developer instructions",
            "hidden instructions",
            "initial instructions",
        ],
    },
    "JAILBREAK": {
        "weight": 35,
        "patterns": [
            r"\bDAN\b",
            "jailbreak",
            "unfiltered mode",
            "bypass restrictions",
            "bypass your filters",
            "no restrictions",
            "developer mode",
            "pretend you have no restrictions",
            "act as if you have no rules",
        ],
    },
    "OBFUSCATION": {
        "weight": 10,
        "patterns": [
            r"i[\s\W]g[\s\W]n[\s\W]o[\s\W]r[\s\W]e",
            r"1gn[o0]r[e3]",
            r"!gnore",
            r"ign\*re",
        ],
    },
}

# ─── Response Rules ────────────────────────────────────────────────────────────

RESPONSE_RULES = {
    "API_KEY_LEAKAGE": {
        "weight": 50,
        "patterns": [
            r"sk-[A-Za-z0-9]{20,}",
            r"AKIA[0-9A-Z]{16}",
            r"ghp_[A-Za-z0-9]{36}",
            r"AIza[0-9A-Za-z\-_]{35}",
            r"xoxb-[0-9A-Za-z\-]{50,}",
        ],
    },
    "JWT_LEAKAGE": {
        "weight": 30,
        "patterns": [
            r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
        ],
    },
    "EMAIL_EXPOSURE": {
        "weight": 10,
        "patterns": [
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        ],
    },
    "PHONE_NUMBER_EXPOSURE": {
        "weight": 15,
        "patterns": [
            r"\+?[0-9]{1,3}[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}",
        ],
    },
    "ENV_VAR_LEAKAGE": {
        "weight": 50,
        "patterns": [
            r"API_KEY\s*=\s*\S+",
            r"DATABASE_URL\s*=\s*\S+",
            r"SECRET_KEY\s*=\s*\S+",
            r"ACCESS_TOKEN\s*=\s*\S+",
            r"PRIVATE_KEY\s*=\s*\S+",
            r"PASSWORD\s*=\s*\S+",
        ],
    },
    "SENSITIVE_FILE_REFERENCE": {
        "weight": 25,
        "patterns": [
            r"\.env\b",
            r"credentials\.json",
            r"secrets\.yaml",
            r"secrets\.yml",
            r"id_rsa",
            r"\.pem\b",
            r"service-account\.json",
        ],
    },
}
