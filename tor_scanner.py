#!/usr/bin/env python3

import requests
import time
import re
import sys
import os
import sqlite3
from datetime import datetime
from pathlib import Path
import platform

try:
    from colorama import init, Fore, Style
    if platform.system() == "Windows":
        from colorama import just_fix_windows_console
        just_fix_windows_console()
    init(autoreset=True)
except ImportError:
    print("[*] Installing colorama...")
    os.system(f"{sys.executable} -m pip install colorama --quiet")
    from colorama import init, Fore, Style
    if platform.system() == "Windows":
        from colorama import just_fix_windows_console
        just_fix_windows_console()
    init(autoreset=True)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("[*] Installing beautifulsoup4...")
    os.system(f"{sys.executable} -m pip install beautifulsoup4 lxml --quiet")
    from bs4 import BeautifulSoup


class Banner:
    @staticmethod
    def show():
        ascii_logo = r"""
████████╗ ██████╗ ██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
╚══██╔══╝██╔═══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
   ██║   ██║   ██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
   ██║   ██║   ██║██╔══██╗    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██║    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""
        print(Fore.LIGHTMAGENTA_EX + "═" * 80)
        print(Fore.LIGHTCYAN_EX + ascii_logo)
        print(Fore.LIGHTMAGENTA_EX + "═" * 80)
        print(Fore.LIGHTGREEN_EX + "[OK] Linux Debian compatible")
        print(Fore.LIGHTGREEN_EX + "[OK] No Tor required (clearnet only)")
        print(Fore.LIGHTGREEN_EX + "[OK] Security rating system")
        print(Fore.LIGHTGREEN_EX + "[OK] Malware detection\n" + Style.RESET_ALL)


class Log:
    @staticmethod
    def ok(m): print(f"{Fore.LIGHTGREEN_EX}[OK] {m}{Style.RESET_ALL}")
    @staticmethod
    def info(m): print(f"{Fore.LIGHTCYAN_EX}[INFO] {m}{Style.RESET_ALL}")
    @staticmethod
    def warn(m): print(f"{Fore.LIGHTYELLOW_EX}[WARN] {m}{Style.RESET_ALL}")
    @staticmethod
    def err(m): print(f"{Fore.LIGHTRED_EX}[ERR] {m}{Style.RESET_ALL}")
    @staticmethod
    def scan(m): print(f"{Fore.LIGHTMAGENTA_EX}[SCAN] {m}{Style.RESET_ALL}")
    @staticmethod
    def found(m): print(f"{Fore.LIGHTGREEN_EX}[FOUND] {m}{Style.RESET_ALL}")
    @staticmethod
    def safe(m): print(f"{Fore.GREEN}[SAFE] {m}{Style.RESET_ALL}")
    @staticmethod
    def danger(m): print(f"{Fore.RED}[DANGER] {m}{Style.RESET_ALL}")
    @staticmethod
    def warning(m): print(f"{Fore.YELLOW}[WARNING] {m}{Style.RESET_ALL}")


class SecurityAnalyzer:
    def __init__(self):
        self.malware_keywords = [
            'malware', 'trojan', 'virus', 'ransomware', 'keylogger', 'botnet',
            'exploit', 'backdoor', 'spyware', 'rat', 'stealer', 'cryptolocker',
            'infected', 'hack', 'brute', 'force', 'crack', 'nulled', 'bypass'
        ]
        
        self.suspicious_keywords = [
            'carding', 'cc', 'dumps', 'paypal', 'bank', 'login', 'password',
            'account', 'fake', 'counterfeit', 'scam', 'fraud', 'phishing',
            'cheat', 'hack', 'bypass', 'crack', 'keygen', 'serial'
        ]
        
        self.trusted_keywords = [
            'market', 'forum', 'community', 'wiki', 'directory', 'search',
            'library', 'archive', 'blog', 'news', 'guide', 'help', 'support'
        ]
        
        self.trusted_sources = ['Dark.fail', 'Tor.taxi'] 

    def analyze_safety(self, data):
        """
        Analizza la sicurezza di un sito onion
        Restituisce: 'safe', 'warning', 'danger'
        """
        title = data.get('title', '').lower()
        source = data.get('source', '')
        category = data.get('category', '').lower()
        
        score = 0
        reasons = []

        for keyword in self.malware_keywords:
            if keyword in title:
                score += 3
                reasons.append(f"Keyword malware: {keyword}")
        
        for keyword in self.suspicious_keywords:
            if keyword in title:
                score += 1
                reasons.append(f"Keyword sospetto: {keyword}")
        
        for keyword in self.trusted_keywords:
            if keyword in title:
                score -= 1
                reasons.append(f"Keyword affidabile: {keyword}")

        if source in self.trusted_sources:
            score -= 2
            reasons.append(f"Fonte affidabile: {source}")
        if 'verified' in category:
            score -= 2
            reasons.append("Categoria verificata")
        elif 'market' in category:
            score += 1
            reasons.append("Mercato (rischio moderato)")
        if score >= 3:
            return 'danger', reasons
        elif score >= 1:
            return 'warning', reasons
        else:
            return 'safe', reasons


class Files:
    def __init__(self, base='onion_results'):
        self.base = Path(base)
        self.base.mkdir(exist_ok=True)
        self.dirs = {
            'all': self.base / 'all_onions',
            'verified': self.base / 'verified',
            'markets': self.base / 'marketplaces',
            'forums': self.base / 'forums',
            'services': self.base / 'services',
            'logs': self.base / 'daily_logs',
            'safe': self.base / 'safe_sites',
            'danger': self.base / 'dangerous_sites',
            'warning': self.base / 'suspicious_sites'
        }
        for d in self.dirs.values():
            d.mkdir(exist_ok=True)
        Log.ok(f"Storage initialized: {self.base}")

    def save(self, data, cat='all'):
        date = datetime.now().strftime('%Y-%m-%d')
        f = self.dirs[cat] / f"{cat}_{date}.txt"
        with open(f, 'a', encoding='utf-8') as file:
            file.write(f"\n{'='*80}\n")
            file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] NEW ONION\n")
            file.write(f"{'='*80}\n")
            file.write(f"Address: {data['address']}\n")
            file.write(f"Source: {data.get('source', 'Unknown')}\n")
            file.write(f"Category: {data.get('category', 'Unknown')}\n")
            file.write(f"Security: {data.get('security', 'unknown')}\n")
            if data.get('security_reasons'):
                file.write(f"Security reasons: {', '.join(data['security_reasons'])}\n")
            if data.get('title'):
                file.write(f"Title: {data['title']}\n")
            if data.get('verified'):
                file.write(f"Status: VERIFIED\n")
            file.write("\n")

    def master(self, onions):
        f = self.base / 'MASTER_LIST.txt'
        with open(f, 'w', encoding='utf-8') as file:
            file.write(f"MASTER ONION LIST - SECURITY RATED\n")
            file.write(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            safe_count = sum(1 for o in onions.values() if o.get('security') == 'safe')
            warning_count = sum(1 for o in onions.values() if o.get('security') == 'warning')
            danger_count = sum(1 for o in onions.values() if o.get('security') == 'danger')
            
            file.write(f"Total: {len(onions)} | Safe: {safe_count} | "
                      f"Warning: {warning_count} | Danger: {danger_count}\n")
            file.write(f"{'='*80}\n\n")

            file.write(f"\n{'='*50}\nSAFE SITES\n{'='*50}\n")
            safe_sites = [addr for addr, data in onions.items() if data.get('security') == 'safe']
            for addr in sorted(safe_sites):
                file.write(f"{addr}\n")

            file.write(f"\n{'='*50}\nSUSPICIOUS SITES (WARNING)\n{'='*50}\n")
            warning_sites = [addr for addr, data in onions.items() if data.get('security') == 'warning']
            for addr in sorted(warning_sites):
                file.write(f"{addr}\n")

            file.write(f"\n{'='*50}\nDANGEROUS SITES\n{'='*50}\n")
            danger_sites = [addr for addr, data in onions.items() if data.get('security') == 'danger']
            for addr in sorted(danger_sites):
                file.write(f"{addr}\n")

    def security_report(self, stats):
        f = self.dirs['logs'] / f"security_report_{datetime.now().strftime('%Y-%m-%d')}.txt"
        with open(f, 'w', encoding='utf-8') as file:
            file.write(f"SECURITY ANALYSIS REPORT\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"{'='*50}\n")
            file.write(f"Total sites: {stats['total']}\n")
            file.write(f"Safe sites: {stats['safe']}\n")
            file.write(f"Suspicious sites: {stats['warning']}\n")
            file.write(f"Dangerous sites: {stats['danger']}\n")
            security_score = (stats['safe'] / stats['total'] * 100) if stats['total'] > 0 else 0
            file.write(f"Security score: {security_score:.1f}%\n")

    def stats(self, s):
        f = self.dirs['logs'] / f"stats_{datetime.now().strftime('%Y-%m-%d')}.txt"
        with open(f, 'w', encoding='utf-8') as file:
            file.write(f"DAILY STATISTICS REPORT\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            for k, v in s.items():
                file.write(f"{k.upper()}: {v}\n")


class Collector:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.s.timeout = 15
        self.pattern = re.compile(r'\b([a-z2-7]{16}|[a-z2-7]{56})\.onion\b', re.I)
        self.security = SecurityAnalyzer()

    def extract(self, text):
        return list(set(self.pattern.findall(text)))

    def ahmia(self):
        onions = {}
        try:
            Log.scan("Ahmia...")
            for q in ['', 'market', 'forum', 'wiki']:
                try:
                    r = self.s.get(f"https://ahmia.fi/search/?q={q}", timeout=15)
                    r.raise_for_status()
                    for a in self.extract(r.text):
                        security, reasons = self.security.analyze_safety({
                            'address': a, 
                            'source': 'Ahmia', 
                            'category': f'search_{q}' if q else 'search'
                        })
                        onions[a] = {
                            'address': a, 
                            'source': 'Ahmia', 
                            'category': f'search_{q}' if q else 'search',
                            'security': security,
                            'security_reasons': reasons
                        }
                    time.sleep(2)
                except Exception as e:
                    Log.warn(f"Ahmia query '{q}': {e}")
                    continue
            Log.found(f"Ahmia: {len(onions)}")
        except Exception as e:
            Log.warn(f"Ahmia: {e}")
        return onions

    def darkfail(self):
        onions = {}
        try:
            Log.scan("Dark.fail...")
            r = self.s.get("https://dark.fail/", timeout=15)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, 'html.parser')
            for link in soup.find_all('a', href=re.compile(r'\.onion')):
                m = self.pattern.search(link.get('href', ''))
                if m:
                    a = m.group(0)
                    title = link.get_text(strip=True)[:100]
                    security, reasons = self.security.analyze_safety({
                        'address': a,
                        'source': 'Dark.fail',
                        'category': 'verified',
                        'title': title,
                        'verified': True
                    })
                    onions[a] = {
                        'address': a,
                        'source': 'Dark.fail',
                        'category': 'verified',
                        'title': title,
                        'verified': True,
                        'security': security,
                        'security_reasons': reasons
                    }
            Log.found(f"Dark.fail: {len(onions)}")
        except Exception as e:
            Log.warn(f"Dark.fail: {e}")
        return onions

    def onionland(self):
        onions = {}
        try:
            Log.scan("OnionLand...")
            for url in ["https://onionlandsearchengine.com/", "https://onionlandsearchengine.com/fresh"]:
                try:
                    r = self.s.get(url, timeout=15)
                    r.raise_for_status()
                    for a in self.extract(r.text):
                        security, reasons = self.security.analyze_safety({
                            'address': a, 
                            'source': 'OnionLand', 
                            'category': 'search'
                        })
                        onions[a] = {
                            'address': a, 
                            'source': 'OnionLand', 
                            'category': 'search',
                            'security': security,
                            'security_reasons': reasons
                        }
                    time.sleep(1)
                except Exception as e:
                    Log.warn(f"OnionLand {url}: {e}")
                    continue
            Log.found(f"OnionLand: {len(onions)}")
        except Exception as e:
            Log.warn(f"OnionLand: {e}")
        return onions

    def tortaxi(self):
        onions = {}
        try:
            Log.scan("Tor.taxi...")
            r = self.s.get("https://tor.taxi/", timeout=15)
            r.raise_for_status()
            for a in self.extract(r.text):
                security, reasons = self.security.analyze_safety({
                    'address': a, 
                    'source': 'Tor.taxi', 
                    'category': 'directory'
                })
                onions[a] = {
                    'address': a, 
                    'source': 'Tor.taxi', 
                    'category': 'directory',
                    'security': security,
                    'security_reasons': reasons
                }
            Log.found(f"Tor.taxi: {len(onions)}")
        except Exception as e:
            Log.warn(f"Tor.taxi: {e}")
        return onions

    def all(self):
        result = {}
        for func in [self.ahmia, self.darkfail, self.onionland, self.tortaxi]:
            try:
                result.update(func())
                time.sleep(3)
            except Exception as e:
                Log.warn(f"Scanner {func.__name__} failed: {e}")
                continue
        return result


class Scanner:
    def __init__(self):
        self.db = 'onion_scanner.db'
        self.files = Files()
        self.coll = Collector()
        self.stats = {
            'total': 0, 'new': 0, 'verified': 0, 'markets': 0, 
            'forums': 0, 'services': 0, 'cycles': 0,
            'safe': 0, 'warning': 0, 'danger': 0
        }
        self.start = datetime.now()
        self.known = {}
        self.running = True
        self.init_db()
        self.load()

    def init_db(self):
        try:
            c = sqlite3.connect(self.db)

            c.execute('''CREATE TABLE IF NOT EXISTS onions
                         (address TEXT PRIMARY KEY, first TEXT, last TEXT,
                          source TEXT, category TEXT, title TEXT, verified INT,
                          security TEXT, security_reasons TEXT)''')

            cursor = c.execute("PRAGMA table_info(onions)")
            columns = [column[1] for column in cursor.fetchall()]
            
            if 'security' not in columns:
                Log.info("Upgrading database: adding security column")
                c.execute("ALTER TABLE onions ADD COLUMN security TEXT")
            
            if 'security_reasons' not in columns:
                Log.info("Upgrading database: adding security_reasons column")
                c.execute("ALTER TABLE onions ADD COLUMN security_reasons TEXT")
            
            c.commit()
            c.close()
            Log.ok(f"DB initialized: {self.db}")
        except sqlite3.Error as e:
            Log.err(f"Database initialization failed: {e}")
            sys.exit(1)

    def load(self):
        try:
            c = sqlite3.connect(self.db)
            cursor = c.execute("SELECT address, source, category, title, security, security_reasons FROM onions")
            
            for row in cursor:
                security_reasons = []
                if row[5]: 
                    security_reasons = [r.strip() for r in row[5].split(',')]
                
                self.known[row[0]] = {
                    'address': row[0], 
                    'source': row[1], 
                    'category': row[2], 
                    'title': row[3],
                    'security': row[4],
                    'security_reasons': security_reasons
                }
            Log.info(f"Loaded: {len(self.known)} entries")
            c.close()
        except sqlite3.Error as e:
            Log.warn(f"Error loading database: {e}")
            Log.info("Starting with empty dataset...")
            self.known = {}

    def save_db(self, d):
        try:
            c = sqlite3.connect(self.db)
            now = datetime.now().isoformat()
            security_reasons = ', '.join(d.get('security_reasons', [])) if d.get('security_reasons') else None
            
            if c.execute("SELECT 1 FROM onions WHERE address=?", (d['address'],)).fetchone():
                c.execute("""UPDATE onions SET last=?, source=?, category=?, title=?, verified=?, 
                             security=?, security_reasons=? WHERE address=?""",
                          (now, d.get('source'), d.get('category'), d.get('title'), 
                           1 if d.get('verified') else 0, d.get('security'), 
                           security_reasons, d['address']))
            else:
                c.execute("""INSERT INTO onions VALUES (?,?,?,?,?,?,?,?,?)""",
                          (d['address'], now, now, d.get('source'), d.get('category'), 
                           d.get('title'), 1 if d.get('verified') else 0,
                           d.get('security'), security_reasons))
            c.commit()
            c.close()
        except sqlite3.Error as e:
            Log.err(f"Database save error for {d['address']}: {e}")

    def cycle(self):
        Log.info("Scanning...")
        try:
            new = self.coll.all()
            truly_new = {a: d for a, d in new.items() if a not in self.known}
            
            if truly_new:
                Log.found(f"{len(truly_new)} new onions")
                for addr, data in truly_new.items():
                    security = data.get('security', 'unknown')
                    if security == 'safe':
                        self.stats['safe'] += 1
                        Log.safe(f"Safe site: {addr}")
                    elif security == 'warning':
                        self.stats['warning'] += 1
                        Log.warning(f"Suspicious site: {addr}")
                    elif security == 'danger':
                        self.stats['danger'] += 1
                        Log.danger(f"Dangerous site: {addr}")
                    
                    cat_f = 'all'
                    if data.get('verified'):
                        cat_f = 'verified'
                        self.stats['verified'] += 1
                    
                    cat = data.get('category', '').lower()
                    if 'market' in cat:
                        cat_f = 'markets'
                        self.stats['markets'] += 1
                    elif 'forum' in cat:
                        cat_f = 'forums'
                        self.stats['forums'] += 1
                    elif 'service' in cat or 'search' in cat:
                        cat_f = 'services'
                        self.stats['services'] += 1

                    security_cat = data.get('security', 'unknown')
                    if security_cat in ['safe', 'warning', 'danger']:
                        self.files.save(data, security_cat)
                    
                    print(f"\n{'='*70}\nNEW: {addr}\nSecurity: {security}\n{'='*70}")
                    if data.get('security_reasons'):
                        print(f"Reasons: {', '.join(data['security_reasons'])}")
                    
                    self.save_db(data)
                    self.files.save(data, 'all')
                    self.files.save(data, cat_f)
                    self.known[addr] = data
                    self.stats['new'] += 1
            else:
                Log.info("No new onions")
            
            self.stats['total'] = len(self.known)
            self.files.master(self.known)
            self.files.security_report(self.stats)
            
        except Exception as e:
            Log.err(f"Scan cycle failed: {e}")

    def show_stats(self):
        up = str(datetime.now() - self.start).split('.')[0]
        print(f"\n{'='*70}\nSTATISTICS & SECURITY OVERVIEW\n{'='*70}")
        for k, v in self.stats.items():
            if k in ['safe', 'warning', 'danger']:
                color = Fore.GREEN if k == 'safe' else Fore.YELLOW if k == 'warning' else Fore.RED
                print(f"{color}{k}: {v}{Style.RESET_ALL}")
            else:
                print(f"{k}: {v}")
        print(f"Uptime: {up}\n{'='*70}\n")

    def run(self):
        Banner.show()
        Log.info(f"System: {platform.system()} {platform.release()}")
        Log.info(f"Python: {sys.version}")
        Log.ok("Security analyzer activated")
        Log.ok("Ready - press Ctrl+C to stop\n")
        
        try:
            while self.running:
                self.stats['cycles'] += 1
                print(f"\n{'-'*70}\nCYCLE #{self.stats['cycles']} - {datetime.now().strftime('%H:%M:%S')}\n{'-'*70}")
                self.cycle()
                self.show_stats()
                self.stats['uptime'] = str(datetime.now() - self.start).split('.')[0]
                self.files.stats(self.stats)
                wait = 300 
                Log.info(f"Next scan in {wait}s...")
                time.sleep(wait)
                
        except KeyboardInterrupt:
            Log.warn("Stopping...")
        except Exception as e:
            Log.err(f"Fatal error: {e}")
        finally:
            Log.ok(f"Done - total: {self.stats['total']}")
            Log.info(f"Results saved in: {self.files.base}")


if __name__ == "__main__":
    try:
        Scanner().run()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
